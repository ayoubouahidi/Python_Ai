def remplissage(m,l,c):
    
    for i in range(l):
        A=[]
        for i in range(c):
            n=int(input("entrer un nombre :"))
            A.append(n)
        m.append(A)
    return m

def sommeC(m,l,c):
    m=[]
    print(remplissage(m,l,c))
    for i in range(l):
        
        for j in range(c):
            s = 0 
            s+=m[i][j]
        

        




