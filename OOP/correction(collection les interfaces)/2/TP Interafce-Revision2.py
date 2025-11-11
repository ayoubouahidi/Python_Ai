
from abc import ABC, abstractmethod

from abc import ABC,abstractmethod
class IOperation(ABC):
    @abstractmethod
    def plus():pass
    @abstractmethod
    def moins():pass 

class Affichage(ABC):
    @abstractmethod
    def affiche(self):pass

class Complexe(IOperation,Affichage):
    def __init__(self,re,im):
        self.__reel = re
        self.__imaginaire = im

    @property
    def Reel(self):return self.__reel
    @Reel.setter
    def Reel(self,re):self.__reel =re

    @property
    def Imaginaire(self):return self.__imaginaire
    @Imaginaire.setter
    def Imagianaire(self,im): self.__imaginaire = im

    def plus(self,obj):
        x = self.__reel + obj.__reel
        y = self.__imaginaire + obj.__imaginaire
        return Complexe(x,y)

    def moins(self,obj):
        x = self.__reel - obj.__reel
        y = self.__imaginaire - obj.__imaginaire
        return Complexe(x,y)

    def affiche(self):
        return f'{self.__reel}+{self.__imaginaire}i'

class Reel(IOperation,Affichage):
    def __init__(self,x):
        self.__x = x
    
    def plus(self,obj):
        return Reel(self.__x + obj.__x)

    def moins(self,obj):
        return Reel(self.__x - obj.__x)
    
    def affiche(self):
        return self.__x

c1 = Complexe(3,4)
print(c1.affiche())
c2 = Complexe(1,2)
print(c2.affiche())
c3=c1.plus(c2)
print(c3.affiche())
c4=c2.moins(c1)
print(c4.affiche())
r1 = Reel(8)
r2 = Reel(6)
print(r1.affiche())
r3 = r1.plus(r2)
print(r3.affiche())
r4 = r1.moins(r2)
print(r4.affiche())