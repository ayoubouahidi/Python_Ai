from abc import ABC,abstractmethod
from math import pi

class Imprimable(ABC):
    @abstractmethod   #interface
    def Imprimer():pass
    
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
    def surface():pass

    @abstractmethod
    def perimetre():pass

    def deplacer(self,dx,dy):
        self.X(self._x + dx)
        self.Y(self._y + dy)

    def Afficher(self):
        print(f'le deplacement : {self._x},{self._y}')

    def Afficher(self):
        print(f'\n Le surface  est : {self.surface()}\n et Le perimetre : {self.perimetre()}')   

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
        super().Afficher()
        print(f' Le rayon : {self.__rayon}')

class Rectangle(Forme,Imprimable):
    def __init__(self,x,y):
        super().__init__(x,y)
    def surface(self):
        return self._x * self._y
    def perimetre(self):
        return 2 * (self._x + self._y)
    def Imprimer(self):
        super().Afficher()

c = Cercle(4,2,6)
c.Imprimer()

r = Rectangle(2,6)
r.Imprimer()