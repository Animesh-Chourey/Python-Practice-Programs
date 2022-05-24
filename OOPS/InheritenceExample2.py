#Use of super() function

class Person:
	name="Amit"
	age=21

	def show(self):
		print("Name: ",self.name)
		print("Age: ",self.age)

class Student(Person):
	stid=101

	def show(self):
		super().show()
		print("Student's ID: ",self.stid)


class Employee(Person):
	empid=201

	def show(self):
		super().show()
		print("Employee ID: ",self.empid)

print("Student Object Created")
s=Student()
s.show()
print("Employee Object Created")
e=Employee()
e.show()