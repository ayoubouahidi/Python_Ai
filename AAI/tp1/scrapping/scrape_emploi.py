import os
import re
import json
import time
import random
import requests
import pandas as pd
import matplotlib.pyplot as plt
from bs4 import BeautifulSoup
from urllib.parse import urljoin

try:
    from tqdm import tqdm
except ImportError:
    def tqdm(iterable, **kwargs):
        return iterable

from config import BASE_URL, START_URL, HEADERS, REQUEST_DELAY, TIMEOUT, MAX_PAGES

SEARCH_URL = START_URL
CACHE_CSV_PATH = os.path.join(os.path.dirname(__file__), "job_urls_cache.csv")
OUTPUT_JSON_PATH = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "..", "data", "brutes", "offres_emploi_details.json")
)
USE_CACHE = True
FORCE_REFRESH = False


def clean_text(value):
    if not value:
        return None
    return re.sub(r"\s+", " ", value).strip()


def text_from_selectors(soup, selectors):
    for selector in selectors:
        node = soup.select_one(selector)
        if node:
            text = clean_text(node.get_text(" ", strip=True))
            if text:
                return text
    return None


def fetch_offer_details(url, session):
    """Télécharge une offre et retourne ses détails sans échouer si des champs manquent."""
    try:
        response = session.get(url, headers=HEADERS, timeout=TIMEOUT)
        response.raise_for_status()
    except requests.RequestException as e:
        return {
            "url": url,
            "title": None,
            "company": None,
            "description": None,
            "location": None,
            "contract_type": None,
            "error": str(e),
            "missing_fields": ["title", "company", "description", "location", "contract_type"],
        }

    soup = BeautifulSoup(response.text, "html.parser")

    title = text_from_selectors(soup, ["h1", ".job-ad-title", "title"])
    company = text_from_selectors(soup, ["a[href*='/recruteur/']", ".company-title", ".field-name-field-offre-entreprise"])
    description = text_from_selectors(soup, [".job-ad-description", ".field-name-body", "article"])
    location = text_from_selectors(soup, [".field-name-field-offre-region", ".job-ad-criteria__value", ".field-name-field-ville"])
    contract_type = text_from_selectors(soup, [".field-name-field-offre-type-contrat", ".job-ad-criteria"])

    details = {
        "url": url,
        "title": title,
        "company": company,
        "description": description,
        "location": location,
        "contract_type": contract_type,
        "error": None,
    }
    details["missing_fields"] = [key for key in ["title", "company", "description", "location", "contract_type"] if not details.get(key)]
    return details

if USE_CACHE and not FORCE_REFRESH and os.path.exists(CACHE_CSV_PATH):
    cache_df = pd.read_csv(CACHE_CSV_PATH)
    if "url" in cache_df.columns:
        job_urls = sorted({str(url).strip() for url in cache_df["url"].dropna() if str(url).strip()})
        print(f"Cache chargé depuis {CACHE_CSV_PATH}")
    else:
        print("Le cache existe mais la colonne 'url' est absente. Nouveau scraping...")
        job_urls = []
else:
    job_urls = []

if not job_urls:
    session = requests.Session()
    job_urls_set = set()

    try:
        first_response = session.get(SEARCH_URL, headers=HEADERS, timeout=TIMEOUT)
        first_response.raise_for_status()
    except requests.RequestException as e:
        print(f"Erreur de requête (page 1): {e}")
    else:
        first_soup = BeautifulSoup(first_response.text, "html.parser")

        page_numbers = []
        for a in first_soup.select("a[href]"):
            href = a.get("href") or ""
            m = re.search(r"[?&]page=(\d+)", href)
            if m:
                page_numbers.append(int(m.group(1)))

        total_pages = (max(page_numbers) + 1) if page_numbers else 1
        if MAX_PAGES and MAX_PAGES > 0:
            total_pages = min(total_pages, MAX_PAGES)

        print(f"Pages à scraper: {total_pages}")

        for page_index in range(total_pages):
            page_url = SEARCH_URL if page_index == 0 else f"{SEARCH_URL}?page={page_index}"

            sleep_s = random.uniform(max(0.5, REQUEST_DELAY), max(1.5, REQUEST_DELAY + 2))
            print(f"Attente polie: {sleep_s:.2f}s avant {page_url}")
            time.sleep(sleep_s)

            try:
                response = session.get(page_url, headers=HEADERS, timeout=TIMEOUT)
                response.raise_for_status()
            except requests.RequestException as e:
                print(f"Erreur de requête ({page_url}): {e}")
                continue

            soup = BeautifulSoup(response.text, "html.parser")

            page_job_urls = {
                urljoin(BASE_URL, href)
                for href in [a.get("href") for a in soup.select("a[href]")]
                if href and "/offre-emploi-maroc/" in href.lower()
            }

            job_urls_set.update(page_job_urls)

        job_urls = sorted(job_urls_set)

    pd.DataFrame({"url": job_urls}).to_csv(CACHE_CSV_PATH, index=False, encoding="utf-8")
    print(f"Cache sauvegardé dans {CACHE_CSV_PATH}")

print(f"URLs detectees: {len(job_urls)}")
for url in job_urls[:20]:
    print(url)

details_session = requests.Session()
offers_details = []
for url in tqdm(job_urls, desc="Scraping details", unit="offre"):
    offers_details.append(fetch_offer_details(url, details_session))

os.makedirs(os.path.dirname(OUTPUT_JSON_PATH), exist_ok=True)
with open(OUTPUT_JSON_PATH, "w", encoding="utf-8") as f:
    json.dump(offers_details, f, ensure_ascii=False, indent=2)

print(f"Offres detaillees collectees: {len(offers_details)}")
print(f"JSON sauvegarde: {OUTPUT_JSON_PATH}")
print(offers_details[:3])