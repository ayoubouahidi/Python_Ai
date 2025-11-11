from abc import ABC, abstractmethod

class Comparable(ABC):
    @abstractmethod
    def compareNum(self, o):
        pass

    @abstractmethod
    def salaireCompare(self,o):
        pass

class Personne(Comparable):
    def __init__(self, num_pers, salaire):
        self.__num_pers = num_pers
        self.__salaire = salaire

    def compareNum(self, o):
        return self.__num_pers == o.__num_pers

    def salaireCompare(self, p):
        if self.__salaire < p.__salaire:
            return -1
        elif self.__salaire == p.__salaire:
            return 0
        else:
            return 1


