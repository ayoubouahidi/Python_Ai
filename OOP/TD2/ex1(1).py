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
        self.__listeA=[]
    
    @property
    def listearticle(self):return self.__listeA

    @listearticle
    def listearticle(self,a):
        self.__listeA=a

    def Recherche(self,ref):
        for i in self.__listeA:
            if i.getref()==ref:
                return i 
            else:
                return 'NULL'
        
    def AjouterArticle(self,A):
        



    

