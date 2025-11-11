from employer import Employer

em1 = Employer(1,1,"safi",1,"ku",2000)
em2 = Employer(2,2,"safi",2,"ku",2000)
em1.affiche()
em2.affiche()
if em1.compareNum(em2):
    print("le deuxiemme est le plus grand")
else:
    print("le premier est le plus grand")

if em1.salaireCompare(em2)==1:
    print("employer1 est le plus garnd")
elif em1.salaireCompare(em2)==-2:
    print("l'employer 2 est le plus grand salaire ")
else:
    print("ont le meme salaire .")

