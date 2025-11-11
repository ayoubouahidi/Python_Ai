from abc import ABC,abstractmethod

class Ipersonne(ABC):
    @abstractmethod
    def affiche():pass
    @abstractmethod
    def calculersalair():pass

class Profil:
    cmp=0
    def __init__(self,code,libelle):
        
        Profil.cmp+=1
        self._id=Profil.cmp
        self._code=code
        self._libelle=libelle

    def getlibelle(self):
        return self._libelle

class Personne(Ipersonne,Profil):
    def __init__(self,id,nom,prenom,daten,salaire,code,libelle):
        super().__init__(code,libelle)
        self.__id=id
        self.__nom=nom
        self.__prenom=prenom
        self.__datenaissance=daten
        self.__salaire=salaire
        # self.__profil=profil

    def getsalaire(self):
        return self.__salaire
    
    def setsalaire(self,a):
        self.__salaire=a

    # def affiche(self):
    #     return f'Je suis {self.__profil.getlibelle()} {self.__nom} {self.__prenom} né le {self.__datenaissance} mon salair {self.calculersalair()}'
    
    def calculersalair(self):
        if self.getlibelle()=='directeur':
            self.setsalaire(self.getsalaire()+self.getsalaire()*0.2)
            return self.__salaire
        else:  
            self.setsalaire(self.__salaire*0.1+self.__salaire) 
            return self.__salaire    
    def affiche(self):
        return f'Je suis {self.getlibelle()} {self.__nom} {self.__prenom} né le {self.__datenaissance} mon salair {self.calculersalair()}'
    
#creation objet 
# pr=Profil(22,"directeur")
p = Personne(1,"ayoub","ouahidi","22/22/22",20000,22,"directeur")  
print(p.affiche())

        

    
    


