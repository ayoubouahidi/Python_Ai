# l=[[1,2,3],[1,2,3]]
# for j in range(3):
#     s = 0 
#     for i in range(2):
#         print(l[i][j])
#         s = s + l[i][j]
#     print("la somme est :",s)
########################
# l = 4
# c = 4
# L = [0] * l
# print(L)
# for i in range(l) :
#       L[i] = [0] * c
# print(L)
#####################
# l = 3
# c = 4
# M = []
# for i in range(l):
#      M.append([0] * c)
# print(M)
##############
# l = 3
# c = 4
# a = [['1'] * c for i in range(l)]
# print(a)
######
# for i in range(1,20,2):
#     print(i)
L=[i for i in range(1,20,2)]
print(L)
M1=[j*2 for j in L]
M2=[[j*2] for j in L]
M3=[[j]*2 for j in L]
print("“M1 :" ,M1)
print("M2: ",M2)
print("m3 : ",M3)
