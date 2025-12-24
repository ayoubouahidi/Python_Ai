import random
import numpy as np
import math as mt
# ex 01 

tab = [1,2,3,4,5,6,7,8,9]

i = 0
while (i < len(tab)):
    print (tab[i])
    i = i + 1

i = 0

while (i < len(tab)):
    print (tab[i], end="/")
    i = i + 1

print(max(tab), min(tab))
i = 0

count  = 0
while (i < len(tab)):
    if (tab[i] % 3 == 0):
        count = count + 1
    i = i + 1

i = 0
somme = 0
while (i < len(tab)):
    somme = somme + tab[i]
    i = i + 1

i = 0
paires = 0 
while (i < len(tab)):
    if  (tab[i] % 2 == 0):
        paires = paires + 1
    i = i + 1


moyenne = 0
i = 0
while (i < len(tab)):
    moyenne = moyenne + tab[i]
    moyenne = moyenne // len(tab)
    i = i + 1

i = 0
produit = 1
while (i < len(tab)):
    produit = produit * tab[i]
    i = i + 1
print(produit)

produit_2 = 0
for i in range(0 , len(tab)):
    if (tab[i] >= 50 and tab[i] <= 70):
        produit_2 = produit_2  * tab[i]
    i = i + 1


i = len(tab) -1 
while (i != 0):
    print(tab[i])
    i = i - 1


#ex2

# def reverse_tab(tab):
#     i = len(tab) - 1
#     rev_tab = []
#     j = 0
#     while(i != 0):
#         rev_tab.append(tab[i])
#         i = i - 1
#     return rev_tab

# print (reverse_tab(tab))

print(tab[::-1])

#ex 3 

list_3 = [8,3,15,4,1,9,20,7]
list_3.sort()
print(list_3)

list_4 = ["Rabat", "Casablanca" , "Fes", "Berkane", "Taza"]
list_4.sort(reverse=True)
print(list_4)

#ex4 

M = []
for i in range (3):
    m = []
    for i in range(3):
        l = []
        for j in range(3):
            n = random.randint(0,1)
            l.append(n)
        m.append(l)
    M.append(m)

print(M)

# ex 05 

def is_diagonal(mat):
    diagonal =np.diag(np.diag(mat)) 
    return (np.array_equal(mat, diagonal))

# def is_diag_sans_diag(mat )
# def is_diagonal_no(mat):
#     diagonal = np.diag(mat)
#     return (np.array_equal(mat, diagonal))

A = np.array([[1, 0, 0],
              [0, 5, 0],
              [0, 0, 9]])

print(is_diagonal(A))


# ex06
T1 = [i for i in range(0, 51) if i % 2 == 0]
print(T1)

T2 = [mt.cos(x)  ** 2  for x in range(len(T1))]
print (T2)

T3 = [1,2,3,2,1]
if (T3 == T3[::-1]):
    print("sysme")
else :
     print("non sysme")

# ex08 

# M1 = np.array([1,2,3],
#               [3,4,5],
#               [6,7,8])


# M2 = np.array([6,-1,8],
#               [2,1,3],
#               [18,2,32])
# add = M1 + M2
# multi = M1 * M2

# ex 09
# list = [1, 2,3,4,6,7,8,9]
M = []
for i in range (3):
    m = []
    for i in range(3):
        l = []
        for j in range(3):
            n = random.randint(0,1)
            l.append(n)
        m.append(l)
    M.append(m)

print(M)
col_sum = np.sum(M, axis=0)  
row_std = np.std(M, axis=1)  
    
print("\n4. Somme des colonnes et écart-type des lignes:")
print("Somme des colonnes:", col_sum)
print("Écart-type des lignes:", row_std)
    

#  10
paniers = {
        "Client_A": {"Pommes": (2.0, 2.50), "Lait": (3, 1.20)},
        "Client_B": {"Bananes": (1.5, 1.80), "Pain": (2, 0.90)},
        "Client_C": {"Pommes": (5.0, 2.50), "Lait": (1, 1.20), "Pain": (1, 0.90)},
        "Client_D": {"Bananes": (0.5, 1.80)}
    }

clients_actifs = list(paniers.keys())

print(f"{len(clients_actifs)} clients")
tout_les_cout = []
couts_par_client = []
# i = 0
for clients , produit in paniers.items():
    cout_total = 0
    for produit_name, (quantite, prix_unitaire) in produit.items():
            cout_produit = quantite * prix_unitaire
            cout_total += cout_produit
    couts_par_client.append((clients, cout_total))
    tout_les_cout.append(cout_total)
    print(f"le cout total est : {cout_total}")

maximum = max(tout_les_cout)
index = tout_les_cout.index(maximum)
client_name = couts_par_client[index][0]
print(client_name, couts_par_client[index][1])

moyenne = 0
nbr = 0
for clients, (produit_name, (quantite, prix_unitaire)) in paniers.items():
    if (produit_name == "Lait"):
        moyenne += prix_unitaire
        





