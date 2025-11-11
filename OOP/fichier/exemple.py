# import json #importer la bibliothèque json
# fichier = open ( "c:/Users/Lenovo/Desktop/POO/fichier/exemple.json", "r" ) #ouvrir le fichier exemple.json en lecture
# x=json.loads(fichier.read( ) ) #décoder le texte et le transformer en dictionnaire.
# print(x)


######################################################
import json #importer la bibliothèque json
# quantiteFournitures= {" cahiers":134, "stylos":{"rouge":80,"bleu":74},"gommes":85} #déclarer un dictionnaire
# fichier=open ("fourniseur.json","w") #ouvrir un fichier en écriture
# fichier.write(json.dumps(quantiteFournitures)) #transformer le dictionnaire en texte json
# fichier.close() #fermer le fichie

fichier = open ( "fourniseur.json", "r" ) #ouvrir le fichier exemple.json en lecture
x=json.loads(fichier.read( ) ) #décoder le texte et le transformer en dictionnaire.
print(x)

