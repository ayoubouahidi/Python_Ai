from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from random import randint
ActivePlayer=1
P1=[]
P2=[]

abdo=Tk()
abdo.title("tic tac toy : playe1")
style=ttk.Style()
style.theme_use('classic')


bu1 = ttk.Button(abdo , text=' ')
bu1.grid(row=0,column=0,sticky='snew' , ipadx=40 , ipady=40)
bu1.config(command=lambda : BuClick(1))


bu2 = ttk.Button(abdo , text=' ')
bu2.grid(row=0,column=1,sticky='snew' , ipadx=40 , ipady=40)
bu2.config(command=lambda : BuClick(2))


bu3 = ttk.Button(abdo , text=' ')
bu3.grid(row=0,column=2,sticky='snew' , ipadx=40 , ipady=40)
bu3.config(command=lambda : BuClick(3))


bu4 = ttk.Button(abdo , text=' ')
bu4.grid(row=1,column=0,sticky='snew' , ipadx=40 , ipady=40)
bu4.config(command=lambda : BuClick(4))


bu5 = ttk.Button(abdo , text=' ')
bu5.grid(row=1,column=1,sticky='snew' , ipadx=40 , ipady=40)
bu5.config(command=lambda : BuClick(5))


bu6 = ttk.Button(abdo , text=' ')
bu6.grid(row=1,column=2,sticky='snew' , ipadx=40 , ipady=40)
bu6.config(command=lambda : BuClick(6))


bu7 = ttk.Button(abdo , text=' ')
bu7.grid(row=2,column=0,sticky='snew' , ipadx=40 , ipady=40)
bu7.config(command=lambda : BuClick(7))


bu8 = ttk.Button(abdo , text=' ')
bu8.grid(row=2,column=1,sticky='snew' , ipadx=40 , ipady=40)
bu8.config(command=lambda : BuClick(8))


bu9 = ttk.Button(abdo , text=' ')
bu9.grid(row=2,column=2,sticky='snew' , ipadx=40 , ipady=40)
bu9.config(command=lambda : BuClick(9))


def BuClick(id):
    global ActivePlayer
    global P1
    global P2
    if(ActivePlayer==1):
        SetLayout(id,'x')
        P1.append(id)
        abdo.title('tic tac toy : playe2')
        ActivePlayer=2
        print(format(P1))
        otoplayer()
    elif(ActivePlayer==2):
        SetLayout(id , 'O')
        P2.append(id)
        abdo.title('tic tac toy : playe1')
        ActivePlayer=1
        print(format(P2))
    abd()
def abd():
    winer = -1


    if( 1 in P1) and (2 in P1) and (3 in P1):
        winer = 1 
    if( 1 in P2) and (2 in P2) and (3 in P2):
        winer = 2 

    if( 4 in P1) and (5 in P1) and (6 in P1):
        winer = 1 
    if( 4 in P2) and (5 in P2) and (6 in P2):
        winer = 2 

    if( 7 in P1) and (8 in P1) and (9 in P1):
        winer = 1 
    if( 7 in P2) and (8 in P2) and (9 in P2):
        winer = 2 

    if( 1 in P1) and (4 in P1) and (7 in P1):
        winer = 1 
    if( 1 in P2) and (4 in P2) and (7 in P2):
        winer = 2 


    if( 2 in P1) and (5 in P1) and (8 in P1):
        winer = 1 
    if( 2 in P2) and (5 in P2) and (8 in P2):
        winer = 2 

    if( 3 in P1) and (6 in P1) and (9 in P1):
        winer = 1 
    if( 3 in P2) and (6 in P2) and (9 in P2):
        winer = 2 

    if( 3 in P1) and (5 in P1) and (7 in P1):
        winer = 1 
    if( 3 in P2) and (5 in P2) and (7 in P2):
        winer = 2 

    if( 1 in P1) and (5 in P1) and (9 in P1):
        winer = 1 
    if( 1 in P2) and (5 in P2) and (9 in P2):
        winer = 2 
    
    if winer == 1:
        messagebox.showinfo(title='cong.',message='Player 1 is winer')
        abdo.quit()   
    if winer == 2:
        messagebox.showinfo(title='cong.',message='Player 2 is winer')
        abdo.quit()
    if len(P1) + len(P2) == 9:
        messagebox.showinfo(title='Draw', message='The game is a draw!')
        abdo.quit()
    


def SetLayout(id , text):
    if (id==1):
        bu1.config(text=text)
        bu1.state(['disabled'])
    elif (id==2):
        bu2.config(text=text)
        bu2.state(['disabled'])
    elif (id==3):
        bu3.config(text=text)
        bu3.state(['disabled'])
    elif (id==4):
        bu4.config(text=text)
        bu4.state(['disabled'])
    elif (id==5):
        bu5.config(text=text)
        bu5.state(['disabled'])
    elif (id==6):
        bu6.config(text=text)
        bu6.state(['disabled'])
    elif (id==7) :
        bu7.config(text=text)
        bu7.state(['disabled'])
    elif (id==8) :
        bu8.config(text=text)
        bu8.state(['disabled'])
    elif (id==9) :
        bu9.config(text=text)
        bu9.state(['disabled'])

def  otoplayer():
    global P1
    global P2
    T=[]
    if (((1 in P2) and (2 in P2)  and (((3 not in P1) and (3 not in P2)))) or
        ((1 in P2) and (3 in P2)  and (((2 not in P1) and (2 not in P2)))) or 
        ((3 in P2) and (2 in P2)  and (((1 not in P1) and (1 not in P2)))) or 
        ((4 in P2) and (5 in P2)  and (((6 not in P1) and (6 not in P2)))) or 
        ((4 in P2) and (6 in P2)  and (((5 not in P1) and (5 not in P2)))) or
        ((5 in P2) and (6 in P2)  and (((4 not in P1) and (4 not in P2)))) or
        ((7 in P2) and (8 in P2)  and (((9 not in P1) and (9 not in P2)))) or
        ((7 in P2) and (9 in P2)  and (((8 not in P1) and (8 not in P2)))) or
        ((8 in P2) and (9 in P2)  and (((7 not in P1) and (7 not in P2)))) or
        ((1 in P2) and (4 in P2)  and (((7 not in P1) and (7 not in P2)))) or 
        ((1 in P2) and (7 in P2)  and (((4 not in P1) and (4 not in P2)))) or 
        ((4 in P2) and (7 in P2)  and (((1 not in P1) and (1 not in P2)))) or 
        ((2 in P2) and (5 in P2)  and (((8 not in P1) and (8 not in P2)))) or 
        ((2 in P2) and (8 in P2)  and (((5 not in P1) and (5 not in P2)))) or 
        ((5 in P2) and (8 in P2)  and (((2 not in P1) and (2 not in P2)))) or 
        ((3 in P2) and (6 in P2)  and (((9 not in P1) and (9 not in P2)))) or
        ((3 in P2) and (9 in P2)  and (((6 not in P1) and (6 not in P2)))) or
        ((6 in P2) and (9 in P2)  and (((3 not in P1) and (3 not in P2)))) or
        ((1 in P2) and (5 in P2)  and (((9 not in P1) and (9 not in P2)))) or 
        ((1 in P2) and (9 in P2)  and (((5 not in P1) and (5 not in P2)))) or 
        ((5 in P2) and (9 in P2)  and (((1 not in P1) and (1 not in P2)))) or 
        ((3 in P2) and (5 in P2)  and (((7 not in P1) and (7 not in P2)))) or 
        ((3 in P2) and (7 in P2)  and (((5 not in P1) and (5 not in P2)))) or      
        ((5 in P2) and (7 in P2)  and (((3 not in P1) and (3 not in P2)))) ):
        x = ERI()
        BuClick(x)
    elif(((1 in P1) and (2 in P1)  and (((3 not in P1) and (3 not in P2)))) or 
         ((1 in P1) and (3 in P1)  and (((2 not in P1) and (2 not in P2)))) or 
         ((3 in P1) and (2 in P1)  and (((1 not in P1) and (1 not in P2)))) or 
         ((4 in P1) and (5 in P1)  and (((6 not in P1) and (6 not in P2)))) or 
         ((4 in P1) and (6 in P1)  and (((5 not in P1) and (5 not in P2)))) or 
         ((5 in P1) and (6 in P1)  and (((4 not in P1) and (4 not in P2)))) or 
         ((7 in P1) and (8 in P1)  and (((9 not in P1) and (9 not in P2)))) or 
         ((7 in P1) and (9 in P1)  and (((8 not in P1) and (8 not in P2)))) or 
         ((8 in P1) and (9 in P1)  and (((7 not in P1) and (7 not in P2)))) or 
         ((1 in P1) and (4 in P1)  and (((7 not in P1) and (7 not in P2)))) or 
         ((1 in P1) and (7 in P1)  and (((4 not in P1) and (4 not in P2)))) or 
         ((4 in P1) and (7 in P1)  and (((1 not in P1) and (1 not in P2)))) or 
         ((2 in P1) and (5 in P1)  and (((8 not in P1) and (8 not in P2)))) or 
         ((2 in P1) and (8 in P1)  and (((5 not in P1) and (5 not in P2)))) or 
         ((5 in P1) and (8 in P1)  and (((2 not in P1) and (2 not in P2)))) or     
         ((3 in P1) and (6 in P1)  and (((9 not in P1) and (9 not in P2)))) or
         ((3 in P1) and (9 in P1)  and (((6 not in P1) and (6 not in P2)))) or 
         ((6 in P1) and (9 in P1)  and (((3 not in P1) and (3 not in P2)))) or
         ((1 in P1) and (5 in P1)  and (((9 not in P1) and (9 not in P2)))) or 
         ((1 in P1) and (9 in P1)  and (((5 not in P1) and (5 not in P2)))) or 
         ((5 in P1) and (9 in P1)  and (((1 not in P1) and (1 not in P2)))) or 
         ((3 in P1) and (5 in P1)  and (((7 not in P1) and (7 not in P2)))) or 
         ((3 in P1) and (7 in P1)  and (((5 not in P1) and (5 not in P2)))) or      
         ((5 in P1) and (7 in P1)  and (((3 not in P1) and (3 not in P2)))) ):
        x = abdrzak()
        BuClick(x)
    else:
     for cell in range(9):
        if cell + 1 not in P1 and cell + 1 not in P2:
            T.append(cell + 1)
     if len(T) > 0:
        x = randint(0, len(T) - 1)
        BuClick(T[x])
def ERI():
    global P1
    global P2
    if (((1 in P2) and (2 in P2)  and (((3 not in P1) and (3 not in P2)))) or ((5 in P2) and (7 in P2)  and (((3 not in P1) and (3 not in P2)))) or ((6 in P2) and (9 in P2)  and (((3 not in P1) and (3 not in P2))))):
            A = 3
    elif ((1 in P2) and (3 in P2)  and (((2 not in P1) and (2 not in P2)))) or  ((5 in P2) and (8 in P2)  and (((2 not in P1) and (2 not in P2)))):
            A = 2
    elif (((3 in P2) and (2 in P2)  and (((1 not in P1) and (1 not in P2)))) or ((5 in P2) and (9 in P2)  and (((1 not in P1) and (1 not in P2)))) or ((4 in P2) and (7 in P2)  and (((1 not in P1) and (1 not in P2))))):
            A = 1
    elif (((4 in P2) and (5 in P2)  and (((6 not in P1) and (6 not in P2)))) or  ((3 in P2) and (9 in P2)  and (((6 not in P1) and (6 not in P2))))):
            A = 6
    elif (((4 in P2) and (6 in P2)  and (((5 not in P1) and (5 not in P2)))) or ((3 in P2) and (7 in P2)  and (((5 not in P1) and (5 not in P2)))) or ((1 in P2) and (9 in P2)  and (((5 not in P1) and (5 not in P2)))) or ((2 in P1) and (8 in P1)  and (((5 not in P1) and (5 not in P2))))):
            A = 5
    elif (((5 in P2) and (6 in P2)  and (((4 not in P1) and (4 not in P2)))) or ((1 in P2) and (7 in P2)  and (((4 not in P1) and (4 not in P2))))):
            A = 4
    elif (((7 in P2) and (8 in P2)  and (((9 not in P1) and (9 not in P2)))) or ((1 in P2) and (5 in P2)  and (((9 not in P1) and (9 not in P2)))) or ((3 in P2) and (6 in P2)  and (((9 not in P1) and (9 not in P2))))):
            A = 9
    elif (((7 in P2) and (9 in P2)  and (((8 not in P1) and (8 not in P2)))) or ((2 in P2) and (5 in P2)  and (((8 not in P1) and (8 not in P2))))):
            A = 8 
    elif (((1 in P2) and (4 in P2)  and (((7 not in P1) and (7 not in P2)))) or ((3 in P2) and (5 in P2)  and (((7 not in P1) and (7 not in P2)))) or ((8 in P2) and (9 in P2)  and (((7 not in P1) and (7 not in P2))))):
            A = 7
    return A
     
def abdrzak():
    global P1
    global P2
    if (((1 in P1) and (2 in P1)  and (((3 not in P1) and (3 not in P2)))) or ((5 in P1) and (7 in P1)  and (((3 not in P1) and (3 not in P2)))) or ((6 in P1) and (9 in P1)  and (((3 not in P1) and (3 not in P2))))):
            x = 3
    elif ((1 in P1) and (3 in P1)  and (((2 not in P1) and (2 not in P2)))) or  ((5 in P1) and (8 in P1)  and (((2 not in P1) and (2 not in P2)))):
            x = 2
    elif (((3 in P1) and (2 in P1)  and (((1 not in P1) and (1 not in P2)))) or ((5 in P1) and (9 in P1)  and (((1 not in P1) and (1 not in P2)))) or ((4 in P1) and (7 in P1)  and (((1 not in P1) and (1 not in P2))))):
            x = 1
    elif (((4 in P1) and (5 in P1)  and (((6 not in P1) and (6 not in P2)))) or  ((3 in P1) and (9 in P1)  and (((6 not in P1) and (6 not in P2))))):
            x = 6
    elif (((4 in P1) and (6 in P1)  and (((5 not in P1) and (5 not in P2)))) or ((3 in P1) and (7 in P1)  and (((5 not in P1) and (5 not in P2)))) or ((1 in P1) and (9 in P1)  and (((5 not in P1) and (5 not in P2)))) or ((2 in P1) and (8 in P1)  and (((5 not in P1) and (5 not in P2))))):
            x = 5
    elif (((5 in P1) and (6 in P1)  and (((4 not in P1) and (4 not in P2)))) or ((1 in P1) and (7 in P1)  and (((4 not in P1) and (4 not in P2))))):
            x = 4
    elif (((7 in P1) and (8 in P1)  and (((9 not in P1) and (9 not in P2)))) or ((1 in P1) and (5 in P1)  and (((9 not in P1) and (9 not in P2)))) or ((3 in P1) and (6 in P1)  and (((9 not in P1) and (9 not in P2))))):
            x = 9
    elif (((7 in P1) and (9 in P1)  and (((8 not in P1) and (8 not in P2)))) or ((2 in P1) and (5 in P1)  and (((8 not in P1) and (8 not in P2))))):
            x = 8 
    elif (((1 in P1) and (4 in P1)  and (((7 not in P1) and (7 not in P2)))) or ((3 in P1) and (5 in P1)  and (((7 not in P1) and (7 not in P2)))) or ((8 in P1) and (9 in P1)  and (((7 not in P1) and (7 not in P2))))):
            x = 7
    return x

abdo.mainloop()