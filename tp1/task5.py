def puissance(x,y):
    re = 1
    for i in range(y):
         re*= x
    return re
n1 = int(input("entrer un nombre : "))
n2 = int(input("entre un nombre : "))

r = puissance(n1,n2)
print("resultat est: ",r)


