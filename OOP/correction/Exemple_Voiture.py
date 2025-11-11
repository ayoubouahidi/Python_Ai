class voiture:
    def __init__(self, v1="Mercedes-Benz", v2="black", v3="AMG-V12"):
        self.__marque = v1
        self.__couleur = v2
        self.__reserveEssence = v3

    # def __init__(self):
    #     self.__marque = "Mercedes-Benz"
    #     self.__couleur = "black"
    #     self.__reserveEssence = "AMG-V12"

    # def __init__(self,v1="Mercedes-Benz"):
    #     self.__marque = v1
    #     self.__couleur = "black"
    #     self.__reserveEssence = "AMG-V12"

    # def __init__(self,v1="Mercedes-Benz",v2="black"):
    #     self.__marque = v1
    #     self.__couleur = v2
    #     self.__reserveEssence = "AMG-V12"


 
    def demarrer(self):
        print("Je demarre")

    def arreter(self):
        print("je m'arrete")

    def getMarque(self):return self.__marque
    def getCouleur(self):return self.__couleur
    def getReserveEssence(self):return self.__reserveEssence

    def setMarque(self, ma):self.__marque = ma
    def setCouleur(self, ma):self.__couleur = ma
    def setReserveEssence(self, ma):self.__reserveEssence = ma

    def affiche(self):
        print(f"la marque est:{self.__marque}, la couleur est{self.__couleur}, de reserve {self.__reserveEssence}")

    def affiche1(self):
        return (f"la marque est:{self.getMarque()}, la couleur est{self.getCouleur()}, de reserve {self.getReserveEssence()}")


# OBJET
m = voiture()
print(m.getMarque())
print(m.getCouleur())
print(m.getReserveEssence())
m.setMarque("BMW")
m.setCouleur("white")
m.setReserveEssence("6.3L")
print(m.getMarque())
print(m.getCouleur())
print(m.getReserveEssence())

# OBJET2
marque = input("saisi la marque: ")
m2 = voiture(marque)
m2.affiche()

# OBJET3
marque = input("saisi la marque: ")
couleur = input("saisi la couleur: ")
m3 = voiture(marque, couleur)
m3.affiche()

# OBJET4
marque = input("saisi la marque: ")
couleur = input("saisi la couleur: ")
reserve = input("saisi la reserve: ")
m2 = voiture(marque, couleur, reserve)
m2.affiche()

# Comportement
m.demarrer()
m.arreter()
print(m2.affiche1())
