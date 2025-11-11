from random import randint
def verifier(x):
    cmpP = 0
    cmpN = 0 
    cmpZ = 0
   
    for i in range(10):
        if x[i] > 0:
         cmpP+=1
        else:
           if x[i]<0:
              cmpN +=1
           else:
              cmpZ+=1
    print("le nombre des positif est : ",cmpP)
    print("le nombre des negatif est : ",cmpN)
    print("le nombre des null est : ",cmpZ)     


T=[randint(-100,100) for i in range(10)]
print(T)
verifier(T) 

 

    
        
        
