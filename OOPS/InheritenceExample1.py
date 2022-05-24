#Single Level Inheritence

class Person:
	name="Amit"
	age=21

	def show(self):
		print("Name: ",self.name)
		print("Age: ",self.age)

class Student(Person):
	stid=101

	def show(self):
		print("Derived Class show()")
		print("Name: ",Person.name)
		print("Age: ",Person.age)
		print("Student's ID: ",self.stid)

s=Student()
s.show()