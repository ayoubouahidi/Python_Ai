e1={"numInscription":1111,"nom":"alaoui","prenom":"zineb","option":"tdi"}

e2={"numInscription":2222,"nom":"alami","prenom":"aya","option":"tdi"}

e3={"numInscription":3333,"nom":"ibtihal","prenom":"nidal","option":"tdi"}

classe={}

for i in range(1,4):

  e=eval("e"+str(i))

  classe[e["numInscription"]]={"nom":e.get("nom"),"prenom":e.get("prenom"),"option":e.get("option")}

print("La classe :",classe)