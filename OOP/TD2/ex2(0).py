from abc import ABC, abstractmethod

class IPersonne(ABC):
    @abstractmethod
    def affiche(self):
        pass

    @abstractmethod
    def calculerSalaire(self):
        pass


class Personne(IPersonne):
    def __init__(self, nom, prenom, date_naissance, salaire):
        self.nom = nom
        self.prenom = prenom
        self.date_naissance = date_naissance
        self.salaire = salaire

    def affiche(self):
        return f"Je suis {self.nom} {self.prenom} né le {self.date_naissance} mon salaire est {self.salaire} dh"

    def calculerSalaire(self):
        return self.salaire

class Profil(Personne):
    def __init__(self, nom, prenom, date_naissance, salaire, poste):
        super().__init__(nom, prenom, date_naissance, salaire)
        self.poste = poste

# Test Program
personne1 = Personne("SAlMI", "Karim", "02 juin 1970", 20000)
personne2 = Profil("Nom2", "Prenom2", "01 janv 1990", 15000, "Poste2")

print(personne1.affiche())
print(personne2.affiche())
####*************ex2

from abc import ABC, abstractmethod

class IOperation(ABC):
    @abstractmethod
    def plus(self, *args):
        pass

    @abstractmethod
    def moins(self, *args):
        pass

class IAffichage(ABC):
    @abstractmethod
    def affiche(self):
        pass


class Complexe(IOperation, IAffichage):
    def __init__(self, partie_reelle, partie_imaginaire):
        self.partie_reelle = partie_reelle
        self.partie_imaginaire = partie_imaginaire

    def plus(self, autre):
        return Complexe(self.partie_reelle + autre.partie_reelle, self.partie_imaginaire + autre.partie_imaginaire)

    def moins(self, autre):
        return Complexe(self.partie_reelle - autre.partie_reelle, self.partie_imaginaire - autre.partie_imaginaire)

    def affiche(self):
        return f"{self.partie_reelle} + {self.partie_imaginaire}i"

class Reel(Complexe):
    def plus(self, *args):
        return Reel(self.partie_reelle + sum(args), self.partie_imaginaire)

    def moins(self, *args):
        return Reel(self.partie_reelle - sum(args), self.partie_imaginaire)

# Test Program
complexe1 = Complexe(4, 3)
complexe2 = Complexe(2, 1)

reel1 = Reel(10, 0)
reel2 = Reel(5, 0)

print(complexe1.plus(complexe2).affiche())
print(reel1.plus(2, 3, 4).affiche())



