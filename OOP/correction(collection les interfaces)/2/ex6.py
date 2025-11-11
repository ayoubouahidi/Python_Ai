from collections import *

class Stagiaire:
    def __init__(self, num = None, nom = None, prenom = None, dateNais = None):
        self.__num = num
        self.__nom = nom
        self.__prenom = prenom
        self.__dateNais = dateNais
        
    def getNum(self):
        return self.__num
    def getNom(self):
        return self.__nom
    def getPrenom(self):
        return self.__prenom
    def getDateNais(self):
        return self.__dateNais
    
    def setNum(self, newnum):
        self.__num = newnum
    def setNom(self, newnom):
        self.__nom = newnom
    def setPrenom(self, newprenom):
        self.__prenom = newprenom
    def setDateNais(self, newdateNais):
        self.__dateNais = newdateNais
        
    def __str__(self):
        return f'{self.__num}\t{self.__nom}\t\t{self.__prenom}\t{self.__dateNais}\t'

### namedtuple ###
Stagiairee = namedtuple('Stagiaire', ['num', 'nom', 'prenom', 'dateNais'])

### deux objets ###
stagiaire1 = Stagiaire(1, 'uchiha', 'itachi', '09/06/2003')
stagiaire2 = Stagiaire(2, 'uchiha', 'obito', '10/02/1993')

### deque ###
listStagiaires = deque()
listStagiaires.append(stagiaire1)
listStagiaires.append(stagiaire2)

### orderDict ###
stagiaires = OrderedDict()
stagiaires[1] = stagiaire1
stagiaires[2] = stagiaire2
for v in stagiaires.values():
    print(v)

### Dictionnaire ###
dict1 = {}
for k in stagiaires.keys():
    dict1[k] = stagiaires[k].getNom()
print(dict1)

### Counter ###
counter = Counter(dict1.values())
print(counter)