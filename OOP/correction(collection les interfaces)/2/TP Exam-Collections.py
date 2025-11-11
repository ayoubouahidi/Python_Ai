from collections import *

class Article:
    def __init__(self, reference, description=None, quantite=None, prix=None):
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
    
art1 = Article(1,'article1',30,70)
art2 = Article(2,'article2',40,100)
art3 = Article(3,'article3',60,50)
articles = deque()

# Ajouter deux objets
articles.append(art1)
articles.append(art2)
articles.append(art3)

# Afficher les articles 
for k in range(len(articles)):
  print(articles[k])

for v in articles:
  print(v)

# Recherche les articles par reference
ref = int(input("entrer le reference"))
for k in range(len(articles)):
    if articles[k].getReference() == ref :
        print(articles[k])
    
# Recherche les articles par objet
ref = int(input("entrer le reference"))
art = Article(ref)
for v in articles :
  if v.getReference() == art.getReference():
    print(v)

# Supprimer les articles par objet
articles.remove(art3)  

# Supprimer les articles par position
ref = int(input("entrer la reference d'articles à supprimer"))
for k in range(len(articles) - 1):
    if articles[k].getReference() == ref :
       del(articles[k])

# Afficher
for v in articles:
  print(v)

#declarer 
artDict = OrderedDict()

# Ajouter OrderedDict
nbre = int(input("entrer le nombre des articles"))
for i in range(nbre):
   ref = int(input("entrer le reference"))
   des = input("entrer la designation")
   prix = float(input("entrer le prix"))
   qte = int(input("entrer la quantité")) 
   a1 = Article(ref,des,qte,prix)
   artDict[ref] = a1

# Parcourir par clé
for k in artDict.keys():
    print(artDict[k])

# Parcourir par valeur
for v in artDict.values():
    print(v)

# la reference : 4        la description : des4   la quantite : 45        le prix : 1200.0
# la reference : 5        la description : des5   la quantite : 23        le prix : 1800.0

# Dictionnaire
dict1 = {}
for k in artDict.keys():
    dict1[k] = artDict[k].getDescription()

print(dict1)   # {4: 'des4', 5: 'des5'} 

dict2 = {}
for k in artDict.keys():
    dict2[k] = artDict[k].getPrix()

print(dict2)  # {4: 1200.0, 5: 1800.0}

dict3 = {}
for k in artDict.keys():
    dict3[k] = artDict[k].getQuantite()

print(dict3)   # {4: 45, 5: 23}

# Counter
c1 = Counter(dict1.values())
print(c1)   # Counter({'des4': 1, 'des5': 1})
c2 = Counter(dict2.values())
print(c2)   # Counter({1200.0: 1, 1800.0: 1})
c3 = Counter(dict3.values())
print(c3)   # Counter({45: 1, 23: 1})

# DefaultDict
listeArticle = defaultdict(list)
for v in articles:
     listeArticle[v.getReference()].append(v.__str__())

print(listeArticle)
