from random import uniform
m = [[round(uniform(0,20),2) for j in range(25)]for j in range(25)]
for i in range(9):
        for j in range(25):
            print(m[i][j],end=" ")
        print()
    
# def plusg(m):
    
#     for i in range(9):
#         pg=m[0][0]
        
#         for j in range(25):
#             if pg < m[i][j]:
#                 pg =m[i][j]
#         print( "le plus grand dans ",i,"est : ",pg)
#         # maj
#         # if pg < 
        


        
#     return pg

# print(plusg(m))

