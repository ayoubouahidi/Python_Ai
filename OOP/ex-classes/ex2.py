from abc import ABC,abstractmethod   #a= abstract ; b = bass , c = class 
import math
class imprimable():
    @abstractmethod
    def imprimer(self):pass

class Forme(ABC,imprimable):
    def __init__(self,x,y):
        self._x=x
        self._y=y
    def getX(self):
        return self._x 
    def getY(self):
        return self._y


    def setX(self,c):
        self._x=c
    def setY(self,d):
        self._y=d 

    
    @abstractmethod
    def surface(self):pass
    @abstractmethod
    def perimetre(self):pass


    def diplacer(self,a):
        self._x = self._x+a
        self._y = self._y+a
    def imprimer(self):
        print(f"x est : {self._x} y est : {self._y} surface est :{self.surface()} ; le perimetre est {self.perimetre()}")




class Rectangle(Forme,imprimable):
    def __init__(self,x,y):
        super().__init__(x,y)

    
    def surface(self):
        return self._x*self._y
    def perimetre(self):
        return 2 * (self._x*self._y)
    
        
    
    def imprimer(self):
        super().imprimer()
        print(f"largeur est {self._x};langueur est {self._y}  ")
    
    def affiche(self):
        print(f"x : { self._x} y : {self._y} ")



class Cercle(Forme,imprimable) :
    def __init__(self,x,y,rayon):
        super().__init__(x,y)
        self.__rayon=rayon
    
    
    def getRayon(self):
        return self.__rayon
    
    def setRayon(self,z):
        self.__rayon=z
    
    def surface(self):
        return math.pi*(self.__rayon**2)
    def perimetre(self):
        return 2 * math.pi*self.__rayon

    
    def imprimer(self):
        super().imprimer()

        print(f' le rayon est : {self.__rayon} ')


#OBJET
re1 = Rectangle(2,2)
re1.surface()
re1.perimetre()
re1.imprimer()

re2 = Cercle(2,2,2)
re2.surface()
re2.perimetre()
re2.imprimer()












