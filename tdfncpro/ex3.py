def fact(n):
    re = 1 
    for i in range(2,n+1):
        re = re*i
    return re
x = int(input("enter un nombre :"))
if x >=0 :
    resultat = fact(x)
    print("le resulta est ",resultat)
else:
    print("ce nombre est invalid ")

for i in range(0,101):
    r = fact(i)
    print("la somme des nombrs de 0 a 100 :",r)



