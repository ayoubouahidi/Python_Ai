class Stagiere :
    t =[]
    def __init__(self,matricule="0000",nom="le nom ",prenom="le prenom",filiere="filiere",note1=0,note2=0,note3=0):
        self.__matricule=matricule
        self.__nom=nom
        self.__prenom=prenom
        self.__filiere=filiere
        self.__note1=note1
        self.__note2=note2
        self.__note3=note3

#GETTERS

    def getMatricule(self):
        return self.__matricule
    def getNom(self):
        return self.__nom
    def getPrenom(self):
        return self.__prenom
    def getFiliere(self):
        return self.__filiere
    def getNote1(self):
        return self.__note1
    def getNote2(self):
        return self.__note2
    def getNote3(self):
        return self.__note3

#SETTERS
    def setMatricule(self,a):
        self.__matricule=a
    def setNom(self,b):
        self.__nom=b
    def setPrenom(self,c):
        self.__prenom=c
    def setFILIERE(self,d):
        self.__filiere=d
    def setNote1(self,e):
        self.__note1=e
    def setNote2(self,f):
        self.__note1=f
    def setNote2(self,g):
        self._note2=g
    def setNote3(self,h):
        self.__note3=h
    

    def check(self):
        if self.__note1 < 0:
            self.__note1=0
        if self.__note2< 0 :
            self.__note2 =0
        if self.__note3 < 0:
            self.__note3 = 0

    def equal(self,s):
        return self.__matricule==s.__matricule
    
        
    def CALCUL(self):
        return (self.__note1 + self.__note2 + self.__note3)/3
    
    def afficher(self):
        print(f"le matricule est {self.__matricule} le nom est {self.__nom} le prenom est {self.__prenom} la filiere est {self.__filiere} les notes sont {self.__note1} ; {self.__note2} ; {self.__note3}; la moyenne generale est {self.CALCUL()} ")
    


    




#objet
# ma = input("entrer matr")
# name = input("entrer le nom ")
# secondename = input("entrer le prenom ")
# filiere = input("entrer filiere")
# no1 =int(input("entrer note 1"))
# no2 = int(input("entrer note2 "))
# no3 = int(input("entrer note 3"))

s1 = Stagiere("1","karami","said","dd")
s1.check()
s1.afficher()
s2=Stagiere("2","karami","said","dd",12,15,14)
s2.check()
s2.afficher()
s3=Stagiere("3","karami","said","dd",11,16,17)
s3.check()
s3.afficher()
s4 = Stagiere("4","salmi","said","ii")
s4.check()
s4.afficher()



s0 = Stagiere()
s0.setMatricule("b1212")
s0.setNom("lool")
s0.setPrenom("c'est du test")
s0.setFILIERE("sc.math")
s0.setNote1(12)
s0.setNote2(-2)
s0.setNote3(20)

re =s1.equal(s2)

if re:
    print("les matricules sont les memes ")
else: 
    print("les matricules sont differents ")

