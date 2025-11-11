from collections import deque
class Article:
    def __init__(self,ref,des,qua,prixuni):
        self.__ref=ref
        self.__des=des
        self.__qua=qua
        self.__prixuni=prixuni
    #accesseure
    def getref(self):
        return self.__ref
    def getdes(self):
        return self.__des
    def getqua(self):
        return self.__qua
    def getprixuni(self):
        return self.__prixuni
    #modificateur
    def setref(self,a):
        self.__ref=a
    def setdes(self,b):
        self.__des=b
    def setqua(self,c):
        self.__qua=c
    def setprixuni(self,d):
        self.__prixuni=d

    #les autres methodes 

    def __str__(self):
        return f"reference est {self.__ref} la description est : {self.__des} , la quantite est {self.__qua} et le prix unitaire {self.__prixuni}"
    



class Stock:
    def __init__(self):
        self.__listeA=deque([])


    def getListA(self):
        return self.__listeA  
    def setListA(self,a):
        self.__listeA=a
    
    #les autres methodes 
    
    
    def RechercheArticle(self,ref):
        for i in range(len(self.__listeA)) :
            if self.__listeA[i].getref() == ref :
                return i
        return len(self.__listeA) + 1
    

    def AjouterArticle(self,A):
        ref = A.getref()
        index = self.RechercheArticle(ref)
        # if index== len(self.__listeA):
        #     self.__listeA.append(A)
        if index < len(self.__listeA) :
            quantiteact = self.__listeA[index].getqua()
            nvlquantite= quantiteact + A.getqua()
            self.__listeA[index].setqua(nvlquantite)

        else:
            self.__listeA.append(A)

    def SupprimerArticle(self,A):
        ref = A.getref()
        index = self.RechercheArticle(ref)
        if index < len(self.__listeA):
            self.__listeA.remove(A)
        
        

   
        



    def afficher(self):
        for i in self.__listeA:
            print(i)


    def Affiche(self,r):
        index = self.RechercheArticle(r)
        if index < len(self.__listeA):
            
            print(self.__listeA[index])

        else:

            print("atricle non trouve ")


    



    


# reference=int(input("entrer la reference du produit : "))
# description=input("entrer la description du produit : ")
# quantite=int(input("entrer la quantite du produit : "))
# prix=float(input("entrer le prix du produit : "))
# ref=int(input("entrer le reference : "))

A1=Article(1,"undo",20,200)
A2=Article(2,"deux",21,250)

# print(A1.__str__())

l=Stock()
l.AjouterArticle(A1)
l.AjouterArticle(A2)
l.afficher()
# l.AjouterArticle(Article(1,"undo",40,200))
# l.afficher()
# l.SupprimerArticle(A2)
# l.afficher()
ref=int(input("entrer le reference : "))
l.Affiche(ref)


# print("choisez un nombre  : ")
# print("1 - Ajouter un article")
# print("2 - Supprimer un article")
# print("3 - Rechercher un article")
# print("4 - Afficher un article ")
# print("0 - sortir ")
# n= int(input())


# while True:

#     match n:
#         case 1:
#             x = int(input("entrer le nombre des article : "))
#             for i in range(x):

#                reference=int(input("entrer la reference du produit : "))
#                description=input("entrer la description du produit : ")
#                quantite=int(input("entrer la quantite du produit : "))
#                prix=float(input("entrer le prix du produit : "))
#                A1=Article(reference,description,quantite,prix)
#                l=Stock()
#                l.AjouterArticle(A1)
            
#         case 4:
#                l.afficher()
#         case 0:
#             print("byby")
#             break

#         case _:
#                print("erreur")
        
            
            


            






