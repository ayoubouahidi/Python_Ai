from tkinter import *
def double(v):
    v=(int(entry_1.get()))

    entry_2.delete(0,END)
    entry_2.insert(0,v*2)

root = Tk()
root.geometry("600x300")
root.title("S.O.S")


Label_1 =Label(root,text="saissir un nombre : ")
Label_1.place(x=10,y=20)

entry_1=Entry(root,width=50,border=1)
entry_1.place(x=180,y=20)
entry_1.bind("<Return>",double)

Label_2 =Label(root,text="liste des nombres nombres: ")
Label_2.place(x=10,y=70)


entry_2=Entry(root,width=50,border=1)
entry_2.place(x=180,y=70)
"""fonction"""

""""""
# Button1=Button(root,text="rechercher les nombres premiers ",width=30,bg="blue",command=double)
# Button1.place(x=180,y=170)
    
root.mainloop()