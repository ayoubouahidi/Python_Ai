from abc import ABC,abstractmethod
class Comparable(ABC):
    @abstractmethod
    def CompareTo():pass

class Personne(Comparable):
    def __init__(self,age,cin):
        self.__age = age
        self.__cin = cin
    def getAge(self):
        return self.__age
    def setAge(self,newage):
        self.__age = newage
    def getCin(self):
        return self.__cin
    def setCin(self,newcin):
        self.__cin = newcin
    def CompareTo(self,p1):
        return self.__age == p1.getAge()
    def Imprimer(self):
        print(f'Age et CIN : {self.__age} {self.__cin}')

class Outils(Comparable):
    def __init__(self,longueur):
        self.__longueur = longueur
    def getLongueur(self):
        return self.__longueur
    def setLongueur(self,newlongueur):
        self.__longueur = newlongueur
    def CompareTo(self,o1):
        if self.__longueur == o1.getLongueur():
            return True
        return False
    def Imprimer(self):
        print(f'longueur est : {self.__longueur}')

p = Personne(20,'HH39423')
p1 = Personne(22,'hhh')
if p.CompareTo(p1):
    print('meme age')
else:
    print('different age')
p.Imprimer()
p1.Imprimer()


o1 = Outils(123)
o2 = Outils(432)
res = o1.CompareTo(o2)
if res : 
    print("meme longueur")
print("different longueur")
o1.Imprimer()
o2.Imprimer()