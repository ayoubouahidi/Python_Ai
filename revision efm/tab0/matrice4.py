M =[]
for i in range(3):
    l=[]
    for j in range(3):
        n = int(input("entrerun nombre :"))
        l.append(n)
    M.append(l)
    
for items in M :#affichaged;une matrice
    print(items)

s = 0 
for i in range(3):
    for j in range(3):
        if i == j:
            s = s + M[i][j] 
print("la somme est :",s)