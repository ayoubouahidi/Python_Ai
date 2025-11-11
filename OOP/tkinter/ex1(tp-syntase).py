from abc import ABC, abstractmethod

class Personne(ABC):
    def __init__(self, num_pers, nom_complet_pers, adresse, tel):
        self.__num_pers = num_pers
        self.__nom_complet_pers = nom_complet_pers
        self.__adresse = adresse
        self.__tel = tel

    @property
    def num_pers(self):
        return self.__num_pers
    
    @num_pers.setter
    def num_pers(self, num_pers):
        self.__num_pers = num_pers
    
    @property
    def nom_complet_pers(self):
        return self.__nom_complet_pers
    
    @nom_complet_pers.setter
    def nom_complet_pers(self, nom_complet_pers):
        self.__nom_complet_pers = nom_complet_pers
    
    @property
    def adresse(self):
        return self.__adresse
    
    @adresse.setter
    def adresse(self, adresse):
        self.__adresse = adresse
    
    @property
    def tel(self):
        return self.__tel
    
    @tel.setter
    def tel(self, tel):
        self.__tel = tel

    @abstractmethod
    def affiche(self):
        pass


