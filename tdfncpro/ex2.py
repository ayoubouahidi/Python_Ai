
def verifier(c):

    if c >= "a" and c <="z":
        r = 1
    else:
        r = 0
    return r
def inverse(x):
  
    y = verifier(x)
    if y == 1:
        re = chr(ord(x) - 32) 
    else:
        re = chr(ord(x) + 32)
    return re 

def transchaine(z):
    reponse=""
    for i in z:
        if ord(i)>=65 and ord(i) <= 90:
            i = chr(ord(i) - 32)
            reponse = reponse + i
        else:
            reponse = reponse + i
    return reponse
A= input("entrer une chaine de caractere : ")
print(transchaine(A))
