t = [1,2,3,4,5,6,7,8,1]
def containduplicate():
    hashm = set()
    for element in t:
        if element in hashm:
            return True
        hashm.add(element)
    return False


#     t=[1,2,3,4,5,6,7,1]
#     n = len(t)
    
#     for i in range(n):
#         for j in range(i+1,n):
#             if t[i]==t[j]:
#                 return True
#     return False
#   ***********************8
# print(containduplicate())
# def chatboot():
#     n = len(t)
#     for i in range(n):
#         for j in range(i+1,n):
#             if t[i]==t[j]:
#                 return True
#     return False
# print(chatboot())
#*******************
    # seen = set()
    # for elements in t:
    #     if elements in seen:
    #         return True
    #     seen.add(elements)
    # return False
print(containduplicate())

        

