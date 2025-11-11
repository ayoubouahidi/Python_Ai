class Stagieaire:
    def __init__(self,matricule="xxx",nom="yyy",prenom="zzz",nt=[]):
        self.__Matricule=matricule
        self.__Nom=nom
        self.__Prenom=prenom
        self.__Notes=nt
        
    def getmatricule(self):
        return self.__Matricule
    def getnom(self):
        return self.__Nom
    def getprenom(self):
        return self.__Prenom
    # def getnote1(self):
    #     return self.__Note1
    # def getnote2(self):
    #     return self.__Note2
    # def getnote3(self):
    #     return self.__Note3
    def getnotes(self):
        return self.__Notes
    
    

    def setmatricule(self,matricule):
        self.__Matricule=matricule
    def setnom(self,nom):
        self.__Nom=nom
    def setprenom(self,prenom):
        self.__Prenom=prenom
    # def setnote1(self,note1):
    #     self.__Note1=note1
    # def setnote2(self,note2):
    #     self.__Note2=note2
    # def setnote3(self,note3):
    #     self.__Note3=note3
    def setnotes(self,b):
        self.__Notes=b

    def equal(self,S):
        return self.__Matricule==S.__Matricule
    
    

    
    def afficher(self):
        print(f"le matricule est : {self.__Matricule}le nom est : {self.__Nom}  et le prenom est : {self.__Prenom} ")
    def affiche (self):
        for i in range(len(self.__Notes)):
            print(self.__Notes[i])

    # def check(self): #
    #     if self.__Note1 < 0 :
    #        self.setnote1(0)
        
    #     if self.__Note2 < 0:
    #          self.setnote2(0)
        
    #     if self.__Note3 < 0:
    #        self.setnote3(0)

    def checkTableau(self):
     for i in range(len(self.__Notes)):
        if self.__Notes[i] < 0 :
            self.__Notes[i] = 0 

           
           
    #def calcul(self ,&moy):
        #moy = (self.__Note1+self.__Note2+self.__Note3)/3
     

    # def calcul(self):
    #     m=(self.__Note1+self.__Note2+self.__Note3)/3
    #     return m 
    def moyenne(self):
        s = 0 
        for i in range(len(self.__Notes)):
            s = s + self.__Notes[i]
        return s
    


    
    
           
              


matricule=int(input("entrer le matricule :"))
nom=input("enter le nom : ")
prenom=input("enter le prenom : ")
L=[]
n=int(input("Donner le nombre de notes :"))
print("Donner les notes :")

for i in range(n):
  L.append(float(input()))
p1=Stagieaire(matricule,nom,prenom,n)
p1.setnotes(L)

p1.checkTableau()
print("le moyenne est : ",p1.moyenne())
p1.afficher()
p1.affiche()
# print("le moyenne est :",p1.calcul())



# matricule=int(input("entrer le matricule :"))
# nom=input("enter le nom : ")
# prenom=input("enter le prenom : ")
# note1=float(input("entrer la note "))
# note2=float(input("entrer la note "))
# note3=float(input("entrer la note "))


# p2=Stagieaire(matricule,nom,prenom,note1,note2,note3)
# p2.check()
# p2.calcul()
# p2.afficher()
# print("le moyenne est :",p1.calcul())


# p3=Stagieaire(matricule,nom,prenom,note1,note2,note3)

# x=p1.equal(p2)
# if x:
#     print("les matricules sont identique .")
# else:
#     print("ne sont pas identique ")
# for i in range(3):
#     print(p3.afficher())

