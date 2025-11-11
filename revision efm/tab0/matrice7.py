from random import randint

m=[]

for i in range(3):
    l=[randint(0,10) for i in range(4)]
    m.append(l)

for items in m :
    print(items)
print("----------")

n = int(input("entrer un nombre :"))
trouv = False
print("----------")
for i in range(3):
    for j in range(4):
        if n == m[i][j]:
            trouv = True

if not trouv:
    print("n'existe pas ")
else:
    print("existe")


    