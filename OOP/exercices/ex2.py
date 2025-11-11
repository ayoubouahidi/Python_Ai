class somme:
    def __init__(self,x=0,y=0):
        self.x=x
        self.y=y
    def som(self):
        return self.x + self.y
a = int (input("entrer un nombre :"))
b = int(input("entrer un nombre :"))
s1=somme(a,b)


print("la somme est le nombre suivant ",s1.som())

