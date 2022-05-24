#super() function with Constructor

class Person:
	name=None
	age=None

	def __init__(self,name,age):
		self.age=age
		self.name=name

	def show(self):
		print("Name: ",self.name)
		print("Age: ",self.age)

class Student(Person):
	sid=None

	def __init__(self,name,age,sid):
		super().__init__(name,age)
		#Person.__init__(self,name,age)  #We can also call constructor of base class by the name of base class name and in the parameter self is also used
		self.sid=sid

	def show(self):
		super().show()
		print("Student's Id: ",self.sid)

class Employee(Person):
	eid=None

	def __init__(self,name,age,eid):
		super().__init__(name,age)
		#Person.__init__(self,name,age)  #We can also call constructor of base class by the name of base class name and in the parameter self is also used
		self.eid=eid

	def show(self):
		super().show()
		print("Employee's Id: ",self.eid)

print("Student Object Created\n")
st=Student("Ani",21,1001)
st.show()

print("\nEmployee Object Created\n")
em=Employee("Sachin",34,245)
em.show()