file = open("ayoub.txt","w")
con="ANA,SMITI,AYOUB"
file.write(con+'\n')
for i in range(10):

                file.write( 'ligne ' + str(i+1) + '\n')

file.close()
file=open('ayoub.txt','r')
print(file.readlines())
file.close()

file = open('ayoub.txt','r')
ch = file.readline()
cmp=0
while ch !='':
        cmp+=1
        ch=file.readline()
file.close()
print("le nombres des lignes est :",cmp)


file = open("ayoub.txt","r")
a1=file.readline()

t= a1.split(",")
t= a1.strip()
print(t)


