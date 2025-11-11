from collections import deque
class ListeEmployer:
    def __init__(self):
        self.__ListeEmp=deque([])
    #getter
    def getList(self):
        return self.__ListeEmp
    #set
    def setList(self,a):
        self.__ListeEmp = a

    #METHODE
    def Rechercheemp(self,Num):
        for emp in self.__ListeEmp:
            if emp.getNum()==Num:
                return emp
        return None
    
    def AjouterEmp(self,emp):
        empR= self.Rechercheemp(emp.getNum())
        if empR is None:
            self.__ListeEmp.append(emp)
        else:
            print("deja existe ")

    def supprimerEmp(self,emp):
        empR=self.Rechercheemp(emp.getNum())
        if empR is not None:
            self.__ListeEmp.remove(emp)
        else:
            print("emplyer non trouver ...")

    def modifierSalaire(self,emp):
        if emp.getGrade()>11:
            emp.setSalaire(emp.getSalaire()+4500)
        elif emp.getGrade()==11:
            emp.setSalaire(emp.getSalaire()+3000)
        elif emp.getGrade()==10:
            emp.setSalaire(emp.getSalaire()+1200)
        elif emp.getGrade()<10:
            emp.setSalaire(emp.getSalaire()+800)


    def modifierEmployer(self,emp,nvnom=None,nvGrade=None):
        empR = self.Rechercheemp(emp.getNum())
        if empR is not None:
            if nvnom is not None:
                emp.setNom(nvnom)
            if nvGrade is not None:
                emp.setGrade(nvGrade)
            self.modifierSalaire(emp)
        else:
            print("Employer n'existe pas ")    
    
    def afficherEmployer(self):
        for emp in self.__ListeEmp:
            emp.affiche()
            
            

