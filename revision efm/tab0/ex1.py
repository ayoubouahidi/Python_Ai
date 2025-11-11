from random import randint

T=[randint(-10,10) for i in range(10)]
print(T)

T1=[]
T2=[]
 
for i in range(10):

    if T[i]>=0:
        T1.append(T[i])
        

    else:
        T2.append(T[i])
        

print(T1)
print(T2)

