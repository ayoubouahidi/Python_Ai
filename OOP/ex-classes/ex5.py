from collections import deque
from collections import OrderedDict,Counter
import datetime
class Fournisseur:
    def __init__(self,code,adresse,nomCom):
        self.__code=code
        self.__adresse=adresse
        self.__nomCom=nomCom
    
    @property
    def Code(self):
        return self.__code
    @property
    def Adresse(self):
        return self.__adresse
    @property
    def NomCom(self):
        return self.__nomCom
    
    @Code.setter
    def Code(self,a):
        self.__code=a
    @Adresse.setter
    def Adresse(self,b):
        self.__adresse=b
    @NomCom.setter
    def NomCom(self,c):
        self.__nomCom=c

    def __str__(self):
        return f"code de fourniseur : {self.__code} adresse : {self.__adresse} nomCom : {self.__nomCom}"

class Ordinateur :
    def __init__(self,code,marque,dateachat,prix,fr):
        self.__code=code
        self.__marque=marque
        self.__dateachat=dateachat
        self.__prix=prix
        self.__fournisseur=fr
    
    @property
    def Code(self):
        return self.__code
    @property
    def Marque(self):
        return self.__marque
    @property
    def dateachat(self):
        return self.__dateachat
    @property
    def prix(self):
        return self.__prix
    @property
    def fournisseur(self):
        return self.__fournisseur
    

    @Code.setter
    def Code(self,a):
        self.__code=a

    @Marque.setter
    def Marque(self,a):
        self.__marque=a
    @dateachat.setter
    def dateachat(self,a):
        self.__dateachat=a
    @prix.setter
    def prix(self,a):
        self.__prix=a
    @fournisseur.setter
    def fournisseur(self,a):
        self.__fournisseur=a
    
    def __str__(self):
        return f"code :  {self.__code} marque : {self.__marque} prix : {self.__prix} date {self.__dateachat} fournisseur {self.__fournisseur.__str__()}"
    
listF = deque()
for i in range(5):
    A1 = Fournisseur((i+1),"adr"+str(i+1),"f"+str(i+1))

    listF.appendleft(A1)
for F in listF:
    print(F)

# A2 = Ordinateur("C","M","DATE","PRIX",A1)

Ordinateur_DIC = OrderedDict()
# o = Ordinateur(1,"MA","22/22/22",1000*i,listF)
# for i in range(3):
#     x = i if i<5 else 5-i
#     code = int(input("donner le code : "))
    
#     o = Ordinateur(code,"MA","22/22/22",1000*(i+1),listF[x])
    # Ordinateur[code]=o
    # Ordinateur[i+1]=o
    
for i in range(10):
    x = i if i < 5 else 5 - i
    code = int(input("donner le code : "))

    o = Ordinateur(code, "MA", "22/22/22", 1000 * (i + 1), listF[x])
    Ordinateur_DIC[code] = o

    Ordinateur_DIC[i+1]=o

for k in Ordinateur_DIC.keys():
    if Ordinateur_DIC[k].prix<5000:
     print(Ordinateur_DIC[k])


d={}
for k in Ordinateur_DIC.keys():
    d[k] = Ordinateur_DIC[k].fournisseur.Code
print(d)

c = Counter(d.values())
print(c)









