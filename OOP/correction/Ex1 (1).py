import math


class Stagiaire:
    def __init__(self, s0="12", s1="Bahraoui", s2="Mohammed-Amine", s3="DD", n1="19", n2="-7", n3="11"):
        self.__matricule = s0
        self.__nom = s1
        self.__prenom = s2
        self.__filiere = s3
        self.__note1 = n1
        self.__note2 = n2
        self.__note3 = n3

# GETTERS
    def getMatricule(self):
        return self.__matricule

    def getNom(self):
        return self.__nom

    def getPrenom(self):
        return self.__prenom

    def getFiliere(self):
        return self.__filiere

    def getNote1(self):
        return self.__note1

    def getNote2(self):
        return self.__note2

    def getNote3(self):
        return self.__note3

# SETTERS
    def setMatricule(self, z):
        self.__matricule = z

    def setNom(self, z):
        self.__nom = z

    def setPrenom(self, z):
        self.__prenom = z

    def setFiliere(self, z):
        self.__filiere = z

    def setNote1(self, z):
        self.__note1 = z

    def setNote2(self, z):
        self.__note2 = z

    def setNote3(self, z):
        self.__note3 = z

# CHECKING NOTES
    def check(self):
        if self.__note1 < 0:
            self.__note1 = 0
        if self.__note2 < 0:
            self.__note2 = 0
        if self.__note3 < 0:
            self. __note3 = 0
# EQUAL

    def equal(self,x):
        return self.__matricule == x.__matricule
# MOYENNE

    def moyenne(self):
        m = ((self.__note1 + self.__note2 + self.__note3)/3)
        return m

# AFFICHER
    def afficher(self):
        print(
            f"votre nom complet est {self.__nom} {self.__prenom}, votre filiere {self.__filiere} \n Votre Notes {self.__note1}\n {self.__note2}\n {self.__note3}\n Votre moyenne est {round(self.moyenne(), 2)}")


# CONSTRUCTEUR
S = Stagiaire()
S.setMatricule("52")
S.setNom("Ayman")
S.setPrenom("test")
S.setFiliere("ICT")
S.setNote1(11)
S.setNote2(-9)
S.setNote3(20)
S.moyenne()
S.check()
S.afficher()
S2 = Stagiaire()
z = S.equal(S2)


if z:
    print("bon")
print("different")
