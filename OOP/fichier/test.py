from adresse import Adresse
from employe import Employe
from employes import ListEmploye

try :
  adr1 = Adresse(1,"Rue1","SAFI",46001)
  #print(adr1)  # __str__()

  emp1 = Employe("N123456","Alami Ali",adr1,"+21224765423",13,17000.00)
  #emp1.affiche()

  adr2 = Adresse(2,"Rue2","SAFI",46001)
  emp2 = Employe("N939876","Dali Sara",adr2,"+21224865529",10,10000.00)

  list = ListEmploye()
  list.ajouterEmploye(emp1)
  list.ajouterEmploye(emp2)
  list.afficherEmploye()  # verifier méthode ajout
  list.modifierEmploye(emp2,"Ghali Ghita",None,None,None)
  list.afficherEmploye() # verifier méthode modifier 
  """ list.supprimerEmploye(emp1)
      list.afficherEmploye() """
  # print(list.rechercheEmployePos(emp2))
  # list.supprimerEmployePos(emp2)
  list.afficherEmploye()
  list.enregistrerEmployes()
  list.enregistrerEmp(emp1)
  # list.lireEmployes()
  # list.lireEmploye(emp1)
  list.EnregistrerEmployesT()
  list.EnregistrerEmployeT(emp2)
  # list.lireEmployesT()
  # list.lireEmployeT(emp2)
except ValueError as e : 
    print(e)
except TypeError as x :
    print(x)
except Exception as c :
    print(c)