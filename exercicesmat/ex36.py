def Remplissage(L,M):
    for i in range(L):
        T = []
        for j in range(L):
            if j == 0 or i == L-1 or i == j:
                T.append(1)
            else:
                T.append(0)
        M.append(T)
    return M
def Affichage(L,M):
    for i in range(L):
        for j in range(L):
            print(M[i][j],end=" ")
        print()                
M = []
L = int(input('tapez L : '))
M = Remplissage(L,M)
Affichage(L,M)          