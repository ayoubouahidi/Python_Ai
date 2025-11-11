from tkinter import *
from tkinter import messagebox

root = Tk()
root.geometry("800x400")
root.title("S.O.S")


Label_1 =Label(root,text="saissir un nombre : ")
Label_1.place(x=10,y=20)

entry_1=Entry(root,width=50,border=1)
entry_1.place(x=180,y=20)

Label_2 =Label(root,text="liste des nombres nombres: ")
Label_2.place(x=10,y=70)

# entry_2=Text(root,width=50,border=1,height=5)
entry_2=Entry(root,width=50,border=1)
entry_2.place(x=180,y=70)

"""fonction"""
def est_premier(n):
    if n == 1:
        return False
    for i in range(2,int(n/2)+1):
        if n%i==0:
            return False
    return True



def estValid(v):
    
     if v.isdigit():
          return int(v)
     return messagebox.showerror("invalid","n'est pas un nombre")



def listdesnombres():
    

    v=((entry_1.get()))
    v=estValid(v)
    # print(v)
    l=[]
    if est_premier(v):
            for i in range(1,v+1):

              if est_premier(i):
                l.append(i)
                
            if l==[]:
                 entry_2.delete(0,END)
                 entry_2.insert(0,"tableau vide")
            else:
                 entry_2.delete(0,END)
                 entry_2.insert(0,l)

    else:
            entry_2.delete(0,END)
            entry_2.insert(0,"n'est pas premiers")




""""""



Button1=Button(root,text="rechercher les nombres premiers ",width=30,bg="blue",command=listdesnombres)
Button1.place(x=180,y=170)


root.mainloop()