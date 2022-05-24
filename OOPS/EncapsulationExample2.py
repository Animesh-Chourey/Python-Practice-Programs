#Proper Encapsulation

class Person:
	__name=None
	__age=None

	def setAge(self,age):
		self.__age=age

	def setName(self,name):
		self.__name=name

	def getAge(self):
		return self.__age

	def getName(self):
		return self.__name

p=Person()
p.setName("Amit")
p.setAge(22)
print("Name= ",p.getName())
print("Age= ",p.getAge())
print("Name= ",p.__name)