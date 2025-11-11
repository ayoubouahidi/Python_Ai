#exemple 1
# try:
#    i= int(input('i ? '))
#    j = int(input('j ? '))
#    print(i, '/', j,'=', i / j)
# except (ValueError, ZeroDivisionError) as e:
#      print('Erreur de calcul :', e) # exécuter le même code pour différents types d’exceptions
# except:
#      print('Autre erreur.')
#exemple 2
# def inverse(a):
    
#     if a == 0 :
#         # raise Exception
#         # raise ValueError
#         raise ValueError("le nombre egal 0 ")
#     else:
#          return f'1/{a}'
    
# try :
#   x = int(input("entrer un entier"))
#   print(inverse(x))

# except ValueError as e:
#     print("erreur :",e)
#exemple 3
# class ZeroException(Exception):pass
# def inverse(a):
#     if a == 0 :
#         raise ZeroException("la valeur de x doit etre different de zero ")
#     else:
#         y = 1.0/a
#         return y
#exemple 4 
class personne:
    cpt = 0 
    def __init__(self,age,diplome):
        personne.cpt+=1
        self.__code = personne.cpt
        self.__age = age 
        self.__diplome = diplome

    def getage(self):
        return self.__age
    
    def getdiplome(self):
        return self.__diplome
    
    def setage(self,a):
        if a < 25 or a > 31: raise ValueError("age ")
        self.__age = a
        
      
    
    def setdiplome(self,b):
        if b !=2 and b !=3:
            raise ValueError("diplome")
        self.__diplome=b
        
        
    
    def affiche(self):
        return f" code est {self.__code}age est {self.__age} diplome est :bac+{self.__diplome}"
    


x = int(input("entrer un age mais valide :"))
y = int(input("enter le niveau :"))


try:
    
    p1 = personne(x,y)
    p1.setage(x)
    p1.setdiplome(y)
    print(p1.affiche())
except ValueError as e:
    print("ereur",e)





        
    

    