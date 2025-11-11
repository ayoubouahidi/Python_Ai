#remplissage
def remplissage(m,l,c):
    m=[]
    for i in range(l):
        l=[]
        for j in range(c):
            n=int(input("entrer un nombre : "))
            l.append(n)
        m.append(l)
    return m

#calcul somme total 
def somme(m,l,c):
    s = 0
    for i in range(l):
        for j in range(c):
            s = m[i][j] + s
    return s
#calcul somme des lignes 
def sommeL(m,l,c):
    for i in range(l):
        s = 0
        for j in range(c):
            s = m[i][j] +s
        print(f"la somme du ligne {i+1} est {s}")
    return s
#calcul la somme des colones 
def sommeC(m,l,c):
   
    for j in range(c):
        s = 0 
        for i in range(l):
            print(m[i][j])
            s = m[i][j] + s
        print(f"la somme du colomn {j+1} est {s}")
    return s



#affichage
l = int(input("entrer le nombre des lignes :"))
c = int(input("entrer le nombres des colounes :"))
T=[]
t = remplissage(T,l,c)
s=somme(t,l,c)

L = len(t)
C = len(t[0])
for i in t:
    print(i)
sl = sommeL(t,l,c)
sc = sommeC(t,L,C)

print("la somme total est ",s)



