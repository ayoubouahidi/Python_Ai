class Fournisseur:
    def __init__(self,Code ,NomCme,Adresse):
        self.__Code= Code
        self.__NomCme=NomCme
        self.__Adresse=Adresse

        # getters les modificateur
    def getCode(self):
        return self.__Code
    def getNomcme(self):
        return self.__NomCme
    def getAdresse(self):
        return self.__Adresse
    #setters les accececeur
    
    def setCode(self,a):
        self.__Code=a
    def setNomCme(self,b):
        self.__NomCme=b
    def setAdresse(self,c):
        self.__Adresse=c
    
    def Afiiche(self):
        print(f"le code est {self.__Code}::: le nom est {self.__NomCme};; l'adresse {self.__Adresse}  ")
#Objet 



class Appelectrique:
    def __init__(self,reference,pui,poi,prix,fournisseur):
        self.__re=reference
        self.__pui=pui
        self.__poi=poi
        self.__prix=prix
        self.__for=fournisseur

    @property
    def Re(self):
        return self.__re
    @property
    def Puissance(self):
        return self.__pui
    @property
    def poids(self):
        return self.__poi
    @property
    def prix(self):
        return self.__prix
    @property
    def fournisseur(self):
        return self.__for
    
    
    @Re.setter
    def Re(self,a):
        self.__re=a
    @prix.setter
    def prix(self,d):
        self.__prix=d

    @Puissance.setter
    def puissance(self,b):
        self.__pui=b
    @poids.setter
    def Poi(self,c):
        self.__poi=c
    

    def getErgetique(self,a):
        if self.__pui < 300  :
            return "class A"
        else:
            if 300< self.__pui < 1000:
                return "class B "
            else:
                return "class  c "
    def affiche(self):
        
        print(f"{self.__re};{self.__poi};{self.__prix};{self.Puissance};{self.getErgetique(en)}")
        self.__for.Afiiche()
# a1= Appelectrique()
F1= Fournisseur("ayoub",'ouahidi',"test")



en=Appelectrique("ayoub",2000,'ouahidi',"test",F1)
en.affiche()


# class Batiment:
#     def __init__(self,adr):
#         self.__adr=adr

#     def getAdr(self):
#         return self.__adr
    
def Compare(self,a):
    return self.__adr==a.__adr
# class Television(Appelectrique):
#     def __init__(self,reference,pui,poi,prix,fre,type):
#         super().__init__(reference,pui,poi,prix)
#         self.__fre=fre
#         self.__type=type
    
#     def affiche



    
            

        
print(1+1==2)