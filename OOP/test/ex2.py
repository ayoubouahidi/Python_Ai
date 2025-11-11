class client:
    def __init__(self,matricule,nom,adresse):
        self.__matricule = matricule
        self.__nomComplet = nom 
        self.__adresse = adresse
        
    def getMatricule(self):
        return self.__matricule
    def getNomcomplet(self):
        return self.__nomComplet
    def getAdresse(self):
        return self.__adresse
    
    def setMatricule(self,matricule):
        self.__matricule = matricule
    def setNomcomplet(self,nom):
        self.__nomComplet = nom
    def setAdresse(self,adresse):
        self.__adresse = adresse
        
    def affiche(self):
        print(f'le matricule : {self.__matricule}\nla nom : {self.__nomComplet}\nl\'adresse{self.__adresse}')

class Cmpte:
    def __init__(self,cmp,s,cl1):
        self.__numCmpte = cmp
        self.__solde = s
        self.__client= cl1
        
    def getNumcmpte(self):
        return self.__numCmpte
    def getSolde(self):
        return self.__solde
    def getClient(self):
        return self.__client
    
    def setNumcmpte(self,cmp):
        self.__numCmpte = cmp
    def setSolde(self,s):
        self.__solde = s
    def setClient(self,cl1):
        self.__client = cl1
        
    def crediter(self,montant):
        self.setSolde(self.getSolde() + montant)
        
    def debiter(self,montant):
        if(self.__solde > montant):
            self.setSolde(self.getSolde() - montant)
        else:
            print("le dibit est plus grand que votre solde!")

    def affiche(self):
        print(f'numCmpte : {self.__numCmpte}\nSolde : {self.__solde}\n client : {self.__client.affiche()}')
        
cmp = input("Donnez votre numCmpte : ")
s = int(input("Donnez votre solde : "))
montant = int(input("Donnez le montant : "))
matricule = input("Donnez le matricule : ")
nom = input("Donnez le nom complet : ")
adresse = input("Donnez l'adresse : ")

cl1 = client(matricule,nom,adresse)
c1 = Cmpte(cmp,s,cl1)
c1.crediter(montant)
c1.affiche()
c1.debiter(montant)
c1.affiche()