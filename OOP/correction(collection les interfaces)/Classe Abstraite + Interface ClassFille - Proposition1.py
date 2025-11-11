from abc import ABC,abstractmethod
from math import pi

class Imprimable(ABC):
    @abstractmethod
    def Imprimer(self):pass
    
class Forme(ABC):
    def __init__(self,x,y):
        self._x = x
        self._y = y
        
    @property
    def X(self):return self._x
    @X.setter
    def X(self,newx):self._x = newx

    @property
    def Y(self):return self._y
    @Y.setter
    def Y(self,newy):self._y = newy

    @abstractmethod
    def surface(self):pass

    @abstractmethod
    def perimetre(self):pass

    def deplacer(self,dx,dy):
        self.X(self._x + dx)
        self.Y(self._y + dy)

    def Afficher(self):
        print(f'le deplacement : {self._x},{self._y}')

                
class Cercle(Forme,Imprimable):
    def __init__(self, x, y,rayon):
        super().__init__(x, y)
        self.__rayon = rayon

    def getRayon(self):
        return self.__rayon
    def setRayon(self,newrayon):
        self.__rayon = newrayon

    def surface(self):
        return pi * (self.__rayon ** 2)

    def perimetre(self):
        return (2 * pi * self.__rayon)

    def Imprimer(self):
        print(f'La surface du cercle  : {self.surface()}\ et Le perimetre  : {self.perimetre()} le rayon : {self.__rayon}')

class Rectangle(Forme,Imprimable):
    def __init__(self,x,y):
        super().__init__(x,y)
    def surface(self):
        return self._x * self._y
    def perimetre(self):
        return 2 * (self._x + self._y)
    def Imprimer(self):
        print(f'La surface du Rectangle  : {self.surface()}\n et Le perimetre du Rectangle  : {self.perimetre()}')

c = Cercle(4,2,6)
c.Imprimer()

r = Rectangle(2,6)
r.Imprimer()