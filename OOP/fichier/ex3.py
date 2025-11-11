import csv #importer la bibliothèque csv
fichier = open("annuaire.csv", "w") #ouvrir un fichier en mode écriture
ecrivainCSV = csv.writer(fichier,delimiter=";") #ouvrie un flux d’écriture
ecrivainCSV.writerow(["Nom","Prénom","Téléphone"]) #écrire une 1ère ligne dans le fichier annuaire.csv
ecrivainCSV.writerow(["0198546372","Marie","0198"]) #écrire une 2ème ligne dans le fichier annuaire.csv
ecrivainCSV.writerow(["Duval","Julien","0374"]) #écrire une 3ème ligne dans le fichier annuaire.csv
ecrivainCSV.writerow(["Jacquet","Bernard","02007"]) #écrire une 4ème ligne dans le fichier annuaire.csv
ecrivainCSV.writerow(["Martin","Julie","0391"]) #écrire une 5ème ligne dans le fichier annuaire.csv
fichier.close() #Fermer le fichie
#####################################

import csv #importer la bibliothèque csv
fichier = open("annuaire.csv", "r")
lecteurCSV = csv.reader(fichier,delimiter=";") # Ouverture du lecteur CSV en lui fournissant le caractère séparateur (ici ";")
for ligne in lecteurCSV: # parcourir les lignes du fichier CSV
  print(ligne) # afficher chaque ligne du fichier CSV
fichier.close() #fermer le fichier CS

##########################################
import csv #importer la bibliothèque csv
fichier = open("annuaire.csv", "r")
lecteurCSV = csv.DictReader(fichier,delimiter=";")
for ligne in lecteurCSV:
   print(ligne)
fichier.close()
###########################################
import csv #importer la bibliothèque csv
bonCommande = [{"produit":"cahier", "reference":"F452CP", "quantite":41, "prixUnitaire":1.6},
{"produit":"stylo bleu", "reference":"D857BL", "quantite":18, "prixUnitaire":0.95},
{"produit":"stylo noir", "reference":"D857NO", "quantite":18, "prixUnitaire":0.95},
] #déclarer des dictionnaires
fichier = open("bon-commande.csv", "w") #ouvrir un fichier en écrire
ecrivainCSV = csv.DictWriter(fichier,delimiter=";",fieldnames=bonCommande[0].keys()) 
#produire des lignes de sortie depuis les dictionnaires, 
# fieldnames contient les clés des dictionnaires
ecrivainCSV.writeheader() # Ecrire la ligne d'en-tête avec le titre des colonnes
for ligne in bonCommande: # Parcourir les dictionnaires
  ecrivainCSV.writerow(ligne) #Ecrire une ligne dans le fichier
fichier.close()
####################################################