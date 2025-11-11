from abc import ABC , abstractmethod
class Comparable(ABC):
    @abstractmethod
    def compareNum(self):
        pass
    @abstractmethod
    def salaireCompare(self):
        pass
    