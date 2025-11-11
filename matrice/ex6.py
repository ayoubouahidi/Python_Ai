notes1 = [18.5,17.75,19]
notes2 = [18.5,17.75,19]
stagiere1 = {'num':1,'nom':'ayoub','notes':notes1}
stagiere2 = {'num':1,'nom':'ayoub','notes':notes2}

l1 = len(notes1)
m1 =0
for i in range(l1):
    m1 = m1+notes1[i]
m1 = m1/l1

l2 = len(notes2)
m2 =0
for i in range(l2):
    m2 = m2+notes2[i]
m2 = m2/l2

if m1 > m2:
    print('le stagire 1 est le plus grand ')
else:
    if m1 < m2:
        print('le stagire 2 est le plus grand ')
    else:
        print('lle mem moyenne ')
