from tkinter import *
root = Tk()
root.title("lcalcul page")
root.geometry("300x300")
root.config(bg="#C1CDCD")
root.resizable(False,False)

label_1 = Label(root, text="Enter the value of N:")
label_1.place(x=10,y=50)
entry_1 = Entry(root)
entry_1.place(x=140,y=50)

label_2 = Label(root, text="Enter the value of N:")
label_2.place(x=20,y=80)
entry_2 = Entry(root)
entry_2.place(x=140,y=80)

def calcul():
    num = entry_1.get()
    if num == 0 :
        return 1
    else:
        return num * calcul(num-1)
entry_result.delete(0, tk.END)  # Clear the result field first
entry_result.insert(0, "Please enter a valid integer")


btn = Button(root,text="calcul",command=calcul)
btn.place(x=200,y=120)

root.mainloop()