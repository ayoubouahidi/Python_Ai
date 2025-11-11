def div(x):
    cmp = 1 
    for i in range(1,x):
        if x%i==0:
            cmp+=1
    return cmp

def pre(n):
    if div(n) == 2:
        r = True
    else:
        r=False
    return r
cmp = 0
for i in range(0,100000):
    
    if pre(i) == True :
        print(i,end=" ")
# print("le nombre des nombres premier :",cmp)
    

# a = int (input("enter le premier nombre :"))

# R= pre(a)
# print(R)