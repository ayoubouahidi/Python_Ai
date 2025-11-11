class Personne:
    def __init__(self,co="personne",nom="ayou",prenom="ayou"):
        self._Code=co
        self._nom=nom
        self._prenom=prenom
    def getCode(self):
        return self._Code
    

    @property
    def Code(self):
        return self._Code
    @property
    def nom(self):
        return self._nom
    @property
    def prenom(self):
        return self._prenom
    

    @Code.setter
    def Code(self,c):
        self._Code=c

    @nom.setter
    def nom(self,a):
        self._nom=a

    @prenom.setter
    def prenom(self,b):
        self._prenom=b


    
    def f1(self,x=0):
        print("function",x)


    def affiche(self):
        print(f"le code est {self.Code} ; le nom est {self.nom}; le prenom est {self.prenom}")

    
class Professeur(Personne):
    def __init__(self,co="professeur",nom="ayoub",prenom="oiahidi",di="math",spe="math"):
       super().__init__(co,nom,prenom)  #dans le cas du champs prive 
       self._diplome=di
       self._specialite=spe


   


    def affiche(self):
        # super().affiche() #dans le cas du champs prive 
        print(f"le code est {self._Code} ; le nom est {self._nom}; le prenom est {self._prenom} le diplome est {self._diplome}; specialite {self._specialite}")



class Eleve(Personne):
    def __init__(self,co="ayoub",nom="ayoub",prenom="ayoub",section="ayoub",nbrjous=20):
        super().__init__(co,nom,prenom)
        self.__section=section
        self.__nbrjous=nbrjous

    def nbrjours(self):
        return self.__nbrjous + 1    

    def affiche(self):
        super().affiche()
        print(f" la section {self.__section};nbrjours {self.__nbrjous}")
    
    

class Salarie(Personne):
    def __init__(self,co="ayoub",nom="ayoub",prenom="ayoub",nbrheur=20,prixheur=20):
        super().__init__(co,nom,prenom)
        self.__nbrheur=nbrheur
        self.__prixheur=prixheur

    def salaire(self):
        return self.__nbrheur * self.__prixheur
    

    def affiche(self):
        super().affiche()
        print(f"nombres des heures est {self.__nbrheur} est le prix par heur est {self.__prixheur}")

   
    

p1= Personne()
Personne.Code = "salwa"
p1.affiche()
# print(p1.Code)
# print(p1.getCode())

# p1.f1()

pro1=Professeur()
pro1.affiche()

# ele1 = Eleve()
# print("nombre des jours est: ",ele1.nbrjours())
# ele1.affiche()

# sal1 = Salarie()
# print("le salaire est ",sal1.salaire())
# sal1.affiche()


# p1 = pro1
# p1.affiche()
# pro1.affiche()

# pro1 = p1
# p1.affiche()
# pro1.affiche()


    









