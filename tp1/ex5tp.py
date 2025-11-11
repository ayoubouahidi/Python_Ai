n = int(input("donner un nombre : "))
p = 10 
for i in range(n,0,-1):
    p = p*(1/i)
print("le resultat : ",p)
