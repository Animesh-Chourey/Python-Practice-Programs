# Here in this example data can be accessed by the user

class Person:
	name=None
	age=None

	def show(self):
		print("Name= ",self.name)
		print("Age= ",self.age)

p=Person()
p.show()
p.name="Amit"
p.age=22
p.show()