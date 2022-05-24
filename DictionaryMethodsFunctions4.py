d1={'A':89,'B':56,'C':45,'D':90,'E':"ABC"}

#keys method
key=d1.keys()
print("key= ",key)
print("type(key): ",type(key))

#values method
value=d1.values()
print("value= ",value)
print("type(value): ",type(value))

#items method
items=d1.items()
print("items= ",items)
print("type(items): ",type(items))

#iterate thorugh items
for i in d1.items():
	print("items: ",i)