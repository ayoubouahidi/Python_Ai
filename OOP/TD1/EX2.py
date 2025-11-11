class Complexe:
    #METHODE
    def __init__(self,a=0,b=0):

        self.__re=a
        self.__ima=b

    def getre(self):
        return self.__re
    def getima(self):
        return self.__ima
    
    def setre(self,a):
        self.__re=a
    def setima(self,b):
        self.__ima=b
    
    def tostring(self):
        return f'{self.__re}+{self.__ima}i'
        
    def add(self,c1):
        x = self.__re + c1.__re
        y = self.__ima + c1.__ima
        return Complexe(x,y)   
    def __add__(self,c1):
        x = self.__re + c1.__re
        y = self.__ima + c1.__ima
        return Complexe(x,y)


    def sub(self,c1):
        x = self.__re - c1.__re
        y = self.__ima - c1.__ima
        return Complexe(x,y)
    def __sub__(self,c1):
        x = self.__re - c1.__re
        y = self.__ima - c1.__ima
        return Complexe(x,y)

    
    def multi(self,c1):
        x = (self.__re * c1.__re ) - (self.__ima * c1.__ima)
        y = (c1.__re * self.__ima) + (c1.__ima*self.__re)
        return Complexe(x,y)
    def __mul__(self,c1):
        x = (self.__re * c1.__re ) - (self.__ima * c1.__ima)
        y = (c1.__re * self.__ima) + (c1.__ima*self.__re)
        return Complexe(x,y)

    
    def __str__(self):
        return f'{self.__re}+{self.__ima}i ayoub'

    


#OBJET

a = int(input("entrer un nombre : "))
b = int(input("entrer un nombre imaginaire : "))
c = int(input("entrer un nombre : "))
d = int(input("entrer un nombre imaginaire  : "))

c1 = Complexe(a,b)
c2 = Complexe(c,d)

c3 = c1.add(c2)
print("addition :",c3.tostring())

c4= c1.sub(c2)
print("substraction est :",c4.tostring())

c5= c1.multi(c2)
print("multiplication :",c5.tostring())

c6 = c1 + c2
print("addition :",c6)
 
c7 = c1 - c2
print("substraction est :",c7)

c8 = c1*c2
print("multiplication :",c8)
        
    
    





