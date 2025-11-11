class Personne:
    #constructeur
    #initialisation
    def __init__(self,cin ="HH00000",nomc ="AYOUB Ouahidi", date="00/00/0000") : #inisialisation
        self.__Cin=cin
        self.__nomcomplet=nomc
        self.__Datedenaissance=date
        #3 getter 
    def getcin(self):
        return self.__Cin
    def getnomcomlet(self):
        return self.__nomcomplet
    def getdate(self):
        return self.__Datedenaissance
    #3 set
    def setcin(self,cin):
        self.__Cin=cin
    def setnomcomplet(self,nomc):
        self.__nomcomplet=nomc
    def setdate(self,date):
        self.__Datedenaissance=date
    #  afficher
    def afficher(self):
        print("CIN :",self.__Cin," ","nom complet :",self.getnomcomlet()," ","date de naissance:",self.__Datedenaissance)
#CREATION OBJET
p1=Personne()
p1.afficher()
p2=Personne("hh9009","omar ntic","21/12/02")
p2.afficher()
p2.setcin("hh1234")
print(p2.getcin())
p2.afficher()

