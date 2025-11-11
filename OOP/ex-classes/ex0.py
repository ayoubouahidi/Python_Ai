class ayoub:
    def __init__(self,x=0,y=0):#constructeure
        self.__x=x
        self.__y=y
    #getter setter
    def getx(self):
        return self.__x
    def setX(self,a):
        self.__x=a

    def gety(self):
        return self.__y
    def setX(self,a):
        self.__x=a
    
    def sum(self):
        return self.__x+self.__y
    

    def affiche(self):
        print(f"x est : {self.__x} y est : {self.__y}")


#objet
# a = int(input("entrer x :"))
# b = int(input("entrer y : "))
a1=ayoub(4,4)
a1.affiche()
print(a1.sum())

        