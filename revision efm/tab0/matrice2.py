M =[]
for i in range(3):
    l=[]
    for j in range(3):
        n = int(input("entrerun nombre :"))
        l.append(n)
    M.append(l)

for items in M :#affichaged;une matrice
    print(items)
L=[]

for j in range(3):
    s=[]
    for i in range(3):
        s.append(M[i][j])
    L.append(s)

print(L)

