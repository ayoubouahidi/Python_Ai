class Client:
    def __init__(self, ma, nc, ad):
        self.__matricule = ma
        self.__nomComplet = nc
        self.__adresse = ad

    @property
    def Matricule(self):
        return self.__matricule

    @Matricule.setter
    def Matricule(self, c): 
        self.__matricule = c

    @property
    def NomCompte(self):
        return self.__nomComplet

    @NomCompte.setter
    def NomCompte(self, c): self.__nomComplet = c

    @property
    def Adresse(self):
        return self.__adresse

    @Adresse.setter
    def Adresse(self, c): self.__adresse = c

    def affiche(self):
        print(f"matricule: {c.Matricule} \nNom complet: {c.NomCompte} \nAdresse: {c.Adresse}")

class Compte:
    def __init__(self, num, solde, cl):
        self.__numCompte = num
        self.__solde = solde
        self.__client = cl
# GETTERS

    def getNumCompte(self):
        return self.__numCompte

    def getSolde(self):
        return self.__solde

# SERTTERS
    def setNumCompte(self, o):
        self.__numCompte = o

    def setSolde(self, o):
        self.__solde = o

# DEPOSER
    def crediter(self, c1, montant):
        c1.__solde -= montant
        self.__solde += montant

    def crediter2(self, montant):
        self.__solde += montant

# TIRER

    def debiter(self, c1, montant):
        if self.__solde > montant:
            c1.__solde += montant
            self.__solde -= montant
        else:
            print("IMPOSSIBLE!!")

    def debiter1(self, montant):
        if self.__solde > montant:
            self.__solde -= montant
        else:
            print("IMPOSSIBLE!!")
# AFFICHE

    def affiche(self):
        print(
            f"matricule: {c.Matricule} \nNom complet: {c.NomCompte} \nAdresse: {c.Adresse} \nNum: {self.__numCompte} \nsolde: {self.__solde}DH")

    def affiche(self):
        self.affiche()
        print( f" Num: {self.__numCompte} \nsolde: {self.__solde}DH")
        
c = Client(2, 'amin', "quartier anass")
z = Compte(9956, 5000, c)
z.affiche()
z1 = Compte(4444, 2000, c)
# z1.crediter(z, 500)
# print(z.getSolde())
# print(z1.getSolde()).
z1.debiter(z, 11500)
print(z.getSolde())
print(z1.getSolde())
