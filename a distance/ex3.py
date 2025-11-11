# l =[1,2,3,4,4,5,5]
# list_sansdouble=[]
# for i in l :
#     if i not in list_sansdouble :
#         list_sansdouble.append(i)
# print(list_sansdouble)
    
    #qustion 2
def minmax(l):
    mi = min(l)
    ma = max(l)
    return f"({mi},{ma})"

l= [1,2,3,4,9]
print(minmax(l))



