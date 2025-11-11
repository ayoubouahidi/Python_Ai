L = []
cmp=0
n = int(input("entrer la taille : "))
a = int(input("entrer le nombre que vous voulez :"))
for i in range(n):
    x = int(input("entrer un nombre "))
    L.append(x)



for i in range(n):
    if a == L[i]:
        cmp+=1
print(f"le nombre {a} est repeter {cmp}")

    