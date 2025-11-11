f = open("c:/Users/Lenovo/Desktop/python/file/infos.txt",'r')
# while True:
    
#     ch=f.readline()
#     l=ch.split(',')
#     print(l)
# #     l="nom : "+ch.split(",")
    
# #     print(str(l))

# #     if f.read()=='':
# #         break
# # f.close()
#     # ch = f.readline()
#     # for i in ch :
#     #  a = f.read()

#     #  l = a.split(",")
#     #  print("le nom :",l)
#     if f.read()=='':
#         break
for line in f:
    infos = line.split(',')


    # if infos[1][-1]=='\n':
    #     infos[1]=infos[1][-1]

    p = return f''