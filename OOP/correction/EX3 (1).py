import math


class Eq2Degre:
    def __init__(self, x1, x2, x3):
        self.__r1 = 0
        self.__r2 = 0
        self.__delta = (x2**2)-4*x1*x3
        self.__a = x1
        self.__b = x2
        self.__c = x3

#GETTERS

    def getR1(self):
        return self.__r1

    def getR2(self):
        return self.__r2

    def getDelta(self):
        return self.__delta

    def getA(self):
        return self.__a

    def getB(self):
        return self.__b

    def getC(self):
        return self.__c

#SETTERS

    def setR1(self, c):
        self.__r1 = c

    def setR2(self, c):
        self.__r2 = c

    def setDelta(self, c):
        self.__delta = c

    def setA(self, c):
        self.__a = c

    def setB(self, c):
        self.__b = c

    def setC(self, c):
        self.__c = c

#RESOUDRE
    def resoudre(self):
        #self.__delta = math.pow(self.__b,2)-(4*self.__a*self.__c)
        if self.__delta > 0:
            self.__r1 = (-self.__b - math.sqrt(self.__delta))/(2*self.__a)
            self.__r2 = (-self.__b + math.sqrt(self.__delta))/(2*self.__a)
        elif self.__delta == 0:
            self.__r1 = -self.__b/(2*self.__a)
        else:
            print("pas de solution")

#AFFICHER delta

    def afficheDiscriminant(self):
        print(self.__delta)

#affiche solution
    def affichesolution(self):
        print(f"la solution est {self.__r1} {self.__r2}")

    def __str__(self):
        if self.__delta > 0:
            return "Deux solutions"
        elif self.__delta == 0:
            return "Une seule solution"
        else:
            return "Pas de solution"


#DEMANDE a,b AND c
x1 = int(input("donner a: "))
x2 = int(input("donner b: "))
x3 = int(input("donner c: "))

# Create an instance of Eq2Degre with user input
E = Eq2Degre(x1, x2, x3)
E.afficheDiscriminant()
#Resolve the equation
E.resoudre()

#Print the results
E.affichesolution()
print(E)
