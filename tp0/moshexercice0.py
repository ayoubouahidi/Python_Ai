"""
#ex0
cmp = 0
s = 0
while True:
    n = int(input("ntrer un nombre : "))
    cmp += 1
    s = s + n
    if cmp == 10:
        break
moy = s/10
print("votre moyenne  est du nombre",s,"est du moyenne", moy)

#ex1
N1 = int(input("donner un nombre : "))
N2  = int(input("donner un autre nombre : "))

if N1 < N2:
    c = N1
    N1 = N2
    N2 = c
print("le plus grand nombre est : ", N1)
print("le plus petit nombre est : ",N2)

#EX2
a = int(input("entrer un  nombre : "))
b = int(input("entrer un  nombre : "))

if a != 0:
    x = -b/a
    print("la solturion est ",x)
else:
    if b == 0:
        print("la soluruin est R ")
    else:
        print("n'est pas de solution ")
        """
#EX3 
c = input("entrer le symbole du groupe : ")

match c :
    case "a": print("ce groupe est A ")
    case "b": print("ce groupe est B ")
    case "c": print("ce groupe est C")
    case _:   print("ce groupe n'est existe pas  ")