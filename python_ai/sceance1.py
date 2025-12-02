# j = int(input("enter le jour"))
# m = int(int(input("enter le mois")))
# anne = int (input("enter l anne"))

# def check_if(anne):
#     if (anne % 4 == 0):
#         return True
#     return False

# if (m == 2):
#     if (check_if(anne)):
#         if (j == 28):
#             j = 1
#         elif (j == 27):
#             j = 2
# if (m == 1 or m == 3 or m == 5 or m == 7 or m == 8 or m == 10 or m == 12 ):
#     if (j == 31) :
#         j = 2
#     elif ( j == 30):
#         j = 2
#     j += 2
# else :
#     if (j == 30) :
#         j =  2
#     j += 2
# print(f"j ({j}) m ({m}) anne ({anne}) ")


# n = int(input("entrer :"))
# result = 0
# while(n == 0):
#     result = n % 10
#     n = 
    
# ***********

# res = []
# res.append(1)
# print(res)

# ***********
# **********************    exercice *********************************************************


# def check_parfait(n):
#     i = 1
#     res = []
#     while(i < n):
#         if (n % i == 0):
#             res.append(i)
#         i+=1
#     print("printed tab",res);
#     somme = sum(res);
#     if (somme == n):
#         return True
#     return False


# print("nombre parfait", check_parfait(6))


# ********************** *********************************************************************




# def reverse_recursion(n):
#     res = []
#     while(n > 10):
#         res.append(n % 10)
#         n //= 10
#     res.append(n)
#     i = 0
#     while(i < len(res)):
#         print(res[i], end="")
#         i+=1
# reverse_recursion(12)



# ********************** liste sc 2*********************************************************************
# def calcul_pos(n):
#     res = 0
#     i = 0
#     while ( i < len(n)):
#         if (n[i] >= 0):
#             res+=1
#         i+=1
#     return res


# n  = int(input ( "entrer le nombre des saisie : "))
# # if (n < 0):
# #     break
# i = 0
# res = []
# while (i < n):
#     nombre = int(input ( "entrer un nombre :"))
#     res.append(nombre)
#     i+=1

# # print(f"le nombres positif : {len(}") 

# #nombre negatif {len(res) - res.count(i>0 for i in range(len(res)))}")




# ****************************************** matrice ******************************************  
# i  = int(input ( "entrer le nombre des saisie : "))
# j  = int(input ( "entrer le nombre des saisie : "))

l =[]
for i in range(50):
    m=[]
    for j in range(50):
        n = int(input("entrer un nombre :"))
        m.append(n)
    l.append(m)

   
