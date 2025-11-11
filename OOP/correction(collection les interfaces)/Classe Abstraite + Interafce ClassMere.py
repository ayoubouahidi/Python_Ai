from abc import ABC,abstractmethod
import math
class Imprimable:
    
    def imprimer(self):pass

class Forme(ABC,Imprimable):
    def __init__(self,x,y):
        self._x=x
        self._y=y   
    @property
    def X(self):return self._x 
    @X.setter   
    def X(self,x):self._x=x

    @property
    def y(self):return self._y
    @y.setter
    def y(self,y):self._y=y

    @abstractmethod
    def surface(self):pass

    @abstractmethod
    def perimetre(self):pass

    def deplacer(self,depx,depy):
        self.X(self._x+depx) 
        self._y=self._y+depy

    def affiche(self):
        print (f'X= {self._x} \n Y= {self._y}')  

    def imprimer(self):
        print(f'\n Le surface  est : {self.surface()}\n et Le perimetre : {self.perimetre()}')

class Cercle(Forme):
    def __init__(self,x,y,r):
        super().__init__(x,y)
        self.__rayon=r
  
    def getRayon(self):
        return self.__rayon 

    def setRayon(self,r):
        self.__rayon=r

    def surface(self):
        return math.pi*(self.__rayon**2)
    
    def perimetre(self):
        return 2*math.pi*self.__rayon
    
    def imprimer(self):
        super().imprimer()
        print (f'\n et son rayon est : {self.__rayon} ')


class Rectangle(Forme) :
    def __init__(self,x,y):
        super().__init__(x,y)

    def surface(self):
        return self._x*self._y
    
    def perimetre(self):
        return 2*(self._x+self._y)
        
    def imprimer(self):
        super().imprimer()
              
c=Cercle(4,2,6)
c.imprimer()


r=Rectangle(2,6)      
r.imprimer()