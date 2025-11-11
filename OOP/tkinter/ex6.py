from tkinter import *


def diviseurs():

    number=(int(entry_1.get()))

    les_diviseurs = []
    for i in range(1, number + 1):
        if number % i == 0:
            les_diviseurs.append(i)

    entry_2.delete(0,END)
    entry_2.insert(0,les_diviseurs)
    

root = Tk()
root.geometry("600x300")
root.title("test")
 

Label_1 =Label(root,text="saissir un nombre : ")
Label_1.place(x=10,y=20)

entry_1=Entry(root,width=50,border=1)
entry_1.place(x=180,y=20)
# entry_1.bind("<Return>",diviseurs)

Label_2 =Label(root,text=f"liste des nombres nombres: ")
Label_2.place(x=10,y=70)



entry_2=Entry(root,width=50,border=1)
entry_2.place(x=180,y=70)


Button1=Button(root,text="valider ",width=30,bg="blue",command=diviseurs)
Button1.place(x=180,y=170)

    
root.mainloop()