
import datetime 

class Profil:
    cpt = 0
    def __init__(self,code,libelle):
        Profil.cpt +=1
        self.__id= Profil.cpt
        self.__code = code
        self.__libelle = libelle

    def getCode(self):return self.__code
    def setCode(self,c):self.__code = c

    def getLibelle(self):return self.__libelle
    def setLibelle(self,l):self.__libelle = l


class IPersonne:
    def __init__(self):pass
    def affiche(self):pass
    def calculerSalaire(self):pass

class Personne(IPersonne):
    cpt = 0
    def __init__(self,nom,prenom,dateNais,salaire,profil):
        Personne.cpt +=1
        self.__id = Personne.cpt
        self.__nom=nom
        self.__prenom=prenom
        self.__dateNais=dateNais
        self.__salaire=salaire
        self.__profil =profil
    
    @property
    def ID(self):return self.__id

    @property
    def Nom(self):return self.__nom
    @Nom.setter
    def Nom(self,n):self.__nom = n

    @property
    def Prenom(self):return self.__prenom
    @Prenom.setter
    def Prenom(self,p): self.__prenom = p

    @property
    def DateNais(self):return self.__dateNais
    @DateNais.setter
    def DateNais(self,d):self.__dateNais = d 

    @property
    def Salaire(self):return self.__salaire
    @Salaire.setter
    def Salaire(self,s):self.__salaire = s

    @property
    def Profil(self):return self.__profil
    @Profil.setter
    def Profil(self,pr):self.__profil = pr
    
    def calculerSalaire(self):
        if(self.__profil.getCode().__eq__("Directeur")):
           self.__salaire +=  0.2*self.__salaire
           return self.__salaire
        if(self.__profil.getCode().eq__("Employe")):
           self.__salaire +=  0.1*self.__salaire
           return self.__salaire
        return self.__salaire

    def affiche(self):
        # date  = datetime.datetime.strptime(self.__dateNais)
        print("Je suis le "+self.__profil.getLibelle() +" "+self.__nom+" "+self.__prenom+ " né le "+ self.__dateNais + " mon salaire est "+str(self.calculerSalaire())+ " dh")

   

f1=Profil(1,"Directeur")
pers1 = Personne("Alami","Ali","12/09/2000",2000,f1)
pers1.affiche()
print(pers1.calculerSalaire())