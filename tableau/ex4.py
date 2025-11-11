from random import randint
t = [randint(-100,100) for i in range(100)]
pp = t[0]
pg = t[0]
pop = 0
pog = 0 
cmp = 0 

def pluspetit():
  pp = t[0]
  pop = 0
  
  for i in range(100):
     if pp > t[i]:
        pp =t[i]
        pop = i
     
  print(t)
  print("le plus petit est ",pp,"sa position est ",pop)
def plusGrand():
    pg = t[0]
    pog = 0 
    
    for i in range(100):
      if pg <t[i]:
        pg = t[i]
        pog = i
    print("le plus grand est ",pg,"sa position est ",pog)
     
def nombreoccurence():
    x = int(input("entrer un nombre : "))
    cmp = 0
    for i in range(100):
        if x == t[i]:
            cmp+=1

    print(x,"repeter",cmp,"fois")


while True:
  print("1 : rechercher PP et sa po\n2 : rechercher Pg et sa po\n3 : nombre d'occurence\n4: quitter")
  y = int(input())

  match y :
    case  1 : print(pluspetit())
    case  2 : print(plusGrand())
    case  3: print(nombreoccurence())
    case 4:  break
    case  _: print("erreur")
     
  
  
          

