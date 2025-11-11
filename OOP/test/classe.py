
class Voiture:
    """
    
    def __init__(self) :
    #decleration des atributs
        self.matricule='12345'
        self.marque='mercedes'
        self.modele='2020'
#creation  objet

v1 = Voiture()
print(v1.matricule)
print(v1.marque)
print(v1.modele)




    def __init__(self,a,m,d) :
        self.matricule=a
        self.marque=m
        self.modele=d
print(v2.matricule)
print(v2.marque)

    def __init__(self,a ="B12345",m ="fiat", d='2020'):
        self.matricule=a
        self.marque=m
        self.modele=d
v3 = Voiture("14355","renault","2022")

print(v3.matricule)
print(v3.marque)
print(v3.modele)
"""
#cretion class
#get pour afficher une valeur
    def __init__(self,a ="B12345",m ="fiat", d='2020') :#initialisation
        self.__Matricule=a
        self.__Marque=m
        self.__model=d

    def getMatricule(self):
        return self.__Matricule
    def getMarque(self):
        return self.__Marque
    def getModel(self):
        return self.__model
    

#set pour replacer une valeure par une autre 
    
    def setMatricule(self,m):
        self.__Matricule=m
    def setMarque(self,m):
        self.__Marque=m
    def setModel(self,m):
        self.__model=m
    def afficher(self):
        print("matricule :",self.__Matricule," ","marque :",self.getMarque()," ","model:",self.__model)
    
    #creation objet
v2 = Voiture()
v2.afficher()

v1 = Voiture()
v1.setMatricule("b1212")

print(v1.getMatricule())
print(v1.getMarque())
print(v1.getModel())
v2 = Voiture()
v2.__Matricule="ayoub"
print(v2.__Matricule)
v3 = Voiture("1223")
print(v3.getMatricule())
print(v3.getMarque())
print(v3.getModel())
v4 = Voiture("1223","peugeot")
print(v4.getMatricule())
print(v4.getMarque())
print(v4.getModel())
v5= Voiture("1223","peugeot","veut")
print(v5.getMatricule())
print(v5.getMarque())
print(v5.getModel())






    



