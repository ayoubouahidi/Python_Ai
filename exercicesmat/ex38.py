from random import uniform
M = [[round(uniform(0,20),2) for j in range(25)] for i in range(9)]
for i in range(9):
    print('[',end=' ')
    for j in range(25):
        print(M[i][j],end=' ')
    print(']\n',end=' ')
MAX = []

k = 1
for L in M:
    max = 0
    indice = 0
    for stagiaire in range(len(L)):
        if L[stagiaire] > max:
            max = L[stagiaire]
            indice = stagiaire
            
    print(f'le majorant dans la classe {k} est le stagiaire {indice} avec une note de {max}')
    k += 1
max = 0
indice = 0
for L in M:
    for stagiaire in range(len(L)):
        if L[stagiaire] > max:
            max = L[stagiaire]
            indice = stagiaire
            classe = M.index(L)+1
print(f'le majorant dans la classe {classe} est le stagiaire {indice} avec une note de {max}')
admis_total = 0
for L in M:
    for stagiaire in L:
        if stagiaire >= 10:
            admis_total += 1
print(f'le total des admis : {admis_total}')