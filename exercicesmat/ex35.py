from random import randint
def Remplir(L,C,M):
    for i in range(L):
        L=[]
        for j in range(C):
            L.append(randint(1,9))
        M.append(L)
    #M = [[randint(1,100) for j in range(C)] for i in range(L)] == The previous 5 lines
    print(M)

def Sommeligne(M):
    k = 1
    for L in M:
        som = 0
        for i in L:
            som += i
        print(f'la somme de ligne {k} : {som}')
        k += 1
        
def Sommecologne(M):
    k = 1
    for L in M:
        for i in L:
            som = 0
            for j in L:
                som += i
            print(f'la somme de cologne {k} : {som}')
            k += 1
M = []
L = int(input('tapez L : '))
C = int(input('tapez C : '))
Remplir(L,C,M)
Sommeligne(M)
Sommecologne(M)