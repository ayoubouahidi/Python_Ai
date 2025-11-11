# f = open('a.txt', 'wt')
# for i in range(10):
#  f.write( "ligne " + str(i+1) + "\n")
# f.close()
# def U(n):
#     if n <0:
#         print('enter un nombre positif')
#     else:
#         if n == 0:
#             return 1/3
#         else:
#             U0 = 1/3
#             U1=2*U0/(U0+3)
            
#             if n==1:
#                 return U1
#             for i in range(2,n+1):
#                 Un=2*U1/(U0+3)
#                 U0, U1 = U1, Un
#             return Un
# print(U(3))
salles = []

for i in range(5):
    salle = {
        'code': f"S{i+1}",'type': f"Type{i+1}",'nbrordinateurs': 3,'ordinateurs':[]
    }
    for j in range(3):  
        ordinateur = {'code': f"O{i+1}-{j+1}",'prix': float(j+1) * 1000,  
        }
        salle['ordinateurs'].append(ordinateur)
    salles.append(salle)
for i in salles:
    print(i)

