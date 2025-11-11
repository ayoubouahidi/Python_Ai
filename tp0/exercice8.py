import math

annee = int(input("entrer annee : "))

if (annee % 4 != 0) or (annee % 100 == 0 and annee % 400 != 0):
    print('annee commune')
else :
    print('anne bissextile ')

    
