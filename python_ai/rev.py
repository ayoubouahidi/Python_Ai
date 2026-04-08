import numpy as np
import random as rd
import math as mt
import matplotlib.pyplot as plt

# A = {1,10,5,3,4,5, "ouahidi"}
# B = {17, 17, 16 , 5, 15}


# L = [1,5,2,5,1,5,6,8]
# # print(L[])
# fruits = ["pomme", "banane", "orange", "kiwi", "mangue", "fraise"]
# print(fruits[:])
# # t = (19, 17 , 15 , 13)
# # print(t)

# suite = [5*i for i in range(2,8)]
# print(suite)

# creer une matrice 
# m = []
# for i in range(3):
#     l = []
#     for j in range(3):
#         l.append(i + j)
#     m.append(l)


# for i in range(len(m)):
#     for j in range(len(l)):
#         print(j, end=" ")
#     print()
# print(m)

# A = float(input("entrer un nombre :"))

# n = int(input("entrer un nombre : "))
# i = 2

# if (n <= 1):
#     print("n'est pas premier ")

# est_premier = True  
# while (i < n):
#     if (n % i == 0):
#         print(f"{n} n'est pas premier ")
#         est_premier = False
#         break
#     i = i + 1

# if(est_premier == True):
#     print(f"{n} est premier")


# def check_si_premier(n):
#     est_premier = True
#     if (n <= 1):
#         est_premier = False
#     i = 2
    
#     while (i < n):
#         if (n % i == 0):
#             # print(f"{n} n'est pas premier ")
#             est_premier = False
#             return False
#         i = i + 1
#     if(est_premier == True):
#         return True

# for i in range(0, 101):
#     if (check_si_premier(i) == True):
#         print(i, end=" ")


# n = int(input("entrer un nombre : "))
# if (n % 400 == 0 or (n % 4 == 0 and n % 100 != 0)):
#     print("anne bisxtille")
# else:
#     print("n'est pas bisxtille ")


# tab = [1,4,2,5,7,8]
# new_tab = []
# i = len(tab) - 1
# j = 0
# while (i >= 0):
#     new_tab.append(tab[i])
#     i = i - 1
#     # j = j + 1
# # print(new_tab)
# tab.sort(reverse=True)
# print(sorted(tab))

# arr = np.linspace(3, 9)
# print(arr[0])

# creer une matrice 
# m = []
# for i in range(3):
#     l = []
#     for j in range(3):
#         l.append(rd.randint(0,10))
#     m.append(l)

# matrix = np.array([[1, 0, 0], [0, 6, 0],[0, 0, 1]])
# # print(matrix.shape)

# # new = np.diag(np.diag(m))


# # print("matrice est  diag  :", np.array_equal(m, new))

# # else:
# #     print("matrice n'est pas diag")

# # for i in range(len(m)):
# #     for j in range(len(l)):
# #         if (i == j and l[i][j] == 1):
# def est_diag(m):
#     for i in range(len(m)):
#         for j in range(len(m[i])):
#             if (i != j and m[i][j] != 0):
#                 return False
#     return True

# print("matrice est diag : ", est_diag(matrix))

# t1 = [i for i in range(0, 51, 2)]
# print(t1)
# t2 = np.cos(t1) ** 2
# print(t2)
# print(t2.min())
# print(np.sum(t2 == t2.max()))

# l = [1,3,5,3,1]
# # def est_sym(l):
# #     if (l == l[::-1]):
# #         return True
# #     return False
# print(l[::-1])

# matrix1 = np.array([[1,2,3],[4,5,6],[7,8,9]])
# matrix2 = np.array([[1,2,3],[4,5,6],[7,8,9]])
# p = matrix1 @ matrix2
# print(matrix1[:, 1])


# paniers = { "Client_A": { "Pommes": (2.0, 2.50), "Lait":(3, 1.20)},
#         "Client_B": {"Bananes": (1.5, 1.80), "Pain": (2,0.90)},
#         "Client_C": {"Pommes": (5.0, 2.50), "Lait": (1, 1.20), "Pain":(1, 0.90)},
#         "Client_D": {"Bananes": (0.5, 1.80)}
# }

# # noms = list(paniers.keys())
# # print(noms)

# total = {}

# for clients, produits in paniers.items():
#     totals = sum( qte * prix for qte , prix in produits.values())
#     total[clients] = totals
#     print(f"{clients} : {total[clients]}")

# maxi = max(total, key = total.get)
# print(maxi)

# totale = sum(produits["Lait"][1] for produits in paniers.values() if "Lait" in produits)
# counte = sum(1 for produits in paniers.values() if "Lait" in produits)
# moy = totale / counte
# print(moy)  


# clients_min = min(total, key=total.get)
# del paniers[clients_min]
# print (paniers)

# def rec_puissance (a , b):
#     if (b <= 1):
#         return a
#     return a * rec_puissance(a , b - 1)

# print(rec_puissance(3,2))

# def rec_fact(a):
#     if (a <= 1):
#         return a
#     return a * rec_fact(a - 1)
# print(rec_fact(5))

# def rec_fibo(a):
#     if (a < 2):
#         return 1
#     return rec_fibo(a - 1) + rec_fibo(a - 2)
# print(rec_fibo(5))


# D = {'nom': 'Dupuis', 'prenom': 'Jacque', 'age': 30}
# D['prenom'] = "JACK"
# print(D.keys())
# print(D.values())

# Ventes = {"Dupont":14, "Hervy":19, "Geoffroy":15, "Layec":21} 

# def dict_manipulation(dict):
#     return (sum(dict.values()))
# def dict_max(dict):
#     return max(dict , key=dict.get)

# print(dict_max(Ventes))

# x = np.linspace(-4, 4)
# y = np.cos(x) + 3 * np.sin(2 * x)

# plt.plot(x , y)
# plt.xlabel("X")
# plt.ylabel("Y")
# plt.grid(True)
# plt.show()


# def palindrome(word):
#     i = 0
#     word = word.lower()
#     # print(word)
#     if (word[i] == ' ' or  word[i] == ',' or word[i] == )

# print(palindrome("kayak"))
# word = "AYOUB"
# word = word.lower()
# print(word)