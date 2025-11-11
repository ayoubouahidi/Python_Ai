from collections import namedtuple,deque,OrderedDict,Counter

stagiere = namedtuple('stagiere',['num','nom','prenom','datenaissance'])
stagiere1 = stagiere('1','ayoub','ouahidi','06/07/2002')
stagiere2 = stagiere('2','ayoub','ouahidi','06/07/2002')

liststagieres = deque()
liststagieres.append(stagiere1)
liststagieres.append(stagiere2)

for item in liststagieres:
  print(item)

stagieres = OrderedDict()

for i in liststagieres:
   stagieres[i.num]=i

for i in stagieres.items():
    print(i)

dict1 = {}
for i in stagieres.keys():
    dict1[i]=stagieres[i].nom

print(dict1)  

a1 =Counter(dict1.values())
print(a1 )
    
    

# dict1 ={}

# dict1 = {"nom1":"ayoub",'nom2':"ouahidi"}





# a1 =Counter(dict1.values())
# print(a1 )





