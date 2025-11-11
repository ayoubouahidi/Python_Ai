l=[1,2,3,4,5,6,7,8,9]
# methode 1 
# s=int(input("entrer un nombre : "))
# E=0
# for i in range(len(l)):
#     if s == l[i]:
#         E=1
#         print("existe ! ")
#         i=len(l)+1

# if E == 0:
#     print("n'existe pas ")
#methode 2 
nombre=int(input("entrer un nombre :"))
bi = 1
bs = len(l)
trouv = False

while bi<=bs and not trouv:
    (m)= (bi +bs)/2
    
    if nombre == (l[int(m)]):
        trouv = True

    else:
        if (l[int(m)])<nombre:
            bi=m+1
        else:
            bs=m-1

if trouv==True:
    print("exicte ")    
else:
    print("n'exicte pas ")    



