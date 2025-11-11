from abc import ABC, abstractmethod

class Comparable(ABC):
    @abstractmethod
    def compareTO(self):pass
class Impribale(ABC):
   @abstractmethod
   def imprimer(self):pass

class Peronne(Comparable,Impribale):
    def __init__(self,age,cin):
        self.__age=age
        self.__cin=cin

    def getage(self):
        return self.__age
    def getCin(self):
        return self.__cin
    
    def setage(self,a):
        self.__age=a
    def setcin(self,a):
        self.__cin=a
    
    def compareTO(self,w):
       if  self.__age <  w.__age:
         return "le deuxiemme est le plus age"
       elif self.__age> w.__age:
        return  "le premier est le plus age"
       else:
          return print("sont egal")
    def imprimer(self):
       print(f"age : {self.__age} comparison est {self.compareTO(c2)}")
    

    
class Outil(Comparable,Impribale):
   def __init__(self,lang):
      self.__lang=lang
    
   def getlang(self):
        return self.__lang
   
   def setlang(self,b):
      self.__lang=b
      
   def compareTO(self,w):
      if  self.__lang <  w.__lang:
         return "le deuxiemme est le plus lang"
      elif  self.__lang >  w.__lang:
        return  "le premier est le plus lang"
      else: print(" sont egal")

   def imprimer(self):
       print(f"age : {self.__lang} comparison est {self.compareTO()}")

      
c1=Peronne(21,21)
c2=Peronne(20,20)
c1.imprimer()
# print(c2.compareTO(c1))

o1=Outil(10)


    








        