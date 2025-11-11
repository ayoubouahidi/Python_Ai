cp = 0 
cn = 0 
cz = 0 
for i in range(10):
    n = int(input("donner un nombre : "))
    if n > 0:
        cp+=1
    else:
        if n < 0:
            cn +=1
        else:
            cz +=1
print(f"on a {cp} nombre positif ")
print(f"on a {cn} nombre negatif ")
print(f"on a {cz} nombre zero ")

    