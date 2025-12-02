# x = int(input("enter un nombre :"))
# y = int(input("enter un nombre :"))
# z = int(input("enter un nombre :"))
# m = int(input("enter un nombre :"))

# s = x + y + z+  m

# i = 0
# while (i < 4)
#     m = int(input("enter un nombre :"))
#     s+=m
# l = x 
# x = l + y + z + m 
# print(f"a -) {s} \n b -) {x}")


# ex3 
# n = int(input("enter n :"))

# i = 1
# s = 0
# while(n > 1):
#     s += 1 / n
#     n-=1

# print(s)

# ex4

# n =  int(input("enter n :"))
# X= float(input("enter X :"))
# res = 0
# while (n >= 0):
#     An = int(input("enter coeffision :"))
#     res += An *( X ** n)
#     n-=1

# print(X)


# ex 5
# def fibomacci(n):
#     if (n < 2):
#         return 1
#     return fibomacci(n - 1) + fibomacci(n - 2)


# # n =  int(input("enter n :"))
# print(fibomacci(5))


# # ex 6 
# n =  int(input("enter n :"))

# i = 1

# if n <= 1:
#     print(f"{n} n'est pas premier")
# else:
#     est_premier = True
#     for i in range(2, n):
#         if (n % i == 0):
#             print("n'est pas premier")
#             est_premier = False
#             break;
#         # i = i - 1
#     if est_premier:
#         print("le nombre est premier")


# ex 07

# for i in range(0 , 101):
#     premier = True
#     for j in range(2, i):
#         if (i % j == 0):
#             # print("n'est pas premier")
#             premier = False
#             break;
#         # i = i - 1
#     if premier:
#         print(f"{i}")

# ex 08
#  
# 1111    occ = 4

# n = int(input("enter un nombre :"))
# chiffre = int(input("enter un chiffre :"))
# check = 0
# occ = 0

# while(n != 0):
#     check = n % 10
#     n = n // 10
#     if (check == chiffre):
#         occ = occ + 1

# print(f"occ est {occ}")

# ex 09

# n = int (input("entrer un nombre : "))
# p  = int (input("entrer le degres :"))
# m = n
count = 0
check = 0
res = 0
def calcul_len(n):
    count = 0
    while(n != 0):
        n = n // 10
        count = count + 1
    return count


# while(n != 0):
#         # count = count + 1
#     check = n % 10
#     n = n // 10
#     res = res + (check ** p)
#     # print(res)
# if (res == m):
#     print("le nombre est narci")
# else :
#     print("n'est pas narci")



# for i in range(10, 1000001):
#     N = calcul_len(i)
#     m = i
#     res = 0
#     while(i != 0):
#         # count = count + 1
#         check = i % 10
#         i = i // 10
#         res = res + (check ** N)
#     # print(res)
#     if (res == m):
#         print(f"le nombre est narci {m}")
    


# 10


# j = int(input("enter le jour"))
# m = int(int(input("enter le mois")))
# anne = int (input("enter l anne"))

# def check_if(anne):
#     if (anne % 4 == 0 || anne % 4 == 0 || anne % 4 == 0 ||anne % 4 == ):
#         return True
#     return False

# if (m == 2):
#     if (check_if(anne)):
#         if (j == 28):
#             j = 1
#         elif (j == 27):
#             j = 2
# if (m == 1 or m == 3 or m == 5 or m == 7 or m == 8 or m == 10 or m == 12 ):
#     if (j == 31) :
#         j = 2
#     elif ( j == 30):
#         j = 2
#     j += 2
# else :
#     if (j == 30) :
#         j =  2
#     j += 2
# print(f"j ({j}) m ({m}) anne ({anne}) ")


# n = int(input("entrer :"))
# result = 0
# while(n == 0):
#     result = n % 10
#     n = 


