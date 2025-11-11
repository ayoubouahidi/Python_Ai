#remplissage
l =[]
for i in range(2):
    m=[]
    for j in range(2):
        n = int(input("entrer un nombre :"))
        m.append(n)
    l.append(m)


#somme
s = 0
for i in range(2):
    for j in range(2):
        s+=l[i][j]
    
    
    


#affichage
for i in l:
    print(i)
    
print(f"la somme est {s}")
