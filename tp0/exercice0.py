import math

R = int(input("entrer le rayon : "))

# on va calculer volume d’une sphère

L = R ** 3
A = math.pi * L
volume = 4/3 * A

print("le volume d\'un\spere : " + str(volume))
