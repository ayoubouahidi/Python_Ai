from collections import*

# class grp:
#     def __init__(self,liste):
#         self.__liste=liste
    
#     def getList(self):
#         return self.__liste
#     def setList(self,a):
#         self.__liste=a

#     def transform(self):
#         return self.__liste=deque()
#     def AjustStp(self,x):
#         return .append(x)
        
#     def Supprimer(self,i):
       
#     def Affiher(self):
#         print(f"pour l'ajout {self.AjustStp()} pour suppression {self.Supprimer()} ")

    
        



    

        
    


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
    def setmatricule(self,a):self.__matricule=a
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
    def nbreStagiaire(cls):return Stagiaire.cpt

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

    def affiche(self):
        # return( "Matricule :"+str(self.__matricule)+"\tNom:\t"+str(self.__nom ))
        return f"mat: {self.__matricule} ,nom   :    {self.__nom}"


class GroupeS:
    def __init__(self):
        self.__liste=[]
    
    def getList(self):
        return self.__liste
    def setList(self,a):
        self.__liste=a

    def Ajout(self,a):
        self.__liste.append(a)
        
    def RecherchV3(self,matricule):
        for v in range(len(self.__liste)):
            if self.__liste[v].getMatricule() == matricule:
                return v
            else:
                return len(self.__liste)+1
            
    def rechercheparobjet(self,stg):
        for k in range(len(self.__liste)):
            if self.__liste[k] == stg:
                return self.__liste[k]
            return 'NULL'
        

    # def Recherche(self,m):
    #     for k in range(len(self.__liste)):
    #         if self.__liste[k].getMatricule() == m:
    #             return k
            
    #     return len(self.__liste[k])+1
    

    # def Recherchv2(self,m):
    #     for k, stagiaire in enumerate(self.__liste):
    #        if stagiaire.getMatricule() == m:
    #           return k
    #        return 'NULL'

    # def rechercheV2(self,st):
    #     for k in range(len(self.__liste)):
    #         if self.__liste[k] == st:
    #             return self.__liste[k]
    #         return 'NULL'
        
    def Ajoutv1(self,m):
        o1=self.rechercheparobjet(m)
        if o1=='NULL':
            self.__liste.append(o1)
        else:
            print("deja , existe ")


    # def modification(self,M):
    #     A1=self.Recherche(M)
    #     A1.setmatricule("new one ")

    # def recherchev3(self,st):
    #     for k in range(len(self.__liste)):
    #         if self.__liste[k] == st:

    #             return k
    #         return -1
    # def supprimer(self,m):
    #     pos = self.Recherche(m)
    #     if pos < len(self.__liste):
    #        self.__liste.pop(pos)

    def suprrimerDE(self,m):
        pos = self.RecherchV3(m)
        if pos < len(self.__liste):
               self.__liste.pop(pos)
               
               

            #  for pos in range(len(self.__liste)-1):
              
            
            #      self.__liste[pos]=self.__liste[pos+1]
              


    def Afficher(self):
        for item in self.__liste:
            print(item.affiche())   
    

    
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
# print(s1.equals(s2)) ## pour verifier la valeur de matricule
# print(s1.get__Matricule()) ##accessseur
# print(s1.notes)   ## property
# print(s2.get__Matricule())
# print(s2.notes)
# print("La moyenne de 1er stagiaire ",s1.moyenne())
# print("La moyenne de 2eme stagiaire ",s2.moyenne())
# s1.affiche()
# s2.affiche()
# del s1
# print(s2.matricule) ## probleme car s1 est détruit
# print(Stagiaire.nbreStagiaire())



A1=GroupeS()
A1.Ajout(s1)

A1.Ajout(s2)

A1.RecherchV3(1)
A1.suprrimerDE(1)
# A1.rechercheparobjet(s1)
# A1.Ajoutv1(A1)
# A1.Ajoutv1(1)
A1.Afficher()
# A1.Ajout(s1)
# A1.modification(s1)

# A1.supprimer(s2.getMatricule())
# A1.Afficher()
# A1.modification(s1)










   

    



    
