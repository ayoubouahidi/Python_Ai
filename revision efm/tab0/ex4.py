l=[1,2,3,5,6]

x=int(input("entrer un nombre : "))
p=0

for i in range(len(l)):
    if x > l[i]:
        p=i

l.insert(p+1,x)



for i in range(len(l)):
    print(l[i])

        


