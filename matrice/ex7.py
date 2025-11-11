m = [[1,2,3,4,5],[1,2,3,4,5],[1,2,3,4,5]]
l = []
for i in range(len(m)):
    M = []
    for j in range(len(m[0])):
        if j % 2 !=0:
            M.append(j)
    l.append(M)

for i in l:
    print(i)


