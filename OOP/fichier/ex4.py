import csv
a = open("test.csv", "w") 
b = csv.writer(a,delimiter=";")
b.writerow(["Nom","Prénom","age"])
b.writerow(["ayoub","ouahidi","0198"])
b.writerow(["loubna","barouk","0374"])
b.writerow(["yassine","Bernard","02007"])
b.writerow(["Martin","Julie","0391"])
a.close()
#################################
import csv #importer la bibliothèque csv
fichier = open("annuaire.csv", "r")
lecteurCSV = csv.DictReader(fichier,delimiter=";")
for ligne in lecteurCSV:
   print(ligne)
fichier.close()