from abc import ABC,abstractclassmethod

class Ipersonne(ABC):
    @abstractclassmethod
    def affiche():pass
    @abstractclassmethod
    def calculersalair():pass


class Profil():
    def __init__(self,code,libelle) :
        self.__code=code
        self.__libelle=libelle

    def getlibelle(self):
        return self.__libelle
    
    def affiche():pass



class Personne(Ipersonne,Profil):
    cmp = 0
    def __init__(self,nom,prenom,daten,salaire,profil) :
        Personne.cmp+=1
        self.__id=Personne.cmp
        self.__nom= nom
        self.__prenom = prenom
        self.__datenaissance = daten
        self.__salaire=salaire
        self.__profil=profil
 

    def getsalaire(self):
        return self.__salaire
    
    def setsalaire(self,a):
        self.__salaire=a

        


    def calculersalair(self):
        if self.__profil.getlibelle() == "directeur":
            self.setsalaire(self.getsalaire()+self.getsalaire()*0,2)
            return self.__salaire
        else:
            self.setsalaire(self.getsalaire()+self.getsalaire()*0.1)
            return self.__salaire
        

    

    def affiche(self):
        return f"Je suis le {self.__profil.getlibelle()} {self.__nom} {self.__prenom} né le {self.__datenaissance} mon salaire est {self.__salaire} "
    
    
pr = Profil("N63","emp") 
print(pr.getlibelle())  
p = Personne("ayoub","ouahidi","22 22 22",20000,pr)
p.calculersalair()
print(p.affiche())
"""ex2"""
# from abc import ABC,abstractclassmethod
# class Ioperation(ABC):
#     @abstractclassmethod
#     def plus():pass
#     @abstractclassmethod
#     def moins():pass

# class IAffichage(ABC):
#     @abstractclassmethod
#     def affiche():pass


# class Complexe(Ioperation,IAffichage):
#     def __init__(self,reel,img):
#         self.__reel=reel
#         self.__img=img
        
#     #accesseur
#     def getimaginaire(self):
#         return self.__img
#     def getreel(self):
#         return self.__reel
#     #modificateur
#     def setimaginaire(self,a):
#         self.__img=a
#     def setreel(self,a):
#         self.__reel=a
#     #les autres methodes du l'interface Ioperation
#     def plus(self,c1):
#         x  = self.__reel+c1.__reel
#         y = self.__img+c1.__img
#         return Complexe(x,y)
#     def __add__(self,c1):
#         x  = self.__reel+c1.__reel
#         y = self.__img+c1.__img 
#         return Complexe(x,y)
    
#     def moins(self,c1):
#          x  = self.__reel-c1.__reel
#          y = self.__img-c1.__img
#          return Complexe(x,y)
#     def __sub__(self,c1):
#          x  = self.__reel-c1.__reel
#          y = self.__img-c1.__img
#          return Complexe(x,y)
#     #les autres methodes du l'interface IAffichage
#     def affiche(self):
#         return f"{self.__reel}+{self.__img}i ayoub"
    
#     def __str__(self):
#         return f'{self.__reel}+{self.__img}i ayoub'
    
    
# # class reel(Ioperation,IAffichage):
# #     def __init__(self) 


# #creation des objet 
# p1 = Complexe(2,3)
# p2 = Complexe(2,3)
# # l = complex()
# p3 = p1 + p2 

# # l.__str__
# # (p1).__sub__(p2)
# print("addition est ",p3)




    





