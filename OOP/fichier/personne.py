from abc import ABC, abstractmethod
import re 
class Personne(ABC):
    def __init__(self,num,nom,adresse,tel):
        if re.match(r"^N[0-9]{6}$",str(num)) :
           self._NumPers = num
        else :
            raise ValueError("le numero doit commencer Par N suivi de 6 chiffres")
        
        if re.match(r"^[A-Za-z\s]+$",str(nom)) :
            self._NomCompletPers = nom
        else :
            raise ValueError("le nom complet doit etre des caracteres")

        self._Adresse = adresse 

        if re.match(r"^(\+212)\d{8}$",str(tel)) :
            self._Tel = tel
        else :
            raise ValueError("le tel doit commencer par 212 suivi 8 chiffres")

    # Accesseurs
    # def get_NumPers(self): return self._NumPers
    @property
    def Numpers(self): return self._NumPers
    
    def get_NomCompletPers(self) : return self._NomCompletPers
    def get_Adresse(self) : return self._Adresse
    def get_Tel(self) : return self._Tel

    # Modificateurs
    def set_NumPers(self,n) : 
        if re.match(r"^N[0-9]{6}$",str(n)) :
           self._NumPers = n
        else :
           raise ValueError("le numero doit commencer Par N suivi de 6 chiffres")
      
    def set_NomCompletPers(self,c) : 
        if re.match(r"^[A-Za-z\s]+$",str(c)) :
            self._NomCompletPers = c
        else :
            raise ValueError("le nom complet doit etre des caracteres")
      
    def set_Adresse(self,a) : self._Adresse = a 
    def set_Tel(self,t) : 
        if re.match(r"^(\+212)\d{8}$",t) :
            self._Tel = t
        else :
            raise ValueError("le tel doit commencer par 212 suivi 8 chiffres")

    @abstractmethod
    def affiche(self): pass


