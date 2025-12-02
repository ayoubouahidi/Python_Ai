import cv2
import matplotlib.pyplot as plt
import numpy as np

# # Charger une image en niveaux de gris
# # Le paramètre 0 force la lecture en mode "grayscale"
image = cv2.imread("test.jpg", 0)

# Afficher la matrice des pixels (valeurs entre 0 et 255)
print("Matrice des pixels :")
print(image)

# Afficher l'image en niveaux de gris
plt.imshow(image, cmap='gray')
plt.title("Image en niveaux de gris")
plt.axis("off")
plt.show()

# Exemple : créer une petite image 4x4 en niveaux de gris
matrice = np.array([
    [255, 64, 128, 255],
    [255, 128, 64, 0],
    [50, 100, 150, 200],
    [200, 150, 100, 50]
], dtype=np.uint8)

plt.imshow(matrice, cmap='gray')
plt.title("Exemple matrice 4x4")
plt.axis("off")
plt.show()