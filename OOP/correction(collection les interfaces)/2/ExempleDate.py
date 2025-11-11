import datetime
class Personne:
    def __init__(self,d):
        self.__dateE = d
    def getDateE(self): return self.__dateE
    
pers = Personne("12/01/2002")
# d=pers.getDateE()
tab = pers.getDateE().split("/")
da= datetime.date(int(tab[2]),int(tab[1]),int(tab[0]))
print(da.year)
