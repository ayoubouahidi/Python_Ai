class Complexe :
    def __init__(self,reel=0,imaginaire=0):
        self.__reel=reel
        self.__imaginaire=imaginaire
    
    #getters
    def getReel(self):
        return self.__reel
    def getImaginaire(self):
        return self.__imaginaire
    
    #setters

    def setReel(self,a):
        self.__reel=a
    def setImaginaire(self,b):
        self.__imaginaire=b
    #methodes 

    def toString(self):
        return f'{self.__reel} {self.__imaginaire}i'
    
    def __str__(self):
        return f'{self.__reel} {self.__imaginaire}i'
    
    def addition(self,c):
        x = self.__reel+c.__reel
        y = self.__imaginaire+c.__imaginaire
        return Complexe(x,y)
    
    def __add__(self,c):
        x = self.__reel+c.__reel
        y = self.__imaginaire+c.__imaginaire
        return Complexe(x,y)
    
    def substraction(self,c):
        x = self.__reel-c.__reel
        y = self.__imaginaire-c.__imaginaire
        return Complexe(x,y)
    
    def __sub__(self,c):
        x = self.__reel+c.__reel
        y = self.__imaginaire+c.__imaginaire
        return Complexe(x,y)
    
    def multiplication(self,c):
        x = 
        


    
    


    

