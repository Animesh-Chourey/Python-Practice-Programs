#Default Constructor

class Test:
	#a=23
	#b=2332

	def __init__(self):
		self.a=None
		self.b=None
	def show(self):
		print("a= ",self.a)
		print("b= ",self.b)
		

t= Test()
t.show()
t.a=11
t.b=56
t.show()
print("Test.__dict__= ",Test.__dict__)
print("t.__dict__= ",t.__dict__)