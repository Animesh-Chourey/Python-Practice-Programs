# List can also concatenate
l1=[10,20,"Hello"]
l2=["Hi",34.23,58+4j]
l3=l1+l2
print("l3: ",l3)

#Immutable Concept
print("id of l3: ",id(l3))
l3[3]="Hey"
print("l3 after altering the data: ",l3)
print("id of l3 ater altering the data: ",id(l3))