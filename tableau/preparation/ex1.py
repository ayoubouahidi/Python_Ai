t = []
n = int(input("entrer la taille du tableau  :"))
for i in range(n):
    x=int(input("entrer un nombre : "))
    t.append(x)
pp = t[0]
p=0
for i in range(n):
    if pp > t[i]:
        pp = t[i]
        p = i
print (t)
print(pp)
print(p+1)