class Personne:
    def __init__(self, c, n, p):
        self._code = c
        self._nom = n
        self._prenom = p

    @property
    def Code(self):
        return self._code
    @Code.setter
    def Code(self, p): self._code = p

    @property
    def Nom(self):
        return self._nom
    @Nom.setter
    def Code(self, p): self._nom = p

    @property
    def Prenom(self):
        return self._prenom
    @Prenom.setter
    def Code(self, p): self._prenom = p

    def affiche(self):
        print(f"Code: {self.Code}\nNom: {self.Nom}\n Prenom: {self.Prenom}")


class Professeur(Personne):
    def __init__(self, c, n, p, d, s):
        super().__init__(c, n, p)
        self.__diplome = d
        self.__specialite = s

    @property
    def Diplome(self):
        return self.__diplome
    @Diplome.setter
    def Diplome(self, p):  self.__diplome = p

    @property
    def Specialite(self):
        return self.__specialite
    @Specialite.setter
    def Specialite(self, p):  self.__specialite = p

    def affiche(self):
        super().affiche()
        print(f"Diplome: {self.Diplome} \nSpecialiste: {self.Specialite}")


class Eleve(Personne):
    def __init__(self, c, n, p, se, nbr):
        super().__init__(c, n, p)
        self.__section = se
        self.__nbrjourA = nbr

    @property
    def Section(self):
        return self.__section
    @Section.setter
    def Section(self, e): self.__section = e

    @property
    def NbrjourA(self):
        return self.__nbrjourA
    @NbrjourA.setter
    def NbrjourA(self, e): self.__nbrjourA = e

    def nbrjourabsence(self):
        self.NbrjourA += 1

    def affiche(self):
        super().affiche()
        print(
            f"Section: {self.Section}\nNombre de jour abssence: {self.NbrjourA}")


class Salarie(Personne):
    def __init__(self, c, n, p, ph, nbrh):
        super().__init__(c, n, p)
        self.__prixheure = ph
        self.__nbreheure = nbrh

    @property
    def Prixheure(self):
        return self.__prixheure
    @Prixheure.setter
    def Prixheure(self, s): self.__prixheure = s

    @property
    def Nbreheure(self):
        return self.__nbreheure
    @Nbreheure.setter
    def Nbreheure(self, s): self.__nbreheure = s

    def salaire(self):
        salaire = self.Prixheure * self.Nbreheure
        return salaire

    def affiche(self):
        super().affiche()
        print(
            f"Prix heure: {self.Prixheure}DH\nNombre heure: {self.Nbreheure}h\n votre salaire: {self.salaire()}DH")


# P = Personne(1111, 'test', 'test')
# PR = Professeur(2222, 'test', 'test', 'DD', 'DM')
# E = Eleve(3333, 'test', 'test2', 'TEST3', 5)
# S = Salarie(4444, 'test', 'test', 300, 50)

# P.affiche()
# PR.affiche()
# E.nbrjourabsence()
# E.affiche()
# S.salaire()
# S.affiche()

co = int(input("saisir le code: "))
no = input("saisir nom: ")
pr = input("saisir prenom: ")
P = Personne(co, no, pr)
# P.affiche()
PR = Professeur(co, no, pr, 'BAC+3', 'DEV DEGITAL')
# PR.affiche()
# E = Eleve(co, no, pr, 'S1', 3)
# E.affiche()
# E.nbrjourabsence()
# E.affiche()
# S = Salarie(co, no, pr, 200, 30)
# S.affiche()
# print(S.salaire())
# PR.Diplome = 'Ingenieur'
# PR.Specialite = 'Full Stack'
# print(PR.Diplome)
# print(PR.Specialite)
# PR.affiche()

PR = P          # polymorphisme
P.affiche()
PR.affiche()
P = PR          # polymorphisme
P.affiche()
PR.affiche()