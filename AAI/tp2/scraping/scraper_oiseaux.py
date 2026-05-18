import os
from mimetypes import guess_extension
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import requests
import os
import io
from PIL import Image
import hashlib
import time
import random
import logging
from datetime import datetime
from config import DRIVER_PATH

# Configuration du logging
log_dir = "../data/logs"
if not os.path.exists(log_dir):
    os.makedirs(log_dir)

log_file = os.path.join(log_dir, f"scraping_{datetime.now().strftime('%Y%m%d_%H%M%S')}.log")
logging.basicConfig(
    level=logging.INFO,
    format='[%(asctime)s] %(levelname)s: %(message)s',
    handlers=[
        logging.FileHandler(log_file),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)
logger.info("=== Debut du scraping ===")


def fetch_image_urls(query:str, max_links_to_fetch:int, wd:webdriver, sleep_between_interactions:int=3):
    def scroll_to_end(wd, scroll_point):  
        wd.execute_script(f"window.scrollTo(0, {scroll_point});")
        time.sleep(sleep_between_interactions)    
 
        
    search_url = f"https://www.bing.com/images/search?q={query}"

    print(f"[SEARCH] Ouverture de : {search_url}")
    wd.get(search_url)
    print(f"[WAIT] Attente du chargement initial...")
    time.sleep(5)  # Attendre le chargement complet
    
    image_urls = set()
    image_count = 0
    number_results = 0
    
    try:
        # Attendre que les images se chargent
        WebDriverWait(wd, 10).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, "img.mimg"))
        )
        print("[OK] Images detectees")
    except:
        print("[WARNING] Timeout en attendant les images")
    
    scroll_errors = 0
    for i in range(1,20):
        try:
            scroll_to_end(wd, i*1000)
            time.sleep(2)
            thumb = wd.find_elements(By.CSS_SELECTOR, "img.mimg")
            print(f"[SCROLL {i}] {len(thumb)} images trouvees")
            time.sleep(2)
            for img in thumb:
                try:
                    # Try to get src first, then fall back to data-src for lazy-loaded images
                    src = img.get_attribute('src')
                    if not src:
                        src = img.get_attribute('data-src')
                    if src and 'http' in src:
                        image_urls.add(src)
                except:
                    pass
                image_count = len(image_urls)
                number_results = image_count
                time.sleep(.2)
            print(f"[STATS] Total trouve : {number_results} images")
            scroll_errors = 0  # Reset error counter on success
            if number_results >= max_links_to_fetch:
                break
        except Exception as e:
            scroll_errors += 1
            print(f"[ERROR] Scroll {i} echoue : {str(e)[:50]}...")
            if scroll_errors >= 3:
                print(f"[STOP] Trop d'erreurs de scroll, arret du scraping")
                break
            time.sleep(2)  # Wait before retrying
            continue
    print(f"[SUCCESS] Scraping termine : {len(image_urls)} images recuperees")
    return image_urls


def persist_image(folder_path:str,url:str):
    image_content = None
    try:
        # Délai aléatoire entre 1 et 3 secondes pour ne pas surcharger le serveur
        delay = random.uniform(1, 3)
        time.sleep(delay)
        
        headers = {'User-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'}
        response = requests.get(url, headers=headers, timeout=15)
        response.raise_for_status()
        image_content = response.content
        logger.info(f"URL telechargee : {url}")
    except requests.Timeout:
        logger.error(f"TIMEOUT : {url}")
        return
    except requests.ConnectionError as e:
        logger.error(f"CONNEXION ERREUR : {url} - {str(e)[:50]}")
        return
    except requests.HTTPError as e:
        logger.error(f"HTTP ERREUR {response.status_code} : {url}")
        return
    except Exception as e:
        logger.error(f"ERREUR telechargement : {url} - {str(e)[:50]}")
        print(f"[ERROR] Could not download {url} - {str(e)[:50]}")
        return
    
    if image_content:
        try:
            image_file = io.BytesIO(image_content)
            image = Image.open(image_file).convert('RGB')
            file_path = os.path.join(folder_path, hashlib.sha1(image_content).hexdigest()[:10] + '.jpg')
            with open(file_path, 'wb') as f:
                image.save(f, "JPEG", quality=85)
            logger.info(f"SUCCES : {file_path}")
            print(f"[SAVED] {file_path}")
        except Exception as e:
            logger.error(f"ERREUR sauvegarde : {url} - {str(e)[:50]}")
            print(f"[ERROR] Could not save {url} - {str(e)[:50]}")


def search_and_download(search_term:str,driver_path:str,target_path='../data/brutes',number_images=100):
    
    logger.info(f"--- DEBUT : Scraping '{search_term}' ---")
    species_folder = '_'.join(search_term.lower().split(' '))
    target_folder = os.path.join(target_path, species_folder)
    if not os.path.exists(target_folder):
            os.makedirs(target_folder)
            print(f"[FOLDER] Created : {target_folder}")
            logger.info(f"Dossier cree : {target_folder}")
    with webdriver.Chrome(service=Service(driver_path)) as wd:
            res = fetch_image_urls(search_term, number_images, wd=wd, sleep_between_interactions=3)
            
    print(f"[DOWNLOAD] Telechargement de {len(res)} images pour '{search_term}'...")
    print(f"[PATH] Destination : {target_folder}")
    logger.info(f"Telechargement de {len(res)} images")
    downloaded = 0
    failed = 0
    for elem in res:
        try:
            persist_image(target_folder,elem)
            downloaded += 1
        except Exception as e:
            failed += 1
            logger.error(f"Echec image {elem}: {str(e)[:50]}")

        
        time.sleep(random.uniform(0.5, 1.5))
    
    logger.info(f"--- FIN : {search_term} | Telecharges: {downloaded}, Echoues: {failed} ---")


if __name__ == "__main__":
    search_terms = ["Hibou grand-duc", "Flamant rose", "Martin-pêcheur", "Cygne tuberculé", "Pic vert"]
    for search_term in search_terms:
        search_and_download(search_term=search_term, driver_path=DRIVER_PATH)
    
    logger.info("=== Scraping termine avec succes ===")
    print(f"\n[DONE] Les logs sont sauvegardes dans : {log_file}")
    
# driver = webdriver.Chrome()

# # Go to the Google home page
# driver.get('https://www.google.com')

# # Download content to temp folder
# asset_dir = "data"
# os.makedirs(asset_dir, exist_ok=True)
# download_assets(driver.request, asset_dir=asset_dir)

# driver.close()