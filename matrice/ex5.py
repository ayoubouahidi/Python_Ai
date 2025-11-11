def matsto(m,l,c):
    for i in range(l):
        s = 0
        for j in range(c):
            s = m[i][j] +s
            if s == 1 or s ==0:
                return True
            

    return False

m = [[0,0,10],[0,0,0]]
l= len(m)
c = len(m[0])
x = matsto(m,l,c)
print(x)


            