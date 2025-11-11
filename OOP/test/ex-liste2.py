from collections import defaultdict
d = defaultdict(list)
i = 1
# for  j  in range(20):
#     if j%2==0:
#      d[i].append(j)
#      i+=1
# print(d)

# i = 1 
# for j in range(5):
#     if j % 2 ==0 :
#         d[j].append(j / 2)
#         i+=1
#     else:
#         d[j].append((j * 3) + 1)
#         i+=1
# print(d)
s4= [('yellew',1),('red',2),('blue',3),('green',4),('green',5),('red',5)]
d4 = defaultdict(set)
for k,v in s4 :
    d4[k].add(v)
print(d4)
