#1
f = open("EFM-ALGO.txt","w")
ph = "JZE NE SUIS PAS UN CRACK EN INFORMATIQUE LOIN DE LA MAIS IL N Y A PAS QUE LES MECANICIENS QUI SACHENT CONDUIRE UNE VOITURE"
f.write(ph)

#2
def crypte(text):
    text_cr = ""
    for i in text:
        asc= ord(i)
        if asc==90 :
            asc =65
            
        
        let=chr(asc+1)
        text_cr+=str(let)
    return text_cr


f=open("EFM-ALGO.txt","r")
con=f.read()
con_cry = crypte(con)

print(con_cry)