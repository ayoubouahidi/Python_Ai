#  ex 1
import random

def trier_colonnes(matrice):
    nb_lignes = len(matrice)
    nb_colonnes = len(matrice[0])
    resultat = [ligne[:] for ligne in matrice]
    for j in range(nb_colonnes):
        colonne = [matrice[i][j] for i in range(nb_lignes)]
        colonne.sort(reverse=True)
        for i in range(nb_lignes):
            resultat[i][j] = colonne[i]
    return resultat


m = 5  
matrix = [[0 for _ in range(m)] for _ in range(m)]

for i in range(m):
    for j in range(m):
        matrix[i][j] = random.randint(0, 20)

print("Matrix before sorting:")
for i in range(m):
    for j in range(m):
        print(matrix[i][j], end=" ")
    print()  

print("********* trie decroisant *********")
sorted_matrix = trier_colonnes(matrix)

for i in range(m):
    for j in range(m):
        print(sorted_matrix[i][j], end=" ")
    print()  

# ex 02 

def printRLE(st):
    n = len(st)
    i = 0
    while (i < n):
        count = 1
        while (i < n - 1 and st[i] == st[i + 1]):
            count += 1
            i += 1
        print(st[i] + str(count), end = "")
        i += 1
    print()

printRLE("aaabbc")

def rev_printRLE(str):
    n = len(str)
    i = 0
    while(i < n):
        if(str[i].isnumeric()):
            rep = int(str[i])
            j = 0
            while(j < rep):
                print(str[i + 1], end="")
                j+=1
        i+=1

rev_printRLE("a2b1c")



def est_trie_croissant_strict(liste):

    """
    Vérifie récursivement si une liste est triée en ordre strictement croissant.
    Condition: X[i] < X[i+1] pour tout i
    """

    if len(liste) <= 1:
        return True
    if liste[0] >= liste[1]:
        return False
    return est_trie_croissant_strict(liste[1:])




