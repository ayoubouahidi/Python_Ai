from tkinter import *
root=Tk()
# root.geometry("600x600")
# root.title("ayoub ouahidi")
def factorielle():
    n=int (input.get())
    if  n > 0:
        res=1 
        for i in range(2,n+1):
            resf *=i
    res.delete(0,END)
    res.insert(0,resf)

valeur=Label (root,text='enter la valeur de n :')
valeur.grid(row=0,column=0, padx=40,pady=20)
# valeur.place(x=180,y=20)
input=Entry(root)
# input.place(x=180,y=70)
input.grid(row=0,column=1, padx=40,pady=20)



valeur=Label (root,text=' loubna cool :')
valeur.grid(row=1,column=0, padx=40,pady=20)
# valeur.place(x=180,y=20)
input=Entry(root)
# input.place(x=180,y=70)

input.grid(row=1,column=1, padx=40,pady=20)
root.mainloop()
