"""
#list
listA = ["ayoub","ouahidi","age21ans"]
listA[2] = "liiste"
print(listA)
#tuple
listB = ("ayoub","ouahidi","age21ans")
X = list(listB)
X[2] = "tuple"
listB = tuple(X)
print(listB)
#tuple add
listC = ("ayoub","ouahidi","toknow")
Y = list(listC)
Y.append("age21ans")
listC = tuple(Y)
print(listC)
tuple = ("ayoub","ouahidi","age21ans")
print (max(tuple))

for x in range(6):
    if x == 3: break
    print(x)
else:
    print('maghadich itktab')

adj = ["ayoub","ouahidi","age21ans"]
lol = ["ahmed","omar","khalid"]
for x in lol:
    for y in adj:
        print(x,y)

#triangle 
n = 5
symbole =  input('entrer le sybole que veur couler : ')
for x in range(n):
    for y in range(n):
        print(symbole,end=' ')
    print()    
         
#triangle
n = 5
symbole = input("entrer le symbole que veurt vouler : ")

for x in range(n):
    for y in range(x + 1):
        print(symbole, end=' ')
    print()
         
#triangle 3
n = 5
symbole = input('entrer votre symbole : ')

for x in range(n):
    for y in range(x,n):
        print(symbole, end=' ')
    print()
        
n = 5
symbole = input('entrer votre symbole : ')
for x in range(n):
    for y in range(x,n):
        print(' ', end='')
    for y in range(x+1):
        print(symbole, end='')
    print()
     
#triangle 4
n = 5
symbole = input('entrer un nombre : ')
for x in range(n):
    for y in range(x+1):
        print(' ', end='')
    for y in range(x,n):
        print(symbole, end='')
    print()
        
n = 5 
symbole = input('entrer un symbole : ')
for x in range(n):
    for y in range(x,n):
        print(" ", end=' ')
    for y in range(x):
        print(symbole, end=' ')
    for y in range(x+1):
        print(symbole, end=' ')
    print()
    """
# n = 5
# symbole = input('entrer votre symbole : ')
# for x in range(n):
#     for y in range(x+1):
#         print(" ",end=' ')
#     for y in range(x,n):
#         print(symbole, end=' ')
#     for y in range(x,n-1):
#         print(symbole,end=' ')
#     print()
# ********************
t=[1,2,3,4,5,6]
# for i ,element in enumerate(t):
#      print(i,element)

""""#test list"""
# ayoub =['ayoub','ouahidi','21ans']
#print(help(ayoub))   # for help
#print(len(ayoub))    # how many elements 
#ayoub.sort()   #List objects have a sort() method that will sort the list alphanumerically( A to Z in 1 to 9  )
#ayoub.reverse()
#ayoub.index('ayoub')



#*************************************LISTE -POO-***********************************
""""supprimer"""
# cetteListe= ["apple", "banana", "cherry"]
# del(cetteListe[1]) #supprimer l’élément se trouvant à la première position
# print(cetteListe) # affiche ["banana", "cherry"]

""""permet de fusioner une liste """
# istA = ["a", "b" , "c"]
# listB = [1, 8, 9]
# istA.extend(listB) #fusionner le deux Listes Liste1 et Liste2
# print(istA)
""""copy"""
# liste1 =["AYOUB","OUAHIDI","21ANS"]
# liste2= liste1.copy()
# print(liste2)

""""clear"""
# liste2.clear()
# print(liste2)
""""reverse"""
# liste1.reverse()
# print(liste1)

"""namedtuple"""

# from collections import *
# from time import *
# # Basic example
# Point = namedtuple('Point', ['x','y'])
# p = Point(11, 22)     # instantiate with positional or keyword arguments
# print(p)
# p[0] + p[1]             # indexable like the plain tuple (11, 22)
# 33
# x, y = p                # unpack like a regular tuple

# print(x, y)

#PREMIERE METHODE #CONSTRUIT UNE NOUVELLE INSTANCE A PARTIR D'UNE SEQUANCE ITERABLE 
# t = [11, 22]
# Point._make(t)
# print(Point._make(t)) #travail seulment dans 'print'

#DEUXIEME METHODE #RENVOI CHAQUE NOM AVEC SA CHAMP(dictionaire)
# print(p._asdict())


#TROISIEME METHODE #renvoie une nouvelle instance  remplaçant les champs specifies par une nouvelle valeur 

# Point(x=11, y=22)
# p._replace(x=33)
# Point(x=33, y=22)

#quatriemme methode #listant les noms du champs

# print(p._fields)
# color = namedtuple("color",'red blue yellow ')
# pixel = namedtuple('pixel',color._fields+Point._fields)
# print(pixel(11,22,33,44,55))




# n= 5
# symbole = input('entrer votre symbole : ')
# for x in range(n):
#     for y in range(x,n):
#         print(' ', end='')
#     for y in range(x+1):
#         print(symbole, end='')
#     print()

array = [1,2,4,5,6]
array[2]="ayoub"
print(array)






