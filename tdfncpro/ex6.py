def suite(n):
    if n == 0 :
        r=13
    else:
        r=4*suite(n-1)+5
    return r 
x = int(input("entrer un nmbre :"))
R=suite(x)
print(R)

