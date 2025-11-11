import math
n = int(input("entrer un nombre :"))
s=0
for i in range(1,n+1):
    if i-1+math.sqrt(i):
     s = s + math.sqrt(i - 1 + math.sqrt(i))
    



print(s)