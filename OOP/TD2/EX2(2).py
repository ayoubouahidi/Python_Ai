########################*******************************EX2***********************************###########################
#*
from abc import ABC,abstractclassmethod
class IOperation(ABC):
    @abstractclassmethod
    def plus():
        pass
    @abstractclassmethod
    def moins():
        pass



class IAffichage(ABC):
    @abstractclassmethod
    def affiche(self):
        pass



class Complexe(IOperation, IAffichage):
    def __init__(self, partie_reelle, partie_imaginaire):
        self.__partie_reelle = partie_reelle
        self.__partie_imaginaire = partie_imaginaire
    

   
    def plus(self,c1):
        x = self.__partie_reelle + c1.__partie_reelle
        y = self.__partie_imaginaire + c1.__partie_imaginaire
        return Complexe(x,y)
    
    def moins(self,c1):
        x = self.__partie_reelle - c1.__partie_reelle
        y = self.__partie_imaginaire - c1.__partie_imaginaire
        return Complexe(x,y)
    def affiche(self):
        return f'{self.__partie_reelle}+{self.__partie_imaginaire}i'
    




class Reel(IOperation, IAffichage):
    def __init__(self,x):
        self.__x=x
    
    def plus(self,c1):
        x = self.__x + c1.__x
       
        return Reel(x)
    

    def moins(self,c1):
        x = self.__x - c1.__x
        return Reel(x)
    
    def affiche(self):
        return f'{self.__x}'
    
    
#Objet

complexe1 = Complexe(4, 3)
complexe2 = Complexe(2, 1)

reel1 = Reel(10)
reel2 = Reel(5)

print(complexe1.plus(complexe2).affiche())
print(reel1.plus(reel2).affiche())

