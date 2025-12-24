import random as rd

# L = []
# N = int(input("entrer un nombre "))
# for i in range(N):
#     v = rd.uniform(-200, 200)
#     L.append(v)


# F = False
# inf = len(L)


# L = [5, 6, 1]
# # L.sort()
# pt = L[0]
# # print (min(L))
# i = 0
# while (i < len(L)):
#     if (pt > L[i]):
#         pt = L[i]
#     i += 1
# print(pt)


# def bubble_sort(L):
#     n = len(L)
#     for i in range(n):
#         for j in range(0, n - i - 1):
#             if L[j] > L[j + 1]:
#                 L[j], L[j + 1] = L[j + 1], L[j]
#     return L

A = [1,4,6,1]
B = [6,9,1,3,5]
result = []

i = 0
j = 0

A.sort()
B.sort()
while (i < len(A)):
    if (A[i] > B[i + 1]):
        result[i] = A[i]
    elif (A[i + 1] > B[i]):
        result[i] = B[i]
    
    
        


