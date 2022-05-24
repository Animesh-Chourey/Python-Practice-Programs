#Call By Reference
def showList(mylist):
	mylist.append(34)
	print("mylist inside function= ",mylist)

mylist=[10,300]
showList(mylist)
print("List outside function: ",mylist)