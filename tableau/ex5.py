from random import randint
T = [randint(0,20) for i in range(100) ]
print(T)
def moyenne(T):

    som = 0
    for i in range(100):
      som=T[i]+som
    moy = som/100
    # print("le moyenne est",moy)
    return moy


cmp=0
moyenne()
print("le moyenne est : ",moyenne())

for i in range(100):
    if T[i]>=moyenne():
        cmp+=1
print("le nombre des etudiant sont : ",cmp)