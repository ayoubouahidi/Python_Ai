from random import randint
t= [1,2,3]
l = [1,2,3]
def addtwosum():
  stock = set()
  for i in range(5):
       stock.add(t[i]+l[i])
         
       
      # else:
      #    if t[i]+l[i] > 9 :
      #        return stock.add(0)
        

print(addtwosum())