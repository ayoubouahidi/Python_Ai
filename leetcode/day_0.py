class solution:
  def twosum():
   t=[6,3,4,5,6]
   target=9
   hashm = {} # index : value 

   for i,element in enumerate(t):
      diff = target - element
      if diff in hashm :
        return [hashm[diff],i]
      hashm[element]=i
   return
  
  print(twosum())


    