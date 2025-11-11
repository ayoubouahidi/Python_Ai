class Point:
    def __init__(self,n,abs,ord, col):
        self.__nom=n
        self.__abscisse=abs
        self.__ordonne=ord
        self.__couleur=col
#GETTERS
    def getNom(self):
        return self.__nom
    def getAbscisse(self):
        return self.__abscisse
    def getOrdonne(self):
        return self.__ordonne
    def getCouleur(self):
        return self.__couleur

#SETTERS
    def setNom(self, n):
        self.__nom = n
    def setAbscisse(self, abs):
        self.__abscisse = abs
    def setOrdonne(self, ord):
        self.__ordonne = ord
    def setC(self, col):
        self.__couleur = col
#TRANSLATION
    def trans(self, dx):
         self.__abscisse +=dx
#AFFICHER
    def affiche(self):
        print(f"la point {self.__nom} d'abscisse {self.__abscisse} d'ordonne {self.__ordonne} et de couleur {self.__couleur}")

n=input("donner une lettre: ")
abs=int(input(f"donner l'abscisse de {a1}: "))
o=int(input(f"Donner ordonne de {a1}: "))
c=input(f"Donner un couleur: ")
P=Point(n,abs,o,c)
P.affiche()
d=int(input("donner translation: "))
P.trans(d)
P.affiche()
