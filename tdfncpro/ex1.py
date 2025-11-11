def verifier(c):

    if c >= "a" and c <="z":
        r = 1
    else:
        r = 0
    return r
ca = input("donner un caractere : ")
resultat = verifier(ca)
print(resultat)
