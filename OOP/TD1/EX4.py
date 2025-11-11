class Point:

    def __init__(self,x=0,y=0,z=0,c0="couleur"):
        self.__x=x
        self.__y=y
        self.__nom=z
        self.__couleur=c0

    def getX(self):
        return self.__x
    def getNom(self):
        return self.__nom
    def geetY(self):
        return self.__y
    def geyCouleur(self):
        return self.__couleur
     
    
    def setX(self,a):
        self.__x=a
    def setNom(self,b):
        self.__nom=b
    def setY(self,c):
        self.__y=c
    def setCouleur(self,q0):
        self.__couleur=q0
    #affichage point
    def afficherPoint(self):
        print(f'{self.__nom}({self.__x},{self.__y})')
    #translation et symetrie
    def symetrieX(self):
        self.__x=self.__x*-1

    def symetrieY(self):
        self.__y=self.__y*-1
        #self.setX(self.getX()*-1)

    def symetrieaxiale(self,T):
        self.__y=self.__y *-1
        self.__x=self.__x *-1

    def symetriecentrale(self):
        self.__y=self.__y *-1
        self.__x=self.__x *-1
        
    def Translate(self,T):
        self.__x=self.__x + T

    #affichage
    def affichercouleur(self):
        print(f"le couleur est : {self.__couleur}")
    def afficherSymetrieX(self):
        print(f"symetrie est de X : {self.__x}")
    def afficherSymtrieY(self):
        print(f"symetrie de y : {self.__y}")

    def afficherResultat(self):
        print(f'la transltion est {self.__x}')
    
#OBJET
a1=12
ab1=23
b1='A'
t1= 12

point1=Point(a1,ab1,b1)
point1.afficherPoint()
point1.Translate(t1)
point1.afficherResultat()
point1.symetrieX()
point1.afficherSymetrieX()
point1.symetrieY()
point1.afficherSymtrieY()




    





