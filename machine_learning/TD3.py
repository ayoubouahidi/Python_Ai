import numpy as np

# Profils des étudiants
A = np.array([85, 90, 12])
B = np.array([80, 85, 10])

# 1. Normes
norm_A = np.linalg.norm(A)
norm_B = np.linalg.norm(B)

# 2. Produit scalaire
dot_AB = np.dot(A, B)

# 3. Similarité cosinus
cosine_similarity = dot_AB / (norm_A * norm_B)

# Affichage des résultats
print("Norme de A :", norm_A)
print("Norme de B :", norm_B)
print("Produit scalaire A·B :", dot_AB)
print("Similarité cosinus :", cosine_similarity)


#  exercice 2 
X = np.array([[1, 2], [3, 4], [5, 6]])
W = np.array([[0.5], [1.2]])

Y = np.dot(X, W)

print("Prédictions Y :\n", Y)

#  exercice 3 

A = np.array([[2, 4],
              [1, 3]])

ATA = np.dot(A.T, A)

print("A^T A =\n", ATA)

# interpretation 
# est une matrice de Gram, qui contient les produits scalaires entre les colonnes de A 
# Les éléments hors diagonale (11) représentent le produit scalaire entre les deux colonnes, donc la mesure de leur corrélation
# 

#  exercice 4 

A = np.array([[4, 7],
              [2, 6]])

det_A = np.linalg.det(A)
inv_A = np.linalg.inv(A)

print("Déterminant de A :", det_A)
print("Inverse de A :\n", inv_A)

#  exerice 5 

X = np.array([[1, 1],
              [1, 2],
              [1, 3]])
Y = np.array([[2],
              [2.5],
              [3.5]])

W = np.linalg.inv(X.T @ X) @ (X.T @ Y)

print("Coefficients W :\n", W)

#  exercice 6 

import numpy as np

A = np.array([[2, 1],
              [1, 2]])

eigvals, eigvecs = np.linalg.eig(A)

print("Valeurs propres :", eigvals)
print("Vecteurs propres :\n", eigvecs)

# 9awdnaha
