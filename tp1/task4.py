def somme(x,y):
    r = x + y
    return  r
"""
#1
n1 = int(input("entrer un nombre : "))
n2 = int(input("entrer un nombre : "))

print("la somme est : ",somme(n1))

#2
n1 = int(input("entrer un nombre : "))
n2 = int(input("entrer un nombre : "))
n3 = int(input("entrer un nombre : "))
n4 = int(input("entrer un nombre : "))

A = somme(n1,n2)
B= somme(n3,n4)
R = somme(A,B)
print("la somme est : ",R)
"""
#3
L = 0

for i in range(100):
    L = somme(L,i)
print("la somme est : ",L)


