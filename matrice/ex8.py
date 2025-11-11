# m =[]
# k = 1
# for i in range(5):
#     l =[]
#     for j in range(5):
#         if i ==j :
#             if k %2==0:
#                 l.append(k)
#             else:
            
#                k=k+1
#         else:
#             n=0
#             l.append(n)
#         k=k+1
        
#     m.append(l)

# for i in m:
#     print(i)
l = [[1,2,3,4,5],[1,2,3,4,5],[1,2,3,4,5]]
s =0
for i in range(len(l)):
    
    for j in range(len(l[0])):
        s = l[i][j]+s

print(s)

