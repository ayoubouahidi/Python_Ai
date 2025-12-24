def puissance(a, b):
    if (b == 1 ):
        return a * b
    return  a * puissance(a, b - 1)

print(puissance(3, 3))

def factorielle(a):
    if (a == 1) :
        return a
    return  a * factorielle(a -1)


print(factorielle(3))

def fibomacci(n):
    if (n < 2):
        return 1
    return fibomacci(n - 1) + fibomacci(n - 2)
print(3)

# def PGCD(a, b)    # a faire !