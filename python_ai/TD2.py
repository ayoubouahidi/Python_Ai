# ex 01 

tab = [1,2,3,4,5,6,7,8,9]

i = 0
while (i < len(tab)):
    print (tab[i])
    i = i + 1

i = 0

while (i < len(tab)):
    print (tab[i], end="/")
    i = i + 1

print(max(tab), min(tab))
i = 0

count  = 0
while (i < len(tab)):
    if (tab[i] % 3 == 0):
        count = count + 1
    i = i + 1

i = 0
somme = 0
while (i < len(tab)):
    somme = somme + tab[i]
    i = i + 1

i = 0
paires = 0 
while (i < len(tab)):
    if  (tab[i] % 2 == 0):
        paires = paires + 1
    i = i + 1


moyenne = 0
i = 0
while (i < len(tab)):
    moyenne = moyenne + tab[i]
    moyenne = moyenne // len(tab)
    i = i + 1

i = 0
produit = 1
while (i < len(tab)):
    produit = produit * tab[i]
    i = i + 1
print(produit)

produit_2 = 0
for i in range(0 , len(tab)):
    if (tab[i] >= 50 and tab[i] <= 70):
        produit_2 = produit_2  * tab[i]
    i = i + 1


i = len(tab) -1 
while (i != 0):
    print(tab[i])
    i = i - 1


#ex2

# def reverse_tab(tab):
#     i = len(tab) - 1
#     rev_tab = []
#     j = 0
#     while(i != 0):
#         rev_tab.append(tab[i])
#         i = i - 1
#     return rev_tab

# print (reverse_tab(tab))

print(tab[::-1])

#ex 3 

list_3 = [8,3,15,4,1,9,20,7]
list_3.sort()
print(list_3)

list_4 = ["Rabat", "Casablanca" , "Fes", "Berkane", "Taza"]
list_4.sort(reverse=True)
print(list_4)

#ex4 

M = []
for z in range(3):
    
    for x in range(3):
        for y in range(3):
            