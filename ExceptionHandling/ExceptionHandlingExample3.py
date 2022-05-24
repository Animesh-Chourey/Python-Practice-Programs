#Different types of Exceptions

print("Start of the program")
try:
	a=10
	print("a= ",a)#b) #Name Exception
	
	l1=[10,20,30]
	print("l1[0]= ",l1[6]) #Index Exception 

except NameError:
	print("Name not found")
except IndexError:
	print("Index Out of Bound")
except Exception:
	print("Handle all Exceptions")
print("End of program")	