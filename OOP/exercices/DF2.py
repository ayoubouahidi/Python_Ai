import math

class Vehicule:
    def __init__(self,marque,date,prix):
        self._marque=marque
        self._date=date
        self._prixachat=prix
        self.__prixcouranr=prix


    

    def getMarque(self):
        return self._marque
    def getDate(self):
        return self._date
    def getPrix(self):
        return self._prixachat
    def getPC(self):
        return self.__prixcouranr
    
    def setMarque(self,a):
        self._marque=a
    def setdate(self,b):
        self._date=b
    def setPrix(self,c):
        self._prixachat= c
    def setPC(self,d):
        self.__prixcouranr=d



    def calculePrix(self,anneActuelle):
        anneActuelle = 2023
        a  = (anneActuelle - self.getDate())*0.01
        self.__prixcouranr(math.max(0,self.getPrix()*(1-a)))


        
    
    def affiche(self):
        print(f"la marque est {self._marque} la date :{self._date}, le prix  {self._prixachat}")


class Voiture(Vehicule):
    def __init__(self,marque,date,prix,cylindre,nbrporte,puissance,kilo):
        super().__init__(marque,date,prix)
        self.__Cylindre=cylindre
        self.__Nbrporte=nbrporte
        self.__Puissance=puissance
        self.__Kilo=kilo


    def getCylindre(self):
        return  self.__Cylindre
    def getNbreporte(self):
        return self.__Nbrporte
    def getPuissance(self):
        return self.__Puissance 
    def getKilo(self):
        return self.__Kilo
    
    def setCylindre(self,a):
        self.__Cylindre=a
    def setNbreporte(self,b):
        self.__Nbrporte=b
    def stPuissance(self,c):
        self.__Puissance=c
    def setKilo(self,d):
        self.__Kilo=d

    def calculePrix(self, anneActuelle):
        d = (anneActuelle - self.getDate()) * 0.02
        if self.__Kilo >= 10000:
            d+=  0.05 * int(self.__Kilo / 10000)
        if self.getMarque == "porche" or "Ferrari":
            d -=0.2
            
        else :
            d +=0.1
        self.setPC(max(0,self.getPrix()*(1-d)))
        




    def affiche(self):
        super().affiche()
        print(f"le cylndre est : {self.__Cylindre} nbvr du porte est : {self.__Nbrporte} puissance est {self.__Puissance} kilo est {self.__Kilo} calcul pri est ; { self.__prixcouranr} ")
v1=Voiture("porche",2020,170000,20,5,20,20000)
v1.calculePrix(2023)
v1.affiche()

class Avion(Vehicule):
    def __init__(self,marque,date,prix,tm,nh):
        super().__init__(marque,date,prix)
        self.__typem=tm
        self.__nbrh=nh
    

    def getType(self):
        return self.__typem
    def getNbreh(self):
        return self.__nbrh
    
    def setTypem(self,a):
        self.__typem=a
    def setNbreh(self,b):
        self.__nbrh=b

    def calculePrix(self):
        d  = self.__prixcouranr == self.getPrix()
        
        if self.__nbrh > 100 :
            d= 0.1 * self.__nbrh / 100
        else:
            d=0.1 * self.__nbrh / 1000
        self.__prixcouranr(math.max(0.0, (1.0 - d) * self.getPrix()))

    def affiche(self):
        super().affiche()
        print(f"type du moteur est {self.__typem} nbr h {self.__nbrh}")
    
    


       


