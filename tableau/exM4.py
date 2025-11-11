# n = 3

# for x in range(n):
#     for y in range(x+1):
#         print('1', end='')
#     for y in range(x+1,n):
#         print("0", end='')
#     print()
def remplissage(m,l,c):
    
    for i in range(l):
        A=[]
        for j in range(c):
            n=int(input("entrer un nombre :"))
            A.append(n)
            
        m.append(A)
        
    return m

def test(m,l,c):
    for i in range(l):
        for j in range(c):
            print(m[i][j],end=" ")
        print()
    return m

def calcul(m,L):
    for i in range(L):
        L1=[]
        for j in range(L):
            if (j == 0 or i ==L -i or i == j ):
                L1.append(1)
            else:
                L1.append(0)
        m.append(L1)
        return m
                          


m=[]
print(remplissage(m,2,2))
print(test(m,2,2))
# print(calcul(m,2))
# print(calcule())
# print(m,)

