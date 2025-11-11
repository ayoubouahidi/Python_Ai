from abc import ABC, abstractmethod

class IPersonne(ABC):
    @abstractmethod
    def affiche(self):
        pass

    @abstractmethod
    def calculerSalaire(self):
        pass

class Profil:
    cmp=0
    def __init__(self,id, poste):
        
        self.__poste = poste
        Profil.cmp+=1
        self.__id=Profil.cmp
    
    def getposte(self):
        return self.__poste 
    
class Personne(IPersonne):
    cmp= 0
    def __init__(self,nom,prenom,date_naissance,salaire,profil):
        
        self.__nom = nom
        self.__prenom = prenom
        self.__date_naissance = date_naissance
        self.__salaire = salaire
        self.__profil=profil
        Personne.cmp+=1
        self.__id=Personne.cmp
       
    
    
    def getsalaire(self):
        return self.__salaire
    
    def getprofil(self):
        return self.__profil
    
    def setsalaire(self,a):
        self.__salaire=a

    

    
    def calculerSalaire(self):
        if self.__profil.getposte().__eq__("dir"):
            self.setsalaire(self.getsalaire()+self.getsalaire()*0.2)
            return self.__salaire
        
        elif self.__profil.getposte()=="emp":
            self.setsalaire(self.getsalaire()+self.getsalaire()*0.1)
            return self.__salaire
        
        else:
             
             return self.__salaire
        
    def affiche(self):
        return f"Je suis {self.__nom} {self.__prenom} né le {self.__date_naissance} mon salaire est {self.calculerSalaire()} dh "
    
    

        

#Objet
p = Profil(1,"dir")
personne1 = Personne("SAlMI", "Karim", "02 juin 2000", 20000,p)
# print(personne1.calculerSalaire())
print(personne1.affiche())



       
    



    
    





