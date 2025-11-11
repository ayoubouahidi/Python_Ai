import random
m=[]
for i in range(4):
    l =[]
    for j in range(4):
        l.append(random.choice([0,1]))
    m.append(l)

for l in m:
    print(l)
