from collections import *
#Exercices 
### NamedTuple ###
Article=namedtuple('Article',['Reference','Designation','Prix','Quantite'])
a1=Article('Ref1','Des1',1200,40)
a2=Article('Ref2','Des2',1400,70)
print(a1)  # Article(Reference='Ref1', Designation='Des1', Prix=1200, Quantite=40)   
print(a2)  # Article(Reference='Ref2', Designation='Des2', Prix=1400, Quantite=70)  
print("Reference :",a1.Reference, "Prix : ",a1.Prix) # Reference : Ref1 Prix :  1200
print("Reference :",a2[0], "Prix :",a2[2])           # Reference : Ref2 Prix : 1400
print(a1._asdict())    # {'Reference': 'Ref1', 'Designation': 'Des1', 'Prix': 1200, 'Quantite': 40}     
print(a2._asdict())    # {'Reference': 'Ref2', 'Designation': 'Des2', 'Prix': 1400, 'Quantite': 70}        

### Counter ###
c= Counter('Infrastructure Digital')
print(c)
c1= Counter([2,8,9,2,1,9,1,3,8,4,5,6,2])
print(c1)
c2 = Counter(['Developpement Mobile','Developpement Digital,','Infrastructure Digital','Cyber securite'])
print(c2)

### defaultdict ###
# Stocker les valeurs multiples de 3 dans un default dict cle et val 
d = defaultdict(list)
for i in range(40):
    if i%3 == 0:
      d[i].append(i)
print(d) 

# Stocker les valeurs multiples de 5 en commencant par key=1 
d = defaultdict(list)
j = 1
for i in range(100):
    if i%5 == 0:
        d[j].append(i)
        j += 1
print(d)
# Stocker les valeurs paires 
d = defaultdict(int)
j = 1
for i in range(20):
    if i%2 == 0:
        d[j] = i
        j += 1
print(d) 

s="developpement informatique"
d = defaultdict(set)
j = 1
for lettre in s:
        d[j].add(lettre)
        j += 1
print(d)



