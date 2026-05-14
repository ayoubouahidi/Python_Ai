import os
from mimetypes import guess_extension
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import requests
import os
import io
from PIL import Image
import hashlib
import time
from config import DRIVER_PATH


def fetch_image_urls(query:str, max_links_to_fetch:int, wd:webdriver, sleep_between_interactions:int=3):
    def scroll_to_end(wd, scroll_point):  
        wd.execute_script(f"window.scrollTo(0, {scroll_point});")
        time.sleep(sleep_between_interactions)    
 
        
    search_url = f"https://www.bing.com/images/search?q={query}"

    wd.get(search_url)
    time.sleep(sleep_between_interactions)  
    
    image_urls = set()
    image_count = 0
    number_results = 0
    
    from selenium.webdriver.common.by import By
    
    for i in range(1,20):
        scroll_to_end(wd, i*1000)
        time.sleep(5)
        thumb = wd.find_elements(By.CSS_SELECTOR, "img.mimg")
        time.sleep(5)
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
            time.sleep(.5)
        print(f"Found: {number_results} search results. Extracting links...")
    return image_urls


def persist_image(folder_path:str,url:str):
    image_content = None
    try:
        headers = {'User-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'}
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
        image_content = response.content
    except Exception as e:
        print(f"ERROR - Could not download {url} - {e}")
        return
    
    if image_content:
        try:
            image_file = io.BytesIO(image_content)
            image = Image.open(image_file).convert('RGB')
            file_path = os.path.join(folder_path, hashlib.sha1(image_content).hexdigest()[:10] + '.jpg')
            with open(file_path, 'wb') as f:
                image.save(f, "JPEG", quality=85)
            print(f"SUCCESS - saved {url} - as {file_path}")
        except Exception as e:
            print(f"ERROR - Could not save {url} - {e}")


def search_and_download(search_term:str,driver_path:str,target_path='./images-BING',number_images=200):
    target_folder = os.path.join(target_path,'_'.join(search_term.lower().split(' ')))
    if not os.path.exists(target_folder):
            os.makedirs(target_folder)
    with webdriver.Chrome(service=Service(driver_path)) as wd:
            res = fetch_image_urls(search_term, number_images, wd=wd, sleep_between_interactions=3)
            
    print(f"Downloading {len(res)} images for '{search_term}'...")
    for elem in res:
        persist_image(target_folder,elem)


if __name__ == "__main__":
    search_terms = ["oiseaux"]
    for search_term in search_terms:
        search_and_download(search_term=search_term, driver_path=DRIVER_PATH)
    
# driver = webdriver.Chrome()

# # Go to the Google home page
# driver.get('https://www.google.com')

# # Download content to temp folder
# asset_dir = "data"
# os.makedirs(asset_dir, exist_ok=True)
# download_assets(driver.request, asset_dir=asset_dir)

# driver.close()