A=[[1, 4, 8], [2, 5, 9], [3, 6, 0]]
B=[[1, 4, 8], [2, 5, 9], [3, 6, 0]]

C=[]
for i in range(3):
    l=[]
    for j in range(3):
        s=A[i][j]+B[i][j]
        l.append(s)
        
    C.append(l)
for i in C :
    print(i)