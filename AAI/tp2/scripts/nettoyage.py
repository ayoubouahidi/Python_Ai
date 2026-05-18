"""
NETTOYAGE DU DATASET D'IMAGES
==============================
Ce script nettoie les images téléchargées en supprimant :
- Les doublons (imagehash)
- Les images trop petites (< 200px)
- Les images corrompues
- Les images avec filigranes (bonus)
"""

import os
import logging
from PIL import Image
import imagehash
from pathlib import Path
import matplotlib.pyplot as plt
import numpy as np
from datetime import datetime
import cv2

# Configuration du logging
log_dir = "../data/logs"
os.makedirs(log_dir, exist_ok=True)
log_file = os.path.join(log_dir, f"nettoyage_{datetime.now().strftime('%Y%m%d_%H%M%S')}.log")

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
# ETAPE 1 : SUPPRESSION DES DOUBLONS
# ============================================================
def find_and_remove_duplicates(folder_path):
    """
    Détecte et supprime les images en double en utilisant imagehash.
    imagehash crée une signature unique pour chaque image.
    Si deux images ont la même signature = elles sont identiques ou très similaires.
    """
    logger.info(f"[ETAPE 1] Suppression des doublons dans : {folder_path}")
    
    if not os.path.exists(folder_path):
        logger.warning(f"Dossier inexistant : {folder_path}")
        return 0
    
    image_hashes = {}  # dictionnaire : hash -> chemin_fichier
    duplicates = []
    
    for filename in os.listdir(folder_path):
        if not filename.lower().endswith(('.jpg', '.jpeg', '.png')):
            continue
        
        filepath = os.path.join(folder_path, filename)
        
        try:
            # Créer une signature (hash) de l'image
            image = Image.open(filepath)
            img_hash = imagehash.average_hash(image)
            
            # Si ce hash existe déjà = c'est un doublon
            if img_hash in image_hashes:
                duplicates.append(filepath)
                logger.info(f"[DOUBLON] {filename}")
            else:
                image_hashes[img_hash] = filepath
        except Exception as e:
            logger.error(f"Erreur hash {filename}: {e}")
    
    # Supprimer les doublons
    for dup_file in duplicates:
        try:
            os.remove(dup_file)
            logger.info(f"[SUPPRIME] Doublon : {os.path.basename(dup_file)}")
        except Exception as e:
            logger.error(f"Erreur suppression {dup_file}: {e}")
    
    logger.info(f"[RESULTAT] {len(duplicates)} doublons supprimés")
    return len(duplicates)


# ============================================================
# ETAPE 2 : FILTRAGE PAR TAILLE
# ============================================================
def filter_by_size(folder_path, min_width=200, min_height=200):
    """
    Supprime les images dont la largeur OU la hauteur < 200 pixels.
    (Les petites images n'ont pas assez de détails pour l'apprentissage)
    """
    logger.info(f"[ETAPE 2] Filtrage par taille (min {min_width}x{min_height}) : {folder_path}")
    
    removed = 0
    
    for filename in os.listdir(folder_path):
        if not filename.lower().endswith(('.jpg', '.jpeg', '.png')):
            continue
        
        filepath = os.path.join(folder_path, filename)
        
        try:
            image = Image.open(filepath)
            width, height = image.size
            
            # Si une dimension < minimum requis = supprimer
            if width < min_width or height < min_height:
                os.remove(filepath)
                logger.info(f"[TROP PETITE] {filename} ({width}x{height})")
                removed += 1
        except Exception as e:
            logger.error(f"Erreur taille {filename}: {e}")
    
    logger.info(f"[RESULTAT] {removed} images trop petites supprimées")
    return removed


# ============================================================
# ETAPE 3 : DETECTION D'IMAGES CORROMPUES
# ============================================================
def check_corrupted_images(folder_path):
    """
    Vérifie que chaque image peut être ouverte correctement.
    Si elle ne s'ouvre pas = elle est corrompue = supprimer.
    """
    logger.info(f"[ETAPE 3] Detection des images corrompues : {folder_path}")
    
    removed = 0
    
    for filename in os.listdir(folder_path):
        if not filename.lower().endswith(('.jpg', '.jpeg', '.png')):
            continue
        
        filepath = os.path.join(folder_path, filename)
        
        try:
            # Essayer d'ouvrir l'image
            image = Image.open(filepath)
            image.verify()  # Vérification supplémentaire
        except Exception as e:
            # Si ça échoue = corrompue
            logger.warning(f"[CORROMPUE] {filename} : {str(e)[:40]}")
            try:
                os.remove(filepath)
                logger.info(f"[SUPPRIMEE] Image corrompue : {filename}")
                removed += 1
            except Exception as delete_error:
                logger.error(f"Erreur suppression {filename}: {delete_error}")
    
    logger.info(f"[RESULTAT] {removed} images corrompues supprimées")
    return removed


# ============================================================
# ETAPE 4 : DETECTION D'IMAGES AVEC FILIGRANES (BONUS)
# ============================================================
def detect_watermark(image_path, threshold=30):
    """
    Détecte si une image a un filigrane/texte en analysant :
    - Les contours nets (bordures du texte/filigrane)
    - Les zones à forte variation de couleur
    
    threshold : plus élevé = plus sensible
    """
    try:
        # Charger l'image en niveaux de gris
        img_cv = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
        if img_cv is None:
            return False
        
        # Calcul du gradient (detection des contours)
        sobelx = cv2.Sobel(img_cv, cv2.CV_64F, 1, 0, ksize=3)
        sobely = cv2.Sobel(img_cv, cv2.CV_64F, 0, 1, ksize=3)
        magnitude = np.sqrt(sobelx**2 + sobely**2)
        
        # Si beaucoup de contours nets = probablement un filigrane
        percent_edges = (np.count_nonzero(magnitude > threshold) / magnitude.size) * 100
        
        return percent_edges > 5  # Si > 5% de contours nets
    except Exception as e:
        logger.error(f"Erreur detection filigrane {image_path}: {e}")
        return False


def remove_watermarked_images(folder_path, threshold=30):
    """
    Cherche et supprime les images avec filigranes.
    """
    logger.info(f"[ETAPE 4] Detection des filigranes : {folder_path}")
    
    removed = 0
    
    for filename in os.listdir(folder_path):
        if not filename.lower().endswith(('.jpg', '.jpeg', '.png')):
            continue
        
        filepath = os.path.join(folder_path, filename)
        
        if detect_watermark(filepath, threshold):
            try:
                os.remove(filepath)
                logger.info(f"[FILIGRANE] {filename} supprimée")
                removed += 1
            except Exception as e:
                logger.error(f"Erreur suppression {filename}: {e}")
    
    logger.info(f"[RESULTAT] {removed} images avec filigranes supprimées")
    return removed


# ============================================================
# ETAPE 5 : VERIFICATION MANUELLE ASSISTEE
# ============================================================
def manual_verification_sample(base_folder, samples_per_class=10):
    """
    Affiche 10 images aléatoires par espèce avec matplotlib.
    Tu peux vérifier manuellement si elles sont bien classées.
    """
    logger.info(f"[ETAPE 5] Verification manuelle assistee")
    
    # Lister tous les dossiers (espèces)
    species_folders = [f for f in os.listdir(base_folder) 
                       if os.path.isdir(os.path.join(base_folder, f))]
    
    for species in species_folders:
        species_path = os.path.join(base_folder, species)
        images = [f for f in os.listdir(species_path) 
                  if f.lower().endswith(('.jpg', '.jpeg', '.png'))]
        
        if len(images) == 0:
            continue
        
        # Sélectionner jusqu'à 10 images aléatoires
        sample_images = np.random.choice(images, 
                                        min(samples_per_class, len(images)), 
                                        replace=False)
        
        # Afficher les images
        fig, axes = plt.subplots(2, 5, figsize=(15, 6))
        fig.suptitle(f'Verification : {species}', fontsize=16)
        axes = axes.flatten()
        
        for idx, img_file in enumerate(sample_images):
            if idx >= 10:
                break
            
            img_path = os.path.join(species_path, img_file)
            try:
                img = Image.open(img_path)
                axes[idx].imshow(img)
                axes[idx].set_title(img_file[:15], fontsize=8)
                axes[idx].axis('off')
            except Exception as e:
                logger.error(f"Erreur affichage {img_file}: {e}")
        
        plt.tight_layout()
        plt.savefig(os.path.join("../data", f"verification_{species}.png"), dpi=100)
        plt.show()
        
        logger.info(f"[OK] Verification {species} affichee")


# ============================================================
# FONCTION PRINCIPALE
# ============================================================
def clean_dataset(base_folder="../data/brutes"):
    """
    Lance le nettoyage complet du dataset.
    """
    logger.info("=== DEBUT DU NETTOYAGE ===")
    
    # Vérifier que le dossier existe
    if not os.path.exists(base_folder):
        logger.error(f"Dossier introuvable : {base_folder}")
        return
    
    # Parcourir chaque espèce (dossier)
    species_folders = [f for f in os.listdir(base_folder) 
                       if os.path.isdir(os.path.join(base_folder, f))]
    
    total_removed = {"duplicates": 0, "small": 0, "corrupted": 0, "watermark": 0}
    
    for species in species_folders:
        species_path = os.path.join(base_folder, species)
        logger.info(f"\n--- Traitement : {species} ---")
        
        # ETAPE 1
        total_removed["duplicates"] += find_and_remove_duplicates(species_path)
        
        # ETAPE 2
        total_removed["small"] += filter_by_size(species_path)
        
        # ETAPE 3
        total_removed["corrupted"] += check_corrupted_images(species_path)
        
        # ETAPE 4 (optionnel, plus lent)
        # total_removed["watermark"] += remove_watermarked_images(species_path)
    
    # ETAPE 5
    logger.info("\n--- Verification manuelle ---")
    manual_verification_sample(base_folder, samples_per_class=10)
    
    # Resume final
    logger.info("\n=== RESUME DU NETTOYAGE ===")
    logger.info(f"Doublons supprimes : {total_removed['duplicates']}")
    logger.info(f"Images trop petites : {total_removed['small']}")
    logger.info(f"Images corrompues : {total_removed['corrupted']}")
    logger.info(f"Images avec filigranes : {total_removed['watermark']}")
    logger.info(f"TOTAL SUPPRIMEES : {sum(total_removed.values())}")
    logger.info("=== NETTOYAGE TERMINE ===")
    
    print(f"\n[DONE] Logs dans : {log_file}")


if __name__ == "__main__":
    clean_dataset()
