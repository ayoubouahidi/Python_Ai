class Personne:
    def _init_(self, cin, nom_complet, date_naissance):
        self.cin = cin
        self.nom_complet = nom_complet
        self.date_naissance = date_naissance

    def get_cin(self):
        return self.cin

    def get_nom_complet(self):
        return self.nom_complet

    def get_date_naissance(self):
        return self.date_naissance

    def set_cin(self, new_cin):
        self.cin = new_cin

    def set_nom_complet(self, new_nom_complet):
        self.nom_complet = new_nom_complet

    def set_date_naissance(self, new_date_naissance):
        self.date_naissance = new_date_naissance

    def affiche(self):
        print(f"CIN: {self.cin}, Nom complet: {self.nom_complet}, Date de naissance: {self.date_naissance}")

# Exemple d'utilisation
personne1 = Personne("12345", "John Doe", "01/01/1990")
personne1.affiche()
