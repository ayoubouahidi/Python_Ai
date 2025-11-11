l=[]
for i in range(2):
    d={"code":int(input("entrer code :")),"type":input("entrer type :"),"surface":input("entrer nom :"),"nombre":int(input("entrer nombre :"))}
    l.append(d)


for i in range(len(l)):
    if l[i]["type"]=="villa":
        pg=l[0]["nombre"]
        p=0
        if l[i]["nombre"]>pg:
            pg=l[i]["nombre"]
            p=i
print("le plus grande villa est du code : ",l[p]["code"])
        