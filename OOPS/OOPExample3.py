class A:
	def show(self):
		print("Hello Show")

a=A()

print("Base class name of class A: ",A.__base__)
#print("Base class name of class A: ",a.__base__)

print("Module Name of int : ",int.__module__)
print("Base class name of int: ",int.__base__)

print("Module Name of object class : ",object.__module__)
print("Base class name of object class : ",object.__base__)

print("A.__dict__ : ",A.__dict__)
print("a.__dict__ : ",a.__dict__)