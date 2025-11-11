import math


def en_forme_heure(sec):

    heure = 0
    minute = 0
    
    if (sec >= 3600):
        heure = sec // 3600
        sec = sec - (heure * 3600)

    # print("im here")
    if (sec >= 60):
        minute = sec // 60
        sec = sec - (minute * 60)
    print(f"{heure} h, {minute} min, {sec} sec")

sec = int(input("entrer en sec :"))
en_forme_heure(sec)
