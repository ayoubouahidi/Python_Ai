
n = input("donner un caractere  :")
s = n
cmp =1
if n =='.':
    print("le . est au debut alors le programme est annuler ")

else:
     while ( n != "."):
        n = input("donner un caractere :")
        if n == s :
          cmp +=1
     print("on a",s,cmp,"fois")
