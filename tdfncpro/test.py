# # fonction sui transforme une chaine en majuscule
# def maj(s):
#     # initialisation de la chaine
#     s_maj = ""
#     for x in s:
#         # on teste si x est un caractère minuscule
#         if ord(x) >= 97 and ord(x) <= 122 :
#             # on transforme x en majuscule
#             x = chr(ord(x) - 32)
#             s_maj = s_maj + x
#         else:
#             s_maj = s_maj + x
#     return s_maj

# # Exemple
# s1 = "helLLLo worlD"
# s2 = "Hello World !"
# print(maj(s1)) # affiche HELLO WORLD
# print(maj(s2)) # affiche HELLO WORLD !

def puissance(x,y):
    A= 1
    for i in range (y):
        A = x*A
    return A
l = puissance(3,2)

print(l)


