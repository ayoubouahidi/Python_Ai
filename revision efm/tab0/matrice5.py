M =[]
for i in range(3):
    l=[]
    for j in range(3):
        n = int(input("entrerun nombre :"))
        l.append(n)
    M.append(l)
    
for items in M :#affichaged;une matrice
    print(items)
a =0
S=[]
for i in range(3):
    l=[]
    for j in range(3):
        l.append( M[j][i])
    S.append(l)

for items in S:#affichaged;une matrice
    print(items)
