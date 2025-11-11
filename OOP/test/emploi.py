T=[["php","Déscription php",10],["js","Déscription Js",7],["java","Déscription Java",0]]
emploi=input("Quel emploi vous cherchez?")
import sys
i=0
while i<3:
    for j in range(3):        
        if T[j][0]==emploi.lower():
            print(T[j][1])
            print("Les postes disponibles:",T[j][2])
            answer=input("voulez vous postulez?")
            if answer.lower()=="oui":
                if T[j][2]==0:
                    print("toutes les postes sont occupées")  
                T[j][2]=T[j][2]-1 
                print(T)
            sys.exit()    
            break
        i=+1
    print("failed")
    sys.exit()               


