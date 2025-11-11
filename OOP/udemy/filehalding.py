# print("avancement", end="\r")

# print("avancement\r")
import re

# chaine = input("entrer une chaine de caractre : ")
# expression =re.compile(r"[a-z]+",chaine)
# print(expression)


Nameage =input("entrer une chaine de caracter ")
# ages = re.findall(r'\d{1,3}', Nameage) #chercher de un, deux ou trois entiers décimaux
# print(ages) 

expression = re.compile(r'\d{1,3}')
print(expression.findall(Nameage))
