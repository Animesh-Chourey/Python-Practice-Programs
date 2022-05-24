#Consructor Overloading is not supported

class A:
	def __init__(self):
		print("this is default cons")

	def __init__(self,a,b):
		print("This is para cons")

a=A()
a1=A(10,20)