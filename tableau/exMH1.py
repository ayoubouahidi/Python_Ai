from random import randint


def remplissage(L,C):
  m = []
  for i in range(L):
     ligne = []

     for j in range(C):
        x= int(input("entrer un element :"))
        ligne.append(x)

     m.append(ligne)

  for item in m:
     print(item)
  return m



# def sommeLIGNE(m):
#    for i in range(l):
#       s = 0
#       for j in range(c) :
#          s = s + m[i][j]

#       print(f"somme du ligne {i+1} est {s}")



# def sommeCOLONE(m):
#    T=[]
#    a= len(m)
#    b= len(m[0])
#    for i in range(b):
#       A = 0
      
#       for j in range(a):
#          A = A + m[i][j]
#       T.append(A)
#       print(f"la somme du colone  est {A}")
#    return A
   

l= int(input("entrer ligne :"))
c = int(input("entrer coloms : "))
T = remplissage(l,c)
for i in T:
   print(i)
# print(remplissage(T))

