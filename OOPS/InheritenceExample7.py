class Test:
	name=None
	def __init__(self,name):
		self.name=name

	def __str__(self):
		return self.name

t=Test("Ani")
print(t)