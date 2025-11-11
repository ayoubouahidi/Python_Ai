class Article:
    def __init__(self, reference, description, quantite, prix):
        self.__reference = reference
        self.__description = description
        self.__quantite = quantite
        self.__prix = prix
        
    def getReference(self):
        return self.__reference
    def getDescription(self):
        return self.__description
    def getQuantite(self):
        return self.__quantite
    def getPrix(self):
        return self.__prix
    
    def setReference(self, newreference):
        self.__reference = newreference
    def setDescription(self, newdescription):
        self.__description = newdescription
    def setQuantite(self, newquantite):
        self.__quantite = newquantite
    def setPrix(self, newprix):
        self.__prix = newprix
        
    def __str__(self):
        return f'la reference : {self.__reference}\tla description : {self.__description}\tla quantite : {self.__quantite}\tle prix : {self.__prix}'
    
class Stock:
    def __init__(self):
        self.__ListArticle = []
        
    @property
    def ListArticle(self): return self.__ListArticle
    @ListArticle.setter
    def ListArticle(self, newListArticle): self.__ListArticle = newListArticle
    
    def RechercheArticle(self, reference):
        for k in range(len(self.__ListArticle)):
            if self.__ListArticle[k].getReference() == reference:
                return k
            else:
                return len(self.__ListArticle) + 1
            
    def RechercheArticleObjet(self,reference):
        for v in self.__ListArticle:
            if  v.getReference() == reference:
                return v
            else:
                return None
    
    # def ajout(self, a):
    #     self.__ListArticle.append(a)
    
    def AjouterArticle(self,article):
        o1 = self.RechercheArticleObjet(article.getReference())
        if o1 == None:
            self.__ListArticle.append(article)
        else:
            print('Deja existe!')
    
    def SupprimerArticle(self, article):
        o1 = self.RechercheArticleObjet(article.getReference())
        if o1 != None:
            self.__ListArticle.remove(article)
        else:
            print('Pas existe!')
            
    # def supprimer(self, a):
    #     self.__ListArticle.remove(a)
    
    def affiche(self):
        for v in self.__ListArticle:
                print(v)
    
    def AfficherArticle(self, reference):
        o1 = self.RechercheArticleObjet(reference)
        if o1 != None:
            for v in self.__ListArticle:
                print(v)
        else:
            print('Pas existe!')
    def rechercheparposition(self,ref):
        for k in range(len(self.__ListArticle)):
            if self.__ListArticle[k].getReference()==ref:
                return k
            else:
                return len(self.__ListArticle)
    def supprimerparposition(self,a):
        pos = self.rechercheparposition(a.getReference)
        if pos <= len(self.__ListArticle):
            self.__ListArticle.pop(pos)
        else:
            print("l'article n'existe pas !")

arti = Article(1,'my way',20,80)
a = Article(110,'quelle histoire',12,100)
a1 = Article(999,'qoire',12,100)
a2 = Article(10729,'qu hsxouszipqaszopisq ire',12,100)
article1 = Stock()
# print('\t\t\t\t-------------------------MENU-------------------------')
# print('\t\t\t\t\t\t\t1/ Ajouter article')
# print('\t\t\t\t\t\t\t2/ Supprimer article')
# print('\t\t\t\t\t\t\t3/ Rechercher article')
# print('\t\t\t\t\t\t\t4/ Aficher article')
# while True:
#     choix = int(input('tapez votre choix : '))
#     match choix:
#         case 1: article1.AjouterArticle(a)
#         case 2: article1.SupprimerArticle(article)
#         case 3: print(article1.RechercheArticle(110))
#         case 4: print(article1.AfficherArticle(110))
#         case _: print('Quitter!')
#     if choix > 4:
#         break
# article1.AjouterArticle(arti)
article1.AjouterArticle(arti)
article1.AjouterArticle(a1)
article1.AjouterArticle(a2)
# article1.affiche()
print(article1.RechercheArticleObjet(10729))
# article1.SupprimerArticle(arti)
# article1.affiche()
# article1.AjouterArticle(a)
# article1.affiche()
# article1.SupprimerArticle(a1)
# article1.affiche()
# article1.AfficherArticle(10729)
# article1.SupprimerArticle(arti)