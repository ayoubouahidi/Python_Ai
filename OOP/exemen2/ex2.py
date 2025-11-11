from collections import Counter,defaultdict

c2 = Counter('infraction digital')
print(c2)  

c3 = Counter([2,2,2,3,45,6,78,8,8,8,9,9,0,0,4,1,6,9])
print(c3)     

c4 = Counter(['full','pop,','info','devlop'])
print(c4) 

# defaultdict Example
d = defaultdict(list)
j = 1
for i in range(1,40):
    if i%3 == 0:
        d[j].append(i)
        j+=1
print(d)


d = defaultdict(int)
j = 1
for i in range(1,40):
    if i%3 == 0:
        d[j].append(i)
        j+=1
print(d)

