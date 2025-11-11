#methode 1
A  = int(input("entrer votre numero que vous voulez echanger : "))
B = int(input("entrer votre numero que vous voulez echanger : "))

C = A
A = B
B = C
print(f"num1 egale : {A}")
print(f'num2 egale : {B}')
#methode 2

A  = int(input("entrer votre numero que vous voulez echanger : "))
B = int(input("entrer votre numero que vous voulez echanger : "))

A = A + B
B = A - B
A = A - B

print(f"num1 egale : {A}")
print(f'num2 egale : {B}')


