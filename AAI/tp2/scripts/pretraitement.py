"""
PRETRAITEMENT DES IMAGES
=========================
Ce script prépare les images pour le deep learning :
1. Redimensionnement à 224x224 (standard ML)
2. Normalisation des pixels [0,255] -> [0,1]
3. Conversion en JPG uniforme
4. Sauvegarde dans data/finales/
"""

import os
import logging
from PIL import Image
import numpy as np
from pathlib import Path
from datetime import datetime
from tqdm import tqdm

# Configuration du logging
log_dir = "../data/logs"
os.makedirs(log_dir, exist_ok=True)
log_file = os.path.join(log_dir, f"pretraitement_{datetime.now().strftime('%Y%m%d_%H%M%S')}.log")

logging.basicConfig(
    level=logging.INFO,
    format='[%(asctime)s] %(levelname)s: %(message)s',
    handlers=[
        logging.FileHandler(log_file),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)


# ============================================================
# ETAPE 1 : REDIMENSIONNEMENT
# ============================================================
def resize_image(image_path, target_size=(224, 224)):
    """
    Redimensionne une image à 224x224 pixels.
    
    Pourquoi 224x224 ?
    - C'est la taille standard pour les modèles ImageNet
    - Taille optimale CPU/GPU
    - Bon compromis entre qualité et vitesse
    """
    try:
        img = Image.open(image_path)
        
        # Redimensionner en gardant les proportions + crop si nécessaire
        # Utiliser LANCZOS pour meilleure qualité
        img_resized = img.resize(target_size, Image.Resampling.LANCZOS)
        
        return img_resized
    except Exception as e:
        logger.error(f"[REDIM] Erreur {image_path}: {e}")
        return None


# ============================================================
# ETAPE 2 : NORMALISATION
# ============================================================
def normalize_image(image):
    """
    Convertit les valeurs des pixels de [0,255] à [0,1].
    
    Pourquoi normaliser ?
    - Les modèles ML apprennent mieux avec des valeurs [0,1]
    - Réduit l'amplitude des gradients
    - Accélère l'apprentissage
    
    Processus :
    1. Convertir en array numpy
    2. Diviser par 255
    """
    try:
        # Convertir en array numpy
        img_array = np.array(image, dtype=np.float32)
        
        # Normaliser : diviser par 255
        img_normalized = img_array / 255.0
        
        # Résultat : valeurs entre 0 et 1
        return img_normalized
    except Exception as e:
        logger.error(f"[NORM] Erreur normalisation: {e}")
        return None


# ============================================================
# ETAPE 3 : CONVERSION EN JPG UNIFORME
# ============================================================
def save_as_jpg(image, output_path, quality=85):
    """
    Sauvegarde l'image en JPG avec compression standard.
    
    Format JPG :
    - Plus léger que PNG (compression avec perte)
    - Format standard pour les datasets
    - Quality 85 = bon compromis taille/qualité
    """
    try:
        # Convertir array normalisé en image PIL
        # Remettre entre 0-255 pour sauvegarde
        if isinstance(image, np.ndarray):
            img_uint8 = (image * 255).astype(np.uint8)
            img = Image.fromarray(img_uint8)
        else:
            img = image
        
        # Convertir en RGB si nécessaire (PNG -> RGB)
        if img.mode != 'RGB':
            img = img.convert('RGB')
        
        # Sauvegarder en JPG
        img.save(output_path, 'JPEG', quality=quality)
        logger.info(f"[SAVED] {os.path.basename(output_path)}")
        return True
    except Exception as e:
        logger.error(f"[SAVE] Erreur sauvegarde {output_path}: {e}")
        return False


# ============================================================
# ETAPE 4 : ORGANISATION FINALE
# ============================================================
def preprocess_image_file(input_path, output_path, target_size=(224, 224)):
    """
    Applique toutes les étapes de prétraitement à une image.
    """
    # Étape 1 : Redimensionner
    img_resized = resize_image(input_path, target_size)
    if img_resized is None:
        return False
    
    # Étape 2 : Normaliser
    img_normalized = normalize_image(img_resized)
    if img_normalized is None:
        return False
    
    # Étape 3 & 4 : Sauvegarder en JPG dans output
    success = save_as_jpg(img_normalized, output_path, quality=85)
    return success


def preprocess_dataset(input_base_folder="../data/brutes", 
                      output_base_folder="../data/finales",
                      target_size=(224, 224)):
    """
    Prétraite toutes les images du dataset.
    
    Structure :
    Input  : data/brutes/hibou_grand-duc/*.jpg
    Output : data/finales/hibou_grand-duc/*.jpg (redimensionnées + normalisées)
    """
    logger.info("=== DEBUT DU PRETRAITEMENT ===")
    logger.info(f"Input  : {input_base_folder}")
    logger.info(f"Output : {output_base_folder}")
    logger.info(f"Taille cible : {target_size}")
    
    # Vérifier que le dossier d'entrée existe
    if not os.path.exists(input_base_folder):
        logger.error(f"Dossier inexistant : {input_base_folder}")
        return
    
    # Créer le dossier de sortie
    os.makedirs(output_base_folder, exist_ok=True)
    
    # Parcourir chaque espèce
    species_folders = [f for f in os.listdir(input_base_folder) 
                       if os.path.isdir(os.path.join(input_base_folder, f))]
    
    total_processed = 0
    total_failed = 0
    
    for species in species_folders:
        input_species_path = os.path.join(input_base_folder, species)
        output_species_path = os.path.join(output_base_folder, species)
        
        # Créer le dossier d'espèce en sortie
        os.makedirs(output_species_path, exist_ok=True)
        
        logger.info(f"\n--- Traitement : {species} ---")
        
        # Lister les images
        images = [f for f in os.listdir(input_species_path) 
                  if f.lower().endswith(('.jpg', '.jpeg', '.png'))]
        
        # Traiter chaque image avec barre de progression
        for img_file in tqdm(images, desc=species):
            input_path = os.path.join(input_species_path, img_file)
            
            # Changer l'extension en .jpg
            output_filename = os.path.splitext(img_file)[0] + '.jpg'
            output_path = os.path.join(output_species_path, output_filename)
            
            # Prétraiter
            success = preprocess_image_file(input_path, output_path, target_size)
            
            if success:
                total_processed += 1
            else:
                total_failed += 1
        
        logger.info(f"[OK] {species} : {len(images) - total_failed} images prétraitées")
    
    # Résumé final
    logger.info("\n=== RESUME DU PRETRAITEMENT ===")
    logger.info(f"Images traitées : {total_processed}")
    logger.info(f"Images échouées : {total_failed}")
    logger.info(f"Total : {total_processed + total_failed}")
    logger.info(f"Taille cible : {target_size}")
    logger.info(f"Format : JPG (quality 85)")
    logger.info(f"Normalisation : [0, 1]")
    logger.info("=== PRETRAITEMENT TERMINE ===")
    
    print(f"\n[DONE] Images finales dans : {output_base_folder}")
    print(f"[LOG] Details dans : {log_file}")


if __name__ == "__main__":
    preprocess_dataset()
