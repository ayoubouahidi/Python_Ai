def sommeM(m,l,c):

    
    A=[]
    for i in range(l):
        s = 0 
        L=[]
        for j in range (c):
            n = int(input("entrer un nombre : "))
            L.append(n)
            s+=L[i][j]

        m.append(L)
        
        z= " S L du",i,"est :",s
        A.append(z)



    print(A)    
        

    
    return m

# def somme(T):
#     T = []
#     som = 0
#     for i in range(100):
#       for j in range(100):
          
#       som=T[i]+som
     

    


m=[]
a=int(input("entrer l"))
b=int(input("entrer c"))

print(sommeM(m,a,b))



