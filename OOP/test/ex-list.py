# listA = ["ayoub","ouahidi","age21ans","loubna","berrouk","ofppt"]
# print(listA)
# print(listA[1])
# print(listA[-1])
# print(listA[1:5])
# for item in listA:
#     print(item)
# if "ayoub" in listA:
#     print("yes")

# listA.append("mine")
# print(listA)

# listA.insert(3,"fine")
# listA.pop(4)
# print(listA)
# listC=[1,2,3,4]
# listB=["personne",".","##"]
# listB.extend(listC)
# # print(listB)

# # listD=listA.copy()
# # print(listD)
# from collections import namedtuple

# Point= namedtuple('ayoub',['x','y'])
# # p=Point(x=3,y=5)
# # p=Point(y=3,x=4)
# # print(p.x+p.y)
# #  print(p._asdict())
# # print(p._replace(x=4,y=5))
# # print(p)
# color=namedtuple('loubna',['red' ,'green','blue'])
# pixel=namedtuple('pixel',Point._fields+color._fields)
# print(pixel(11,22,33,44,55))
# from collections import deque,ChainMap
# list1 = deque(["ayoub", "loubna", "22"])
# list1.appendleft("ofppt")
# list1.append("Alice")
# print(list1)
# list1.pop()
# list1.popleft()
# print(list1)

# A = {'a':1,'b':2}
# B ={'b':5,'c':6}
# C= ChainMap(A,B)
# # print(C.items())
# for i,j in C.items():
#     print(i,j)


from collections import Counter,deque,ChainMap
# listA = ["ayoub","ouahidi","age21ans","ofppt","ayoub"]
# listB = Counter(listA) 
# print(listB) 
# listA = [1,1,1,2,2,2,3,3,4,56,77,7,7]
# listB = Counter(listA) 
# print(listB) 

# listA = Counter[{1,1,1,2,2,2,3,3,4,56,77,7,7}]
# print(listA)


# listA = Counter('gallahad') 
# print(listA) 

# listA = Counter({'red': 4, 'blue': 2}) 
# print(listA)

# listA = Counter(cats=4, dogs=8) 
# print(listA) 

# a = Counter(['ayoub','ouahidi'])
# print(a['test'])

# li = Counter({'a': 3, 'l': 2, 'g': 1, 'h': 1, 'd': 1})
# li.update("stage")
# print(li)

# test= Counter(chaise = 15,table= 20,ayoub=90,test=3)
# print(test.most_common(2))

# A = Counter(a=4, b=2, c=1, d=2)
# print(sorted(A.elements()))

# A1 = Counter(a=4,b=1,c=3,d=4)
# A2 = Counter(a=2,b=-2,c=3)
# A2.subtract( A1)
# print(A2.total())

# AA=deque("sta")
# for item in AA:
#     print(item.upper())
# AA.append("ge")
# print(AA)
# AA.appendleft("FULL")
# print(AA)
# AA.pop()
# print(AA)
# print(list(AA))

# AA[0]=2
# print(AA)
# print((list(reversed(AA))))
x = {('a', 1),('b', 10),('b', 10)}
y = {('b', 10)}
z = ChainMap(y, x)
for k, v in z.items(): #parcourir les éléments de z
 print(k, v)

# AA0=ChainMap(list(AA),list(A1))
# print(AA0)
# for k,v in AA0.items():
#     print(k,v)
from collections import OrderedDict,defaultdict
# d=OrderedDict()
# d['a']='1' #remplir d
# d['b']='2'
# d['c']='3'
# d['d']='4'
# d.move_to_end('b')
# print(d) #affiche OrderedDict([('a', '1'), ('c', '3'), ('d', '4'), ('b', '2')])
# d.move_to_end('b',last=False)
# print(d) #affiche OrderedDict([('b', '2'), ('a', '1'), ('c', '3'), ('d', '4')])
# print(d.popitem(False)) #affiche ('d', '4')
# print(d) #affiche Orde
# AA.extend("left")
# AA.extendleft("loooo")
# print(AA)

s = [('yellaw', 1),('blue',2),('yellaw', 3),('blue',4)]
d= defaultdict(int)
for k,v in s:
   d[k]=+(v)
print(sorted(d.items()))

s1 = "developemment"
d1 = defaultdict(int)
for k in s1:
   d1[k]=+1
print(d1.items())
print()
print(sorted(d1.items()))



from collections import defaultdict
defaultdcit_obj =defaultdict(int)
defaultdcit_obj["key1"]="value1"
defaultdcit_obj["key2"]="value2"
print(defaultdcit_obj["key1"]) #affiche: value1
print(defaultdcit_obj["key2"]) #affiche: value2
print(defaultdcit_obj["key3"])