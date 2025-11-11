import math
class datenaiisance:
    def __init__(self,j,m,a): 
        self.__jour=j
        self.__mois=m
        self.__annee=a

    def getJour(self):
        return self.__jour
    def getmois(self):
        return self.__mois
    def getannee(self):
        return self.__annee
    
    def setJour(self,a):
        self.__jour=a
    def setMois(self,b):
        self.__mois=b
    def setAnne(self,c):
        self.__annee=c
    
    def affiche(self):
        print(f"{self.__jour}  ,{self.__mois} ;  {self.__annee}" )
class employer:
    def __init__(self,matricule):
        self.__ma=matricule
   



    
