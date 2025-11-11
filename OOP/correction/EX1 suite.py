class Point:
    def __init__(self, p, x, y, c):
        self.__p = p
        self.__x = x
        self.__y = y
        self.__c = c
# GETTERS

    def getP(self):
        return self.__p

    def getX(self):
        return self.__x

    def getY(self):
        return self.__y

    def getC(self):
        return self.__c

# SETTERS
    def setP(self, z):
        self.__p = z

    def setX(self, z):
        self.__x = z

    def setY(self, z):
        self.__y = z

    def setC(self, z):
        self.__c = z
# TRANSLATION

    def transx(self, X):
        self.__x += X

    def transy(self, Y):
        self.__y += Y

    def transboth(self, b):
        self.__x += b
        self.__y += b

# SEMETRIE
    def semtrx(self):
        self.__x *= -1

    def semtry(self):
        self.__y *= -1

    def semetrie(self):
        self.__x *= -1
        self.__y *= -1


# AFFICHER

    def affiche(self):
        print(
            f"la point {self.__p} d'abscisse {self.__x} d'ordonne {self.__y} et de couleur {self.__c}")


a1 = input("donner une lettre: ")
a2 = int(input(f"donner l'abscisse de {a1}: "))
a3 = int(input(f"Donner ordonne de {a1}: "))
a4 = input(f"Donner un couleur: ")
P = Point(a1, a2, a3, a4)
P.affiche()
a5 = int(input("donner translation d'abscisse : "))
a6 = int(input("donner translation d'ordonné: "))
P.transx(a5)
P.transy(a6)
P.affiche()
a7 = int(input("donner translation pour x et y: "))
P.transboth(a7)
P.affiche()
P.semtrx()
P.affiche()
P.semtry()
P.affiche()
