class Calculate:
	def add(self,a,b):
		print("Sum= ",a+b)

	def diff(self,a,b):
		print("Diff= ",a-b)

c=Calculate()
c.add(10,45)
c.diff(45,10)

print("Calculate.__dict__ : ",Calculate.__dict__)
print("c.__dict__ : ",c.__dict__)