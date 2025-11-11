import math
class  Eq2Degre:
    def __init__(self,x1=0,x2=0,x3=0):
        self.__delta=(x2)**2-4*x1*x3
        self.__a = x1
        self.__b = x2
        self.__c = x3
        self.__s1 = 0
        self.__s2 = 0

    def getDelta(self):
        return self.__delta
    def getA(self):
        return self.__a
    def getB(self):
        return self.__b
    def getC(self):
        return self.__c
    def getS1(self):
        return self.__s1
    def getS2(self):
        return self.__s2
    
    def setDelta(self,x):
        self.__delta = x
    def setA(self,y):
        self.__a=y
    def setB(self,z):
        self.__b=z
    def setC(self,w):
        self.__c=w
    def setS1(self,u):
        self.__s1=u
    def setS2(self,v):
        self.__s2 = v
    def afficherdelta(self):
        print(f"delta est : {self.__delta}")
    

    def resoudre(self):
        if self.__delta > 0:
           self.__s1 = (-self.getB()+math.sqrt(self.__delta))/(2*(self.__a))
           self.__s2 = (-self.getB()-math.sqrt(self.__delta))/(2*(self.__a))
        else:
            if self.__delta == 0:
                self.__s1 = (-self.__b)/self.__a
            else:
                print("n'est pas une solution dans R")
    def toString(self):
        if self.__delta>0:
            print("deux solution ")
        else:
            if self.__delta == 0 :
                print("une solution")
            else:
                print("n'est pas une solution ")
    def affichersolution(self):
        print(f"les solution sont {self.__s1} {self.__s2}")
    
#OBJET
a1 = 1
b1 = 1
c1 = -2

eq1 = Eq2Degre(a1,b1,c1)
eq1.afficherdelta()
eq1.resoudre()
eq1.toString()
eq1.affichersolution()








    
