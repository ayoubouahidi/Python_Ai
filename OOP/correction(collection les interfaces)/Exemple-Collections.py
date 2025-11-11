from collections import *
""""
### tuple ###
t=(11,22)  
print(t)       # (11, 22)
print(t[0])    # 11
print(t[1])    # 12
t1=(11,22,'groupe') 
print(t1)  # (11, 22, 'groupe')
"""

### namedtuple ###
# Point = namedtuple('Point',['a','b','c'])  # Point le nom de tuple
# p = Point(11, 22,33)
# print(p[0]+ p[1],p[2]) # par index  ==> 11 22
# print(p.a , p.b)   # par nom attribut    ==> 33
# print(p)   # Point(a=11, b=22)
# print(p._asdict())   # {'a': 11, 'b': 22}



# print(p._replace(30))  #error
# print(p._replace(30,7))  #error
# print(p._replace(a=30,7))  #error
# print(p._replace(30,b=7)) #error 


# print(p._replace(a=30))     # Point(a=30, b=22) ==> a change sa valeur
# print(p._replace(b=7))      # Point(a=11, b=7)  ==> b  change sa valeur
# print(p._replace(a=30,b=7)) # Point(a=30, b=7) ==> a et b change ses valeurs
# print(p)                    # Point(a=11, b=22)  ==> point n'a pas changé sa valeur

# print(Point._fields)      # Recupere les noms des attributs ('a', 'b')
# Color=namedtuple('Color', 'red green, blue') 
# # print(Color._fields)      # Recupere les noms des attributs ('red', 'green', 'blue')
# Pixel=namedtuple('Pixel', Point._fields + Color._fields) 
# print(Pixel(11,22,128,266,0,0))   # Pixel(a=11, b=22, red=128, green=266, blue=0)
# print(Point._fields)            # ('a', 'b')
# # p = Point(100,110)
# # print(p)                       # Point(a=100, b=110)
# color = namedtuple('Col','red green blue')
# c = color('red','green','blue')
# print(c)                       # Col(red='red', green='green', blue='blue')
# Pixel = namedtuple('Pi',Point._fields + color._fields)
# print(Pixel(3, y=23, blue=15, red=255, green = 129)) # error 
# print(Pixel(3, blue=15, red=255, green = 129,y=23))  # error
# print(Pixel(3,23, blue=15, red=255, green = 129))    # Pi(a=3, b=23, red=255, green=129, blue=15)

#*#*#**#*#*#*#*#*#*#*#*#*#*#
# a = Pixel(11,22,128,266,0,0,0)
# print(a)
#*#*#**#*#*#*#*#*#*#*#*#*#*#


# # namedtuple Example
# Personne=namedtuple('Personne',['Nom','Age'])
# p1=Personne('Amine', 21)
# p2=Personne(Nom='Ayman',Age=22)
# print(p1)     # Personne(Nom='Amine', Age=21)
# print(p2)     # Personne(Nom='Ayman', Age=22)
# print(p1.Nom, 'Age de',p1.Age) # Amine Age de 21
# print(p2[0], 'Age de',p2.Age)  # Ayman Age de 22
# print(p1._asdict())            # {'Nom': 'Amine', 'Age': 21}
# print(p2._asdict())            # {'Nom': 'Ayman', 'Age': 22}


# ### deque ###
# favorite_deque = deque(['samary','jamie','mary'])
# favorite_deque.appendleft('alice')
# favorite_deque.append('bob')
# print(favorite_deque)         # deque(['alice', 'samary', 'jamie', 'mary', 'bob'])
# favorite_deque.pop()
# print(favorite_deque)         # deque(['alice', 'samary', 'jamie', 'mary'])
# favorite_deque.popleft()
# print(favorite_deque)         # deque(['samary', 'jamie', 'mary'])  
# p1 = favorite_deque.clear()
# print(p1)                     # None


# Deque Example
# d = deque('sta')
# for x in d:
#     print(x.upper()) # S  T   A
# d.append('ck')
# print(d)           # deque(['s', 't', 'a', 'ck'])
# d.appendleft('full')
# print(d)           # deque(['full', 's', 't', 'a', 'ck'])
# d.pop()
# print(d)           # deque(['full', 's', 't', 'a'])     
# d.popleft()
# print(d)           # deque(['s', 't', 'a'])    
# print(list(d))     # ['s', 't', 'a']
# d[0]='e'
# print(d)           # deque(['e', 't', 'a'])
# l = []
# l.extend(reversed(list(d)))
# print(l)         # ['a', 't', 'e']
# print(d)


# d.extend('k font-end')

# print(d)        # deque(['e', 't', 'a', 'k', ' ', 'f', 'o', 'n', 't', '-', 'e', 'n', 'd'])
#*#*#*#*#*#*#*##*#*#*#**#*#*#*#*#*#*#*#*#*#*#
# p = deque(['ayoub'])
# p.extend("ayoub")
# print(p)
#*#*#**#*#*#*#*#*#*#*#*#*#*#
# d1 = deque(reversed(d))
# print(d1)      # deque(['d', 'n', 'e', '-', 't', 'n', 'o', 'f', ' ', 'k', 'a', 't', 'e'])
# d1.clear()
# d1.extend('digital')
# print(d1)      # deque(['d', 'i', 'g', 'i', 't', 'a', 'l'])
# d1.extendleft(reversed('developpement'))
# print(d1)      # deque(['d', 'e', 'v', 'e', 'l', 'o', 'p', 'p', 'e', 'm', 'e', 'n', 't', 'd', 'i', 'g', 'i', 't', 'a', 'l'])
# d1.insert(0,'back-end')
# d1[1]='full-stack'
# print(d1)  # deque(['back-end', 'full-stack', 'e', 'v', 'e', 'l', 'o', 'p', 'p', 'e', 'm', 'e', 'n', 't', 'd', 'i', 'g', 'i', 't', 'a', 'l'])


### ChainMap ###
# l1=['a','b','c']
# l2=['x','y']
# l3 = ChainMap(l1,l2) 
# for v in l3:
#     print(v)        # x
#                     # y
#                     # a
#                     # b
#                     # c
# print(l3)           # ChainMap(['a', 'b', 'c'], ['x', 'y'])

# x = {'a':1,'b':2}
# y = {'b':10,'c':4}
# z = ChainMap(y,x)
# print(z)            # ChainMap({'b': 10, 'c': 4}, {'a': 1, 'b': 2})
# for k,v in z.items():
#     print(k,v)
# a 1
# b 10
# c 4
# dic1 = {'x':1,'y':4,'z':5}
# dic2 = {'a':4,'b':2}
# d14 = ChainMap(dic1,dic2)
# print(d14)    # ChainMap({'x': 1, 'y': 4, 'z': 5}, {'a': 4, 'b': 2})


# x = ['a', 'b' , 'c']
# y = [1, 2, 3]
# z = ChainMap(x, y)
# print(z)           # ChainMap(['a', 'b', 'c'], [1, 2, 3])
# for v  in z:
#     print(v) 
# 1
# 2
# 3
# a
# b
# c
# x = {'a': 1, 'b': 2}
# y = {'b': 10, 'c': 11}
# z = ChainMap(x, y)
# print(z)              # ChainMap({'a': 1, 'b': 2}, {'b': 10, 'c': 11})
# print(z.items())      # ItemsView(ChainMap({'a': 1, 'b': 2}, {'b': 10, 'c': 11}))
# for k, v in z.items():
#     print(k, v)
# # b 2
# # c 11
# # a 1

# L1={'a':1,'b':2,'c':3}
# L2={'x':4,'y':5}
# L3= ChainMap(L1,L2)
# print(L3)             # ChainMap({'a': 1, 'b': 2, 'c': 3}, {'x': 4, 'y': 5})
# for k,v in L3.items():
#     print(k,':',v)
# x : 4
# y : 5
# a : 1
# b : 2
# c : 3


"""
### Counter  ###  
c1 = Counter()
print(c1)     # Counter()

c2 = Counter('je ai prend une guerre contre moi, et les resultats cent ce que tu vois maintenant.')
print(c2)     # Counter({' ': 15, 'e': 13, 't': 8, 'n': 7, 'r': 5, 'u': 5, 'a': 4, 'i': 4, 's': 4, 'c': 3, 'o': 3, 'm': 2, 'l': 2, 'j': 1, 'p': 1, 'd': 1, 'g': 1, ',': 1, 'q': 1, 'v': 1, '.': 1})

c3 = Counter(['g1','g2'])
print(c3)     # Counter({'g1': 1, 'g2': 1})

c4 = Counter(['full','pop,','info','devlop'])
print(c4)     # Counter({'full': 1, 'pop,': 1, 'info': 1, 'devlop': 1})

c5 = Counter([1,2,3,5,7,1,5,5,3,2])
print(c5)     # Counter({5: 3, 1: 2, 2: 2, 3: 2, 7: 1})

c6 = Counter('full'+'deplo')
print(c6)     # Counter({'l': 3, 'f': 1, 'u': 1, 'd': 1, 'e': 1, 'p': 1, 'o': 1})

c7 = Counter(['a','b'])
print(c7['c']) # 0

c8 = Counter(a=4,b=2,c=1,d=8)
i = ''.join(c8.elements())
print(i)     # aaaabbcdddddddd

c9 = Counter(a=4,b=2,c=1,d=-2,e=0)
print(sorted(c9.elements()))   # ['a', 'a', 'a', 'a', 'b', 'b', 'c']

c10 = Counter({'a':4,'b':2,'c':1})
print(sorted(c10.elements()))  # ['a', 'a', 'a', 'a', 'b', 'b', 'c']

c11 = Counter(a=5,b=7,d=0,e=8)
print(c11.total())         # 20
c12 = Counter(a=3,b=-5,c=2,d=1,f=6)
c11.subtract(c12)              
print(c11)                 # Counter({'b': 12, 'e': 8, 'a': 2, 'd': -1, 'c': -2, 'f': -6})
print(c11.total())         # 13
c12.subtract(c11)
print(c12)                 # Counter({'f': 12, 'c': 4, 'd': 2, 'a': 1, 'e': -8, 'b': -17})

c10 = Counter(a=4,b=2,c=1,d=-2,e=0)
c10.subtract(c10)
print(c10)                 # Counter({'a': 0, 'b': 0, 'c': 0, 'd': 0, 'e': 0})
"""

### OrderedDict ###
d0 = OrderedDict()
d0['a'] = '1'
d0['b'] = '2'
d0['c'] = '3'
d0['d'] = '4'
# print(d0)
print(d0)      # OrderedDict([('a', '1'), ('b', '2'), ('c', '3'), ('d', '4')])
d0.move_to_end('b')
print(d0)      # OrderedDict([('a', '1'), ('c', '3'), ('d', '4'), ('b', '2')])
d0.move_to_end('b',last=False)
print(d0)      # OrderedDict([('b', '2'), ('a', '1'), ('c', '3'), ('d', '4')])
# print(d0.popitem(True))  # ('d', '4')
# print(d0)      # OrderedDict([('b', '2'), ('a', '1'), ('c', '3')])   
# print(d0.popitem(False)) # ('b', '2')
# print(d0)      # OrderedDict([('a', '1'), ('c', '3')])



# # defaultdict Example
# s = [('yellow',1),('blue',2),('red',1),('yellow',3),('red',2)]
# d = defaultdict(list)
# for k,v in s:
#     d[k].append(v)
# print(d)    # defaultdict(<class 'list'>, {'yellow': [1, 3], 'blue': [2], 'red': [1, 2]})
# print(sorted(d.items()))  # [('blue', [2]), ('red', [1, 2]), ('yellow', [1, 3])]
# print(d.items())          # dict_items([('yellow', [1, 3]), ('blue', [2]), ('red', [1, 2])])

# s = [('yellow',1),('blue',2),('red',1),('yellow',3),('red',2)]
# d = defaultdict(int)
# for k,v in s:
#     d[k] = v
# print(d)         # defaultdict(<class 'int'>, {'yellow': 3, 'blue': 2, 'red': 2})
# print(d.items()) # dict_items([('yellow', 3), ('blue', 2), ('red', 2)])
# print(sorted(d.items())) # [('blue', 2), ('red', 2), ('yellow', 3)]

# s = [('yellow',1),('red',3),('blue',2),('green',4),('red',1),('green',1)]
# d = defaultdict(set)
# for k,v in s:
#     d[k].add(v)
# print(d)  # defaultdict(<class 'set'>, {'yellow': {1}, 'red': {1, 3}, 'blue': {2}, 'green': {1, 4}})

# l = [1,2,3,4,2,5,3,2]
# d = defaultdict(int)
# for k in l:
#     d[k] += 1
# print(d)         # defaultdict(<class 'int'>, {1: 1, 2: 3, 3: 2, 4: 1, 5: 1})
# print(d.items()) # dict_items([(1, 1), (2, 3), (3, 2), (4, 1), (5, 1)])
# print(sorted(d.items())) # [(1, 1), (2, 3), (3, 2), (4, 1), (5, 1)]
# """
# """
# # Exemple 
# s = 'developpement'
# d = defaultdict(int)
# for k in s:
#     d[k] = k
# print(d.items())   # dict_items([('d', 'd'), ('e', 'e'), ('v', 'v'), ('l', 'l'), ('o', 'o'), ('p', 'p'), ('m', 'm'), ('n', 'n'), ('t', 't')])
# print(sorted(d.items())) # [('d', 'd'), ('e', 'e'), ('l', 'l'), ('m', 'm'), ('n', 'n'), ('o', 'o'), ('p', 'p'), ('t', 't'), ('v', 'v')]

# # Exemple Counter
# s = 'developpement'
# d = defaultdict(int)
# for k in s:
#     d[k] += 1

# print(d)  # defaultdict(<class 'int'>, {'d': 1, 'e': 4, 'v': 1, 'l': 1, 'o': 1, 'p': 2, 'm': 1, 'n': 1, 't': 1})
# print(d.items()) # dict_items([('d', 1), ('e', 4), ('v', 1), ('l', 1), ('o', 1), ('p', 2), ('m', 1), ('n', 1), ('t', 1)])
# print(sorted(d.items())) #[('d', 1), ('e', 4), ('l', 1), ('m', 1), ('n', 1), ('o', 1), ('p', 2), ('t', 1), ('v', 1)]
# """
# """
# ### ChainMap Example
# dic1 = [('a',1),('b',2),('c',3)]
# dic2 = [('x',5),('y',6)]
# dic3 = ChainMap(dic1,dic2)
# print(dic3)   # ChainMap([('a', 1), ('b', 2), ('c', 3)], [('x', 5), ('y', 6)])

# # chainMap
# dic1 = [('a',1),('b',2),('c',3)]
# dic2 = [('x',5),('y',6),('a',7)]
# dic3 = ChainMap(dic1,dic2)
# print(dic3)   # ChainMap([('a', 1), ('b', 2), ('c', 3)], [('x', 5), ('y', 6), ('a', 7)])
# # for k,v in dic3.items(): # error 
# #   print(k,v)
# for v in dic3:
#    print(v)
# ('x', 5)
# ('y', 6)
# ('a', 7)
# ('a', 1)
# ('b', 2)
'''autre '''
# liste = [1,2,3,4,5]
# for i in enumerate(liste):
#     print(i)

# #Exercices 
# # Stocker les valeurs paires dans un default dict cle et val sont paires 
# d = defaultdict(list)
# for i in range(20):
#     if i%2 == 0:
#         d[i].append(i)
# print(d) 
# # defaultdict(<class 'list'>, {0: [0], 2: [2], 4: [4], 6: [6], 8: [8], 10: [10], 12: [12], 14: [14], 16: [16], 18: [18]})

# # Stocker les valeurs paires en commencant par key=1 dont la clé et val sont differents
# d = defaultdict(list)
# j = 1
# for i in range(20):
#     if i%2 == 0:
#         d[j].append(i)
#         j += 1
# print(d)
# # defaultdict(<class 'list'>, {1: [0], 2: [2], 3: [4], 4: [6], 5: [8], 6: [10], 7: [12], 8: [14], 9: [16], 10: [18]})


# # Stocker les valeurs si  valeur pair val//2 sinon  val*3 + 1dans un default dict
# d = defaultdict(int)
# for i in range(21):
#     if i%2 == 0:
#         d[i] = (i//2)
#     else:
#         d[i] = ((i*3)+1)
# print(d)
# #defaultdict(<class 'int'>, {0: 0, 1: 4, 2: 1, 3: 10, 4: 2, 5: 16, 6: 3, 7: 22, 8: 4, 9: 28, 10: 5, 11: 34, 12: 6, 13: 40, 14: 7, 15: 46, 16: 8, 17: 52, 18: 9, 19: 58, 20: 10})