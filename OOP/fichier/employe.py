from personne import Personne
from comparable import Comparable


class Employe(Personne,Comparable):
    def __init__(self,num,nom,adr,tel,grade,sal):
        super().__init__(num,nom,adr,tel)
        #Personne.__init__(self,num,nom,adr,tel)
        if type(grade) is not int :
            raise TypeError("le grade doit etre de type entier")
        else :
            self.__Grade = grade

        if type(sal) is not float :
            if sal < 4000 :
                raise ValueError("salaire doit etre superieur à 4000")
            raise TypeError("le salaire doit etre de type float")
        else :
            self.__Salaire = sal
    
    def get__Grade(self) : return self.__Grade
    def get__Salaire(self) : return self.__Salaire

    def set__Grade(self,g) :
        self.__Grade = g
    def set__Salaire(self,s) :
        self.__Salaire = s

    def affiche(self):
        print(f" Num Personne :{self._NumPers} Nom Complet :{self._NomCompletPers} Adresse : {self._Adresse} Telephone : {self._Tel} Grade : {self.__Grade} Salaire : {self.__Salaire}")

    def compareNum(self,pers1):
         if self._NumPers == pers1.get_NumPers() :
             return True
         return False
        

    def salaireCompare(self,pers1):
        if self.__Salaire < pers1.get__Salaire() :
            return -1
        elif self.__Salaire > pers1.get__Salaire() :
            return 1
        else :
            return 0

        