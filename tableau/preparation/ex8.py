n= int(input("entrer la taille du tableau : "))
def remlissage(t,n):
    t=[]
    
    for i in range(n):
        x = int(input("entrer un nombre : "))
        t.append(x)
    return t

def somme(t,l,T):
    T=[]
    for i in range(n):
       T.append(t[i]+l[i])
    return T 



T1=[]
T2=[]
T=[]
T1 = remlissage(T1,n)
T2 =remlissage(T2,n)
T = somme(T1,T2,T)
print(T1)
print(T2)
print(T)

#######################################################

# n = int(input("entrer la taille du tableau : "))

# def remlissage(t, n):
#     t = []

#     for i in range(n):
#         x = int(input("entrer un nombre : "))
#         t.append(x)
#     return t

# def somme(t, l, T):
#     T = []  # Initialize T as an empty list

#     for i in range(n):
#         T.append(t[i] + l[i])  # Append the sum of elements to T
#     return T

# T1 = []
# T2 = []
# T = []

# T1 = remlissage(T1, n)
# T2 = remlissage(T2, n)
# T = somme(T1, T2, T)

# print("T1:", T1)
# print("T2:", T2)
# print("Somme:", T)
