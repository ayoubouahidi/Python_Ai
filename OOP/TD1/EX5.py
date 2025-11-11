class Client:
    def __init__(self,matricule="ay1222",nomcomplet="le nom complet ",adresse="adresse"):
        self.__matricule =matricule
        self.__nomcomplet = nomcomplet
        self.__adresse = adresse
    
    def getMatricule(self):
        return self.__matricule
    def getNomcomplet(self):
        return self.__nomcomplet
    def getAdresse(self):
        return self.__adresse
    
    def setMatricule(self,a):
        self.__matricule= a
    def setNomcomplet(self,b):
        self.__nomcomplet = b
    def setAdresse(self,c):
        self.__adresse =c 

    def affiche(self):
        print(f"le nom du client est : {self.__nomcomplet};le matricule est : {self.__matricule}; l'adresse du client est : {self.__adresse}")


class Compte:
    def __init__(self,nc="nomcompte",so=0,client=None):
        self.__nomcompte=nc
        self.__solde=so
        self.__client=client

    def getNomcopte(self):
        return self.__nomcompte
    def getSolde(self):
        return self.__solde
    def getClient(self):
        return self.__client
    

    def setNomcopte(self,a):
        self.__nomcompte = a
    def setSolde(self,b):
        self.__solde = b
    def setClient(self,c):
        self.__client=c

    def afficher(self):
        print(f"le nom u compte est : {self.__nomcompte} ; le solde est :{self.__solde};{self.__client}")
    
    def debiter(self,montant):
        self.__solde = self.__solde  - montant
    def crediter(self,montant):
        self.__solde = self.__solde + montant
    

#OBJET

# nom = input("entrer le nom du compte : ") 
# solde= int(input("entrer le solde du compte : "))
# montant1 = int(input("entrer le montant que cous coulez ajouter :"))

# c1 = Compte(nom,solde)
# c1.afficher()
# if montant1 >= 0 :
#     c1.crediter(montant1)
#     c1.afficher()
# elif montant1 < 0 and solde>montant1:
#     c1.debiter(montant1)
#     c1.afficher()




# class Client:
#     def __init__(self,matricule="ay1222",nomcomplet="le nom complet ",adresse="adresse"):
#         self.__matricule =matricule
#         self.__nomcomplet = nomcomplet
#         self.__adresse = adresse
    
#     def getMatricule(self):
#         return self.__matricule
#     def getNomcomplet(self):
#         return self.__nomcomplet
#     def getAdresse(self):
#         return self.__adresse
    
#     def setMatricule(self,a):
#         self.__matricule= a
#     def setNomcomplet(self,b):
#         self.__nomcomplet = b
#     def setAdresse(self,c):
#         self.__adresse =c 

#     def affiche(self):
#         print(f"le nom du client est : {self.__nomcomplet};le matricule est : {self.__matricule}; l'adresse du client est : {self.__adresse}")
nom = input("entrer le nom du compte : ") 
solde= int(input("entrer le solde du compte : "))
montant1 = int(input("entrer le montant que cous coulez ajouter :"))


cl1 = Client("1300","ahmed","adr")
c1 = Compte(nom,montant1,cl1)

cl1.affiche()
if montant1 >= 0 :
    c1.crediter(montant1)
    c1.afficher()
elif montant1 < 0 and solde>montant1:
    c1.debiter(montant1)
    c1.afficher()




# nom="ayoub ouahidi"
# matricule= "1234567"
# adresse=" lot koutobia "
# cl1= Client(matricule,nom,adresse)
# cl1.affiche()
    