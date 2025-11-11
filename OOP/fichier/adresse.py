import re

class Adresse :
   def __init__(self,num,rue,ville,codePostale):
     self.__Num = num
     self.__Rue = rue
     self.__Ville = ville
     if re.match(r"^\d{5}$",str(codePostale)) :
        self.__CodePostale = codePostale
     else : 
        raise ValueError("code postale")
       
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
   def CodePostale(self,code) : 
     if re.match(r"^\d{5}$",str(code)) :
        self.__CodePostale = code
     else : 
        raise ValueError("code postale")

   def __str__(self):
       return f"Num : {self.__Num} Rue : {self.__Rue} Ville : {self.__Ville} Code Postale : {self.__CodePostale}"

