class student:
    def __init__(self,name="Nom",secondename="Prenom"):
        self.__name=name
        self.__secondename=secondename
    def getname(self):
        return self.__name
    def getsecondename(self):
        return self.__secondename
    def setname(self,name):
        self.__name=name 
    def setsecondename(self,secondename):
        self.__secondename=secondename
    def somme(self):
        return self.__name+self.__secondename
    def print(self):
        print("le nom est ",self.getname(),"le prenom ",self.getsecondename())
class sciencestudnet(student):
    def afficherr(self):
        print(" test de fonction ")
a = sciencestudnet()
a.print()
a.afficherr()

    
    
    


        