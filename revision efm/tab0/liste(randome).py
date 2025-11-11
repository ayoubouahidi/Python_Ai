from random import randint
# methode 1 (remplissage du tb )
# l=[0,0,0]
# for i in range(3):
#     l[i]=int(input("entrer un nombre :"))

# print(l)
""""""
# methode 2
# l = []
# for i in range(3):
#     l.append(int(input("entrer un nombre :")))
# print(l)
""""""
# test du fct randome 

l=[randint(-100,100) for i in range(10)]
# l=[randint(0,10) for i in range(10)]


print(l)