from random import randint
t = [0 for i in range(11)]
print(t)
x = int(input("entrer un nombre :"))
"""insertion au debut """
# t.append(x)
# print(t)
"""insertion a la fin """
#methode 1
# t.insert(0,x)
# print(t)
#methode 2 
# for i in range(10,0,-1):
#     t[i]=t[i-1]
# t[0]=x
# print(t)
'''test'''
# y =(input("donner un y"))
# t.__add__(y)#pour connecter une liste par une autre 
# print(t)
"""insertion a la fin """
p = int(input("donner une position : "))
for i in range(10,p+1,-1):
    t[i]=t[i-1]
t[p-1]=x
print(t)
