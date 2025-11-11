#EXPLICATION :DANS  MATRICE (TABLEAU A DEUX DIMENSUIN ) FAIRE UN ALGO ET UN PROGRAMME PYTHON QUI CALCUL LE CENTRE DU (IDOR MN CENTRE ELA CHKEL 7ALAZONI )
import numpy as np

def trouver_centre(matrice):
    lignes, colonnes = matrice.shape

    if lignes % 2 == 1 and colonnes % 2 == 1:
        # Matrice impaire
        centre = (lignes // 2, colonnes // 2)
    else:
        # Matrice paire (choisir le centre à droite ou à gauche)
        centre = (lignes // 2, colonnes // 2)

    return centre

# Exemple d'utilisation
matrice = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9],[1,2,3]])
centre = trouver_centre(matrice)

print(f"Le centre de la matrice est situé à l'indice : {centre}")