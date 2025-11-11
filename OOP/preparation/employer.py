from ex2 import Personne
from ex3 import Comparable
class Employer(Personne,Comparable):
    def __init__(self,Num,Rue,Ville,CodePostal,Grade,Salaire):
        super().__init__(Num,Rue,Ville,CodePostal)
        self.__Grade=Grade
        self.__Salaire=Salaire
    
    #getters
    def getGrade(self):
        return self.__Grade
    def getSalaire(self):
        return self.__Salaire
    #setters
    def setGrade(self,a):
        self.__Grade=a
    def setSalaire(self,a):
        self.__Salaire=a

    #methode
    def affiche(self):
        print(f"le salaire est {self.__Salaire} le grade est {self.__Grade}")

    def compareNum(self,pe1):
        return self.getNum==pe1.getNum()
     
    def salaireCompare(self,pe1):
        if self.__Salaire>pe1.__Salaire:
            return 1 
        else:
            if self.__Salaire<pe1.__Salaire:
                return -1
            else:
                return 0 
    
        
        