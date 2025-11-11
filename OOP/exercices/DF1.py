import math
class Figure:
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

    def setCentre(self,x,y):
        self._x=x
        self._y=y


    def affiche(self):
        print(f"x est {self._x} ;  y est { self._y} ")



class Cercle(Figure) : # class fille 
    def __init__(self,x,y,rayon):
        super().__init__(x,y)     # constructeur 
        self.__rayon=rayon
    
    
    def getRayon(self):
        return self.__rayon
    
    def setRayon(self,z):
        self.__rayon=z
    
    def surface(self):
        return math.pi*(self.__rayon**2)

    
    def affiche(self):
        super().affiche()

        print(f' le rayon est {self.__rayon} surface est : {self.surface()} ')


class Rectangle(Figure):
    def __init__(self,x,y,largeur,langueur):
        super().__init__(x,y)
        self._largeur=largeur
        self._langueur=langueur
    def getLargeur(self):
        return self._largeur
    def getLangueur(self):
        return self._langueur
    
    def setLargeur(self,a):
        self._largeur=a
    def setLangueur(self,b):
        self._langueur= b 
    
    def surface(self):
        return self._langueur*self._largeur
    
    def affiche(self):
        super().affiche()
        print(f"largeur est {self._largeur};langueur est {self._langueur} surface est :{self.surface()} ")


class RectangleColore(Rectangle):
    def __init__(self,x,y,largeur,langueur,couleur):
        super().__init__(x,y,langueur,largeur)
        self.__couleur=couleur


    def getCouleur(self):
        return self.__couleur
    
    def setCouleur(self,a):
        self.__couleur=a
     
    def affiche(self):
        super().affiche()
        print(f"couleur est {self.__couleur}")




    

c1=Cercle(17,17,18)
c1.setX(19)
print(c1.getX())
c1.setY(20)
print(c1.getY())
c1.affiche()

print("surface est : ",c1.surface())




    
    
     
        
    