from random import randint
m=[]
for i in range(3):
    l=[randint(0,10) for i in range(4)]
    m.append(l)

for items in m:
    print(items)
    
print("----------")

for i in range(3):
    pgl=m[i][1]
    ppl=m[i][1]
    for j in range(4):
        if pgl < m[i][j]:
            pgl = m[i][j]
        
        if ppl > m[i][j]:
            ppl =m[i][j]

    print(f"le plus grand dans ligne {i+1} est {pgl}")
    print(f"le plus petit dans ligne {i+1} est {ppl}")

print("----------")

for j in range(4):
    pgc=m[1][j]
    ppc=m[1][j]
    for i in range(3):
        if pgc < m[i][j]:
            pgc = m[j][j]
        if ppc > m[i][j]:
            ppc = m[i][j]

    print(f"le plus grand dans colone {j+1} est {pgc}")
    print(f"le plus petit dans colone {j+1} est {ppc}")
    

