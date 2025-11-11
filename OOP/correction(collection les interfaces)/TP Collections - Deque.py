from collections import deque

class Stagiaire:
    cpt=0  ## initialiser l'attribut de classe avec la valeur 0
    
##  def __init__(self,nom,prenom,filiere):
##        self.__nom=nom
##        self.__prenom=prenom
##        self.__filiere=filiere
##        Stagiaire.cpt +=1        #incrémenter l'attribut de la classe
##        self.__matricule=Stagiaire.cpt #affecter l'attribut matricule la valeur de compteur
##        self.__notes=[]
##        
    def __init__(self,nom,prenom,filiere,nts):
        self.__nom=nom
        self.__prenom=prenom
        self.__filiere=filiere
        Stagiaire.cpt +=1
        self.__matricule=Stagiaire.cpt
        self.__notes = nts

    ## accesseurs/getters
    def getMatricule(self):return self.__matricule
    def getNom(self):return self.__nom
    def getPrenom(self):return self.__prenom
    def getFiliere(self):return self.__filiere
    def getNotes(self):return self.__notes

    ## mutateurs/modificateurs/setters
    def setNom(self,n):self._nom=n
    def setPrenom(self,pr):self.__prenom=pr
    def setFiliere(self,f):self.__filiere=f
    def setNotes(self,nts):self.__notes=nts

    @property
    def matricule(self):return self.__matricule

    @property 
    def nom(self):return self.__nom
    @nom.setter
    def nom(self,n):self.__nom=n

    @property 
    def prenom(self):return self.__prenom
    @prenom.setter
    def prenom(self,p):self.__prenom=p

    @property
    def filiere(self):return self.__filiere
    @filiere.setter
    def filiere(self,f):self.__filiere=f
    
    @property
    def notes(self):return self.__notes
    @notes.setter
    def notes(self,nts):self.__notes=nts

    @classmethod  ## declarer une méthode de la classe
    def nbreStagiaire(cls):
        return Stagiaire.cpt

    def equals(self,s1):
        return self.__matricule == s1.__matricule

    def __del__(self):
        Stagiaire.cpt -=1

    def check(self):
        for i in range(len(self.__notes)):
            if self.__notes[i] < 0 :
                self.__notes[i] = 0
                
    def moyenne(self):
        if len(self.__notes)!=0:
         return sum(self.__notes)/len(self.__notes)
    
    def calcul(self):
        if len(self.__notes)!=0:
            for i in range(len(self.__notes)):
                s = s + self.__notes[i]
            return  s/len(self.__notes)

    def Affiche(self):
        print(f'Matricule :\t{self.__matricule}\tNom:\t{self.__nom}\tPrenom:\t{self.__prenom}\tNote:\t{self.__notes}')
        
    def __str__(self):
        return f'Matricule :\t{self.__matricule}\tNom:\t{self.__nom}\tPrenom:\t{self.__prenom}\tNote:\t{self.__notes}'
        
class Groupe:
    def __init__(self):
        self.__ListStagiaire = deque([])  #[]
    
    def Ajouter(self,s):
        self.__ListStagiaire.append(s)
        
    def getListStg(self):
        return self.__ListStagiaire

    def AfficheParValue(self):
        for x in self.__ListStagiaire:
             print(x)

    def AfficheParKey(self):
        for k in range(len(self.__ListStagiaire)):
            print(self.__ListStagiaire[k])

    def RechercheParMatricule(self,matr):
        for k in range(len(self.__ListStagiaire)):
            if self.__ListStagiaire[k].getMatricule() == matr:
                return k
            else:
                return self.__ListStagiaire.count(10) +1
            
    def RechercheParObjet(self,o):
        for k in range(len(self.__ListStagiaire)):
            if self.__ListStagiaire[k].getMatricule() == o.getMatricule():
              return self.__ListStagiaire[k]
            else:
              return 'NULL'

    def AjouteParVerif(self,s):
        o = self.RechercheParObjet(s)
        if o == 'NULL' :
           self.__ListStagiaire.append(s)
        else:
           print('Deja existe!')

    def SupprimerParMatricule(self, mat):
        pos = self.RechercheParMatricule(mat)
        if pos < len(self.__ListStagiaire) :
            del (self.__ListStagiaire[pos]) 
        else:
            print("La suppression est échouée") 
    
    def SupprimerParObjet(self,stg):
        o = self.RechercheParObjet(stg)
        if o != ['NULL']:
          self.__ListStagiaire.remove(stg)
        else :
          print("La suppression est échouée")
            
l1=[12.67,16,18]
l2=[13,15,14.75]
##l1=[]
##for i in range(4):
## l1.append(float(input("entrer les notes de la liste1:\t")))
##
##l2=[]
##for i in range(4):
## l2.append(float(input("entrer les notes de la liste2:\t")))
## 
s1=Stagiaire("Alami","Ahmed","DD",l1)
s2=Stagiaire("Bahi","Sara","DD",l2)
s3=Stagiaire('ggggg','hshshshsh','dd',[12,20,20])
s4=Stagiaire('Saki','Amine','ID',[13.50,15.25,16.75])
# print(s1.equals(s2)) ## pour verifier la valeur de matricule
# print(s1.getMatricule()) ##accessseur
# print(s1.notes)   ## property
# print(s2.getMatricule())
# print(s2.notes)
# print("La moyenne de 1er stagiaire ",s1.moyenne())
# print("La moyenne de 2eme stagiaire ",s2.moyenne())
# s1.affiche()
# s2.affiche()
# del s1
# print(s2.matricule) ## probleme car s1 est détruit
# print(Stagiaire.nbreStagiaire())


g=Groupe()
print('-- Ajouter Sans Verification  --')
g.Ajouter(s1)
g.Ajouter(s2)
# g.AfficheParValue()
g.AfficheParKey()
print("La position est: ",g.RechercheParMatricule(2))
print('-- Recherche Par Matricule --')
x= g.RechercheParMatricule(2)
if x < len(g.getListStg()):
  print("Stagiaire existe")
else:
  print("Stagiaire n'existe pas") 
g.AfficheParValue()
print('-- Recherche Par Objet --')
y=g.RechercheParObjet(s4)
if y != 'NULL':
  print("Stagiaire existe")
else:
  print("Stagiaire n'existe pas")
g.AfficheParKey()
print('-- Supprimer Par Matricule --')
g.SupprimerParMatricule(2)
g.AfficheParValue() 
print('-- -- Ajouter Apres Verification --')
g.AjouteParVerif(s4)
g.AfficheParValue() 
print('-- Ajouter Apres Verification  --')
g.AjouteParVerif(s3)
g.AfficheParValue() 
print('-- Supprimer Par Objet --')
g.SupprimerParObjet(s3)  
g.AfficheParValue() 