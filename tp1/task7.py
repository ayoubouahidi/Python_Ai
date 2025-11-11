def verifier(n):
    if n % 2 == 0:
        r= 0
    else :
        r = 1
    return r 

cmp=0
for i in range(10):
    x = int(input("donner un nombre : "))
    if verifier(x)== 0:
        cmp +=1
print("le nombre des nombres pair est : ",cmp)
print("le nombre des nombres pair est : ",10-cmp)


    