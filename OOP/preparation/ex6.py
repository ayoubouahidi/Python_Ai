import re
class Adresse:
    def __init__(self,Num,Rue,Ville,CodePostal):
        self.__Num = Num 
        self.__Rue = Rue
        self.__Ville =Ville
        if re.match(r"^\d{5}$",str(CodePostal)):
            self.__CodePostal = CodePostal
        else:
            raise ValueError("code postal incorrect")
        
    @property
    def Num(self): return self.__Num
    @Num.setter
    def Num(self,num) : self.__Num = num

    @property
    def Rue(self): return self.__Rue
    @Rue.setter
    def Rue(self,rue): self.__Rue = rue

    @property
    def Ville(self):return self.__Ville
    @Ville.setter
    def Ville(self,ville): self.__Ville = ville

    @property
    def CodePostale(self) : return self.__CodePostale
    @CodePostale.setter
    def Codepostale(self,a):
     if re.match(r"^\d{5}$",str(a)):
        self.__CodePostal=a
     else:
        raise ValueError("code postal")