
class ListEmploye:
    def __init__(self):
        self.__employes = []

    def recherche(self, num_pers):
        for employe in self.__employes:
            if employe.num_pers == num_pers:
                return employe
        return None
    
    def ajouterEmploye(self, employe):

        if not self.recherche(employe.num_pers):
            self.employes.append(employe)
            print("Employé ajouté avec succès.")
        else:
            print("Employé déjà existant.")

    def ajouterEmploye(self, employe):
        if not self.recherche(employe.num_pers):
            self.employes.append(employe)
            print("Employé ajouté avec succès.")
        else:
            print("L'employé existe déjà.")

    def modifierEmploye(self, num_pers):
        employe = self.recherche(num_pers)
        if employe:
            employe.salaire = new_salaire
            self.augmenter_salaire(employe)
            print("Salaire modifié avec succès.")
        else:
            print("Employé non trouvé.")

    def supprimerEmploye(self, num_pers):
        employe = self.recherche(num_pers)
        if employe:
            self.employes.remove(employe)
            print("Employé supprimé avec succès.")
        else:
            print("Employé non trouvé.")

liste_employes = ListEmploye()
l=[]
v=7
for i in range(1,v+1):
                
         l.append(i)
print(l)