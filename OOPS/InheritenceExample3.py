class Person:
	name= None
	age= None
	
	def __init__(self,n,a):
		self.name=n
		self.age=a
	
	def show(self):
		print("Name is ",self.name)
		print("Age is ",self.age)

class Student(Person):
	stid=None
	
	def __init__(self,n,a,si):
		self.name=n
		self.age=a
		self.stid=si
	def show(self):
		super().show()
		print("Id is ",self.stid)

class Employee(Person):
	empid=None
	def __init__(self,n,a,eid):
		self.name=n
		self.age=a
		self.eid=eid
	def show(self):
		super().show()
		print("Id is ",self.empid)

s= Student("amit",12,'a12')
s.show()
e=Employee("Rohan",34,'r12')
e.show()
