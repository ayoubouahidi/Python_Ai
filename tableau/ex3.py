from random import randint
# T=[]
# for i in range (10):
#    x = random.randint(0,10)
#    T.append(x)
# print(T)
# print(max(T))
# print(min(T))
t = [randint(-100,100) for i in range(100)]

pp = t[0]
pg = t[0]
pop = 0
pog = 0 
cmp = 0 
x = int(input("donner un nombre "))
for i in range(100):
    if pp > t[i]:
        pp =t[i]
        pop = i
    else:
        if x==t[i]:
            cmp+=1
print(t)
print("le plus petit est ",pp,"sa position est ",pop)
for i in range(100):
    if pg <t[i]:
        pg = t[i]
        pog = i
    else:
        if x==t[i]:
            cmp+=1
print("le plus grand est ",pg,"sa position est ",pog)
print(x,"repeter",cmp,"fois")

