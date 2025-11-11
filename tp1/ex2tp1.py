cmp = 0
s = 0

while True:
    X = int(input("entrer un nombre positif : "))
    cmp+=1
    s = s + X
    if X < 0:
        break



moy = s/cmp
print("la moyenne est ",moy)

