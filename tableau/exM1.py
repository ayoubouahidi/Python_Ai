
def entrerM(t,l,c):
   sL=0
   for i in range(l):
      m = []
      for j in range(c):
        n=int(input("emtrerun nombre :"))
        m.append(n)
        sL=sL+n

      S=sL
      t.append(m)
      print(f"la somme du {i} est {S}")


   return t

t=[]
l = int(input("entrer un nombre "))
c = int(input("entrer un nombre : "))
print(entrerM(t,l,c))
print(t)