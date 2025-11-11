class DateNaissance:
    def __init__(self,jours,mois,annee):
        self.__jours=jours
        self.__mois=mois 
        self.__annee=annee
    def affiche(self):
        print(f'{self.__jours}/{self.__mois}/{self.__annee}')
    
    @property
    def Jours(self):
        return self.__jours
    @property
    def Mois(self):
        return self.__mois
    @property
    def Annee(self):
        return self.__annee
    @Jours.setter
    def Jours(self,j):
        self.__jours=j
    @Mois.setter
    def Mois(self,m):
        self.__mois=m
    @Annee.setter
    def Annee(self,a):
        self.__annee=a
class Employe:
    def __init__(self,matricule,nom,prenom,datenaissance):
        self._matricule=matricule
        self._nom=nom
        self._prenom=prenom
        self._datenassance=datenaissance
    def affiche(self):
        print(f'Matricule :{self._matricule}\nle nom :{self._nom}\nprenom :{self._prenom}\ndate de naissance: ') 
        self._datenassance.affiche()
class Cadre(Employe):
    def __init__(self,matricule,nom,prenom,datenaissance,i):
        super().__init__(matricule,nom,prenom,datenaissance)
        self.__indice=i
    @property
    def Indice(self):
        return self.__indice
    @Indice.setter
    def Indice(self,i):
        self.__indice=i

    def getsalaire(self):
        match self.__indice:
            case 1:
                print("20000 Dh")
            case 2:
                print("25000 Dh")
            case 3:
                print("30000 Dh")
            case 4:
                print("35000 Dh")
            case _:
                print("Tapez entre 1 et 4")
    def affiche(self):
        super().affiche()
        print(f'Indice: {self.__indice} salaire: {self.getsalaire()}')
class Patron(Employe):
    def __ini__(self,matricule,nom,prenom,datenaissance,pourcentage,chifreaffaiare):
        super().__init__(matricule,nom,prenom,datenaissance)
        self.__pourcentage=pourcentage
        self.__chifreaffaire=chifreaffaiare
    def Salaire(self):
        return (self.__pourcentage * self.__chifreaffaire)/100
    def affiche(self):
        super().affiche()
        print(f'pourcentage: {self.__pourcentage} chifreaffaire:{self.__chifreaffaire} \n salaire:{self.Salaire()}')

d=DateNaissance(10,2,2000)
d.affiche()
c1=Cadre("mat47","dagdague","soufiane",d,3)
c1.affiche()