from collections import deque
import csv

class ListEmploye :
    def __init__(self):
        self.__employes = deque()
    
    def rechercheEmploye(self,numPers):
        for emp in self.__employes :
            if emp.get_NumPers() == numPers :
                return emp
        return None

    def ajouterEmploye(self,emp):
        empTr = self.rechercheEmploye(emp.get_NumPers())
        if empTr is None :
            self.__employes.append(emp)
            print("Ajout avec succès")
        else :
            print("Employe Deja existe")

    def modifierSalaire(self,emp):
        if emp.get__Grade() < 10 :
           emp.set__Salaire(emp.get__Salaire() + 800)
        elif emp.get__Grade() == 10 :
           emp.set__Salaire(emp.get__Salaire() + 1200)
        elif emp.get__Grade() == 11 :   
           emp.set__Salaire(emp.get__Salaire() + 3000)
        elif emp.get__Grade() > 11 :   
           emp.set__Salaire(emp.get__Salaire() + 4500)

    def modifierEmploye(self,emp,nvnom=None,nvadr=None,nvtel=None,nvgrade=None) :
        empTr = self.rechercheEmploye(emp.get_NumPers())
        if empTr is not None :
            if nvnom is not None :
               emp.set_NomCompletPers(nvnom)
            if nvadr is not None :
                emp.set_Adresse(nvadr)
            if nvtel is not None :
                emp.set_Tel(nvtel)
            if nvgrade is not None :
                emp.set__Grade(nvgrade)
            self.modifierSalaire(emp)

    def supprimerEmploye(self,emp) :
        empTr = self.rechercheEmploye(emp.get_NumPers())
        if empTr is not None :
            self.__employes.remove(emp)   
        else : 
            print("employé non trouvé") 

    """  def rechercheEmployePos(self,emp) :
        for i in  range(len(self.__employes)):
            if self.__employes[i].get_NumPers() == emp.get_NumPers() : 
                return i
        return len(self.__employes) + 1 """

    """  def supprimerEmployePos(self,emp) :
        pos = self.rechercheEmploye(emp)
        if pos < len(self.__employes) :
            del (self.__employes[pos])
        print("Employe introuvable") """

    def afficherEmploye(self) :
        for emp in self.__employes :
            emp.affiche()    # print(emp)  ==> __str__()
   
    def  enregistrerEmployes(self):
        with open("employes.csv", 'w', newline='') as f:
            header = ["NumPers", "NomCompletPers","Adresse", "Tel", "Grade", "Salaire"]
            writer = csv.DictWriter(f, fieldnames=header)
            writer.writeheader()
            for v in self.__employes:
                writer.writerow({"NumPers": v.get_NumPers(),"NomCompletPers": v.get_NomCompletPers(),
                                "Adresse": v.get_Adresse(),"Tel": v.get_Tel(),
                                 "Grade": v.get__Grade(),"Salaire": v.get__Salaire()
            })

    def  enregistrerEmp(self,emp):
        with open("employe.csv", 'w', newline='') as f:
            header = ["NumPers", "NomCompletPers","Adresse", "Tel", "Grade", "Salaire"]
            writer = csv.DictWriter(f, fieldnames=header)
            writer.writeheader()
            empTr = self.rechercheEmploye(emp.get_NumPers())
            #emp.affiche()
            if empTr is not None :
                writer.writerow({"NumPers": emp.get_NumPers(),"NomCompletPers": emp.get_NomCompletPers(),
                                "Adresse": emp.get_Adresse(),"Tel": emp.get_Tel(),
                                 "Grade": emp.get__Grade(),"Salaire": emp.get__Salaire()
            })

    def lireEmployes(self):
        f = open("employes.csv", 'r')
        readcsv = csv.reader(f, delimiter='-')
        for v in readcsv:
            print(v)
        f.close()
    
    def lireEmploye(self,emp):
        f = open("employe.csv", 'r')
        readcsv = csv.reader(f, delimiter='-')
        for v in readcsv:
            if v[0] == emp.get_NumPers() :
                print(v)
        f.close()

    def EnregistrerEmployesT(self):
        f = open("employes.txt","w")
        ch = "NumPers NomComplet Adresse Tel Grade Salaire"
        f.write(ch + "\n")
        for emp in self.__employes :
            ch = str(emp.get_NumPers()) + "-" +emp.get_NomCompletPers() + "-" + str(emp.get_Adresse()) + " - " + str(emp.get_Tel())
            ch +=  " -" + str(emp.get__Grade()) + "- " + str(emp.get__Salaire())
            f.write(ch + "\n") 
             # f.write(emp.affiche())
        f.close()

    def EnregistrerEmployeT(self,em):
        f = open("employe.txt","w")
        ch = "NumPers NomComplet Adresse Tel Grade Salaire"
        f.write(ch + "\n")
        for emp in self.__employes :
            if emp.get_NumPers() == em.get_NumPers() :
               ch = str(emp.get_NumPers()) + "-" +emp.get_NomCompletPers() + "-" + str(emp.get_Adresse()) + " - " + str(emp.get_Tel())
               ch +=  " -" + str(emp.get__Grade()) + "- " + str(emp.get__Salaire())
               f.write(ch + "\n") 
               # f.write(emp.affiche())
        f.close()

    def lireEmployesT(self):
        f = open("employes.txt","r")
        print(f.read())
        f.close()

   ## probleme ## 
    """ def lireEmployeT(self,em):
        f = open("employe.txt","r")
        tab = f.readline().strip().split("-")
        while True:
            x = f.readline()
            for s in range(x) :
                print(s)
        f.close() """