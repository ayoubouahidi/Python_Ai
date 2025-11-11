t=[]
x = int(input("donner  un  nombre : "))
while x!=0:
    t.append(x)
    x = int(input("entrer un nombre : "))
cmp = 0 
for i in range(len[t]):
    if t[i]>0:
        cmp+=1
print(cmp)
for i in range(len[t]):
    if t[i]<0:
        t[i]=0
print(t)
