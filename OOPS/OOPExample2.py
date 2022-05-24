class A:
	def add(self):
		print("Hello Add")

a=b=c=A()
print("type(a) : ",type(a))
print("Name is : ",A.__name__)
print("Module name of A : ",A.__module__)

#print("a.__name__: ",a.__name__)
print("Module Name through object: ",a.__module__)

print("A: ",A)
print("a: ",a)
print("b: ",b)