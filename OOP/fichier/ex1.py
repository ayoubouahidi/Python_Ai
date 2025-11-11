f = open("C:/Users/Lenovo/Desktop/POO/fichier/fichier.txt", 'w')
for i  in range(10):
    f.write(str(i))
f.close()

f = open("C:/Users/Lenovo/Desktop/POO/fichier/fichier.txt",'r')
print(f.read())
f.close()