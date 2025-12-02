# /* ************************************************************************** */
# /*                                                                            */
# /*                                                        :::      ::::::::   */
# /*   collection                                          :+:      :+:    :+:   */
# /*                                                    +:+ +:+         +:+     */
# /*   By: hamel-yo <hamel-yo@student.42.fr>          +#+  +:+       +#+        */
# /*                                                +#+#+#+#+#+   +#+           */
# /*   Created: 2024/11/08 07:19:47 by hamel-yo          #+#    #+#             */
# /*   Updated: 2024/11/21 09:42:59 by hamel-yo         ###   ########.fr       */
# /*                                                                            */
# /* ************************************************************************** */

#  ********** tuple **********


# t1 = tuple()
# t2 = (17, 18 , 16 , 19)
# t3 = ("ayoub", "ouahidi", 18)
# t4 = 17, 18 , 19 
# t5 = (17,)
# t6 = (17)  # NOT A TUPLE 
# t7 = (17, 18 , 18.5) * 3 # repeat 3 times 





# print(t2 ^ t4)
# ******************************


#  ********** set(ensemple) **********

# s1 = set()  # creer une set vide 
# s2 = {"ayoub", 18, 17}
# s3 = {1,2,3,18}
# s4 = {19, 18 , 20 , 17}
# s4.add(30)
# # # s3.remove(2) # supprime tout les 2
# # # s3.discard(3000)

# # A = {1, 2, 3,8,  4}
# # B = {3, 4, 5, 6}

# # # les operation disponibles dans set sont : - , | , & , ^ 
# # # elem = s3.pop()  
# print(s3)

# print(A - B) 

# ******************************




#  ********** LIST **********


# l1 = [17, 19, 18]
# l2 = [1,2,3,4,5,6,7]

# l2.append(17)
# l2.insert(1,18)
# # del l2[1:]
# # l1.sort()
# l3 = [n * 2 + 1 for n in range(1, 11)]

# print(sorted(l3))

# ******************************



l =[]
for i in range(3):
    m=[]
    for j in range(3):
        n = int(input("entrer un nombre :"))
        m.append(n)
    l.append(m)

for i in range(0, len(l)):
    for j in range(0, len(l)):
        print(l[i][j],end=", ")
    print()