from random import randint

T=[randint(0,10) for i in range(20)]
print(T)
n = int(input("entrer un nombre :"))

cmp=0

for i in range(20):
    if T[i]==n:
        cmp+=1
print("le nombre d'ocurence est :",cmp)
