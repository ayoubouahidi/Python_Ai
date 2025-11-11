class Persone:
    def __init__(self, d1, d2, d3):
        self.__cin = d1
        self.__nom_complet = d2
        self.__date_naissance = d3

    # GETTERS
    def getCin(self):
        return self.__cin

    def getNom_complet(self):
        return self.__nom_complet

    def getDate_naissance(self):
        return self.__date_naissance

    # SETTERS
    def setCin(self, a1):
        self.__cin = a1

    def setNom_complet(self, a1):
        self.__nom_complet = a1

    def setDate_naissance(self, a1):
        self.__date_naissance = a1

    # AFFICHER
    def afficher(self):
        print(
            f"Votre CIN: {self.__cin}, votre nom {self.__nom_complet}, votre date de naissance {self.__date_naissance} ")


person = Persone()
person.afficher()
