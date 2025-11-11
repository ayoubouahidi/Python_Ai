from tkinter import *
from tkinter import ttk
from math import gcd

root=Tk()
root.geometry("600x300")
root.title("test")

Label_1 =Label(root,text="saissir un nombre : ")
Label_1.place(x=10,y=20)

entry_1=Entry(root,width=50,border=1)
entry_1.place(x=180,y=20)

entry_2=Entry(root,width=50,border=1)
entry_2.place(x=180,y=40)

combo=ttk.Combobox(root,values=["PGCD",'PPCM'])
combo.place(x=180,y=100)

Label_RE =Label(root,text="RESULTAT : ")
Label_RE.place(x=10,y=120)

def calcul(n1):
  n1= int(entry_1.get())
  n2= int(entry_2.get())

  d=gcd(n1,n2)
  m=(n1*n2)/d
  if combo ==["PGCD"]:
    Label_RE["text"]+=str(d)

combo.bind("<<ComboboxSelected>>",calcul)





    

root.mainloop()