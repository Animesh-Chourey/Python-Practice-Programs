#Para Constructor

class Test:
	def __init__(self,a,b):
		self.a=a
		self.b=b

	def show(self):
		print("a= ",self.a)
		print("b= ",self.b)

t=Test(10,20)
t.show()