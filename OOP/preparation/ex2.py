from abc import ABC , abstractmethod
class Personne(ABC):
    def __init__(self,Numpers,NomComplet,Adresse,Tel):
        self.__Numpers=Numpers
        self.__Nom=NomComplet
        self.__Adresse= Adresse
        self.__Tel= Tel

    def getNum(self):
        return self.__Numpers
    def getNom(self):
        return self.__Nom
    def getAdresse(self):
        return self.__Adresse
    def getTel(self):
        return self.__Tel
    #setter
    def setNum(self,a):
        self.__Numpers=a
    def setNom(self,a):
        self.__Adresse=a
    def setAdresse(self,a):
        self.__Adresse=a
    def setTel(self,a):
        self.__Tel=a 
    #methodes
    @abstractmethod
    def affiche(self):
        pass
#objet
# per1 = Personne(1,'ayoub','safi',212620341685)


