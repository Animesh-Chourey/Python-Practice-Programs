set1={45,90+5j,True,10.74,"Hello",99,62.85}
print("set1: ",set1)

#remove method
set1.remove(99)
print("set1 after remove: ",set1)
#set1.remove(99) If element does not exist remove method will give an error

#discard method
set1.discard(62.85)
print("set1 after discard: ",set1)
#set1.discard(62.85) If element does not exist discard method will not give an error