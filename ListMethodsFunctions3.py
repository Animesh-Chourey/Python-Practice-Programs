#copy method
list1=[23,67,45,78,90]
print("lsit1: ",list1)
newlist=list1.copy()
print("newlist: ",newlist)
print("id(list1): ",id(list1))
print("id(newlist): ",id(newlist))

#remove method
list2=[23,67,45,78,90,45]
print("list2: ",list2)
list2.remove(45)
print("list2 after remove: ",list2)

#clear method
list1.clear()
print("list1 after clear: ",list1)