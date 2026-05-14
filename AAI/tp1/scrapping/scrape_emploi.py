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

import html

import nltk
import spacy
from nltk.corpus import stopwords

nltk.download("punkt", quiet=True)
nltk.download("punkt_tab", quiet=True)
nltk.download("stopwords", quiet=True)

# Initialize NLTK stopwords for French
STOP_WORDS_FR = set(stopwords.words("french"))

# Initialize spaCy model
try:
    nlp = spacy.load("fr_core_news_sm")
except OSError:
    print("Downloading spaCy French model...")
    import subprocess
    subprocess.run(["python", "-m", "spacy", "download", "fr_core_news_sm"], check=True)
    nlp = spacy.load("fr_core_news_sm")

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
OUTPUT_NETTOYEES_PATH = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "..", "data", "brutes", "offres_emploi_nettoyees.csv")
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
        # "salaire": 
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

        # ==================== PAGINATION ====================
        # Extraire les numéros de page disponibles
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

            # ==================== POLITESSE (DÉLAI) ====================
            # Ajouter un délai aléatoire pour respecter le serveur
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

# partie 5 



def nettoyer_texte(texte):

    if not texte:
        return ""
    texte = html.unescape(texte)
    texte = re.sub(r"<[^>]+>", " ", texte)
 
    texte = re.sub(
        r"[^\w\s.,;:!?'\"\(\)\-àâäéèêëîïôöùûüçÀÂÄÉÈÊËÎÏÔÖÙÛÜÇ]",
        " ",
        texte,
    )
    # Normalisation : retours à la ligne excessifs → double saut de ligne
    texte = re.sub(r"\n{3,}", "\n\n", texte)
    # Normalisation : espaces multiples → espace simple
    texte = re.sub(r" {2,}", " ", texte)
    return texte.strip()

def tokeniser(texte):
    tokens = nltk.word_tokenize(texte, language="french")
    tokens = [
        t.lower()
        for t in tokens
        if re.search(r"[a-zA-ZàâäéèêëîïôöùûüçÀÂÄÉÈÊËÎÏÔÖÙÛÜÇ]", t)
    ]
    return tokens

 
def supprimer_stop_words(tokens):
    return [t for t in tokens if t not in STOP_WORDS_FR]
 
 
def lemmatiser(tokens):
    doc = nlp(" ".join(tokens))
    return [token.lemma_.lower() for token in doc if token.lemma_.strip()]

def pipeline_nettoyage(texte):

    texte_propre = nettoyer_texte(texte)
    tokens = tokeniser(texte_propre)
    tokens = supprimer_stop_words(tokens)
    lemmes = lemmatiser(tokens)
    return {
        "description_nettoyee": texte_propre,
        "tokens": lemmes,
        "tokens_str": " ".join(lemmes),
    }


rows = []
for offre in tqdm(offers_details, desc="Nettoyage NLP", unit="offre"):
    description_brute = offre.get("description") or ""
    resultat = pipeline_nettoyage(description_brute)
 
    rows.append({
        "url":                  offre.get("url"),
        "title":                offre.get("title"),
        "company":              offre.get("company"),
        "location":             offre.get("location"),
        "contract_type":        offre.get("contract_type"),
        "description_brute":    description_brute,
        "description_nettoyee": resultat["description_nettoyee"],
        "tokens":               resultat["tokens_str"],
    })
 
df_nettoyees = pd.DataFrame(rows)
 
os.makedirs(os.path.dirname(OUTPUT_NETTOYEES_PATH), exist_ok=True)
df_nettoyees.to_csv(OUTPUT_NETTOYEES_PATH, index=False, encoding="utf-8")
 
print(f"[Partie 5] Descriptions nettoyées sauvegardées : {OUTPUT_NETTOYEES_PATH}")
print(f"[Partie 5] Nombre d'offres traitées : {len(df_nettoyees)}")
print(df_nettoyees[["title", "description_nettoyee", "tokens"]].head(3))

# partie 6

#Extraction de compétences
skills_list = [
    "python", "java", "c++", "sql", "excel",
    "javascript", "html", "css", "react",
    "django", "node", "linux","word","powerpoint"
]

def extract_skills(text):
    found = []

    text = text.lower()

    for skill in skills_list:
        if skill in text:
            found.append(skill)

    return found

df = pd.read_json("/content/projet_emploi/data/brutes/jobs.json")
df["skills"] = df["description"].apply(extract_skills)

print(df[["titre", "skills"]].head())

from wordcloud import WordCloud
import matplotlib.pyplot as plt

text = " ".join(df["description"].dropna())

wordcloud = WordCloud(width=800, height=400).generate(text)

plt.imshow(wordcloud)
plt.axis("off")
plt.show()

print("Nombre total d'offres:", len(df))
from collections import Counter

all_skills = []

for skills in df["skills"]:
    all_skills.extend(skills)

top_skills = Counter(all_skills).most_common(10)

print(top_skills)
print(df["ville"].value_counts())

print(df["salaire"].describe())
skills, counts = zip(*top_skills)

plt.bar(skills, counts)
plt.xticks(rotation=45)
plt.title("Top compétences")
plt.show()

df["ville"].value_counts().plot(kind="bar")
plt.title("Répartition par ville")
plt.show()

