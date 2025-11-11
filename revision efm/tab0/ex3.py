from random import randint
l= [randint(-10,10) for i in range(20)]
print(l)

pp=l[0]
posp=0

for i in range(20):
    if l[i]<pp:
        pp= l[i]
        posp=i+1

print("le plus petit est : ",pp,"sa position est : ",posp)

pg= max(l)
posg = l.index(pg)

print("le plus grand est : ",pg,"sa position est : ",posg+1)