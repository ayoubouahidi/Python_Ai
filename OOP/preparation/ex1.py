class Adresse:
    def __init__(self,Num,Rue,Ville,CodePostal):
        self.__num = Num 
        self.__Rue = Rue
        self.__Ville =Ville
        self.__code= CodePostal

        #getters

    @property
    def Num(self):
        return self.__num
    @property
    def Rue(self):
        return self.__Rue
    @property
    def Ville(self):
        return self.__Ville
    @property
    def Code(self):
        return self.__code
    
    #setter

    @Num.setter
    def Num(self,a):
         self.__num=a
    @Rue.setter
    def Rue(self,a):
         self.__Rue=a
    @Ville.setter
    def Ville(self,a):
        self.__Ville= a
    @Code.setter
    def code(self,a):
        self.__code= a

    #fonctions 
        
    def __str__(self):
        return f'le num :{self.__num} la rue est {self.__Rue} la ville est {self.__Ville} le code est {self.__code}'
#creation objet 
adr1 = Adresse(1,1,'safi',1)
print(adr1.__str__())
    
