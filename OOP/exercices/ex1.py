class rectangle :
    def __init__(self,a=0,b=0):
        self.a=a
        self.b=b
    def surface(self):
        return self.a*self.b
   
x= int(input("entrer longueure :"))
y= int(input("entrer largeur :"))

rectangle1=rectangle(x,y)
print("la surface du triangle est:",rectangle1.surface())

