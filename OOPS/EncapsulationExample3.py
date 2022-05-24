#Encapsulation through constructor

class Person:
	__name=None
	__age=None

	def __init__(self,n,a):
		self.__name=n
		self.__age=a

	def getName(self):
		return self.__name

	def getAge(self):
		return self.__age

p=Person("Amit",43)
print("Name: ",p.getName())
print("Age: ",p.getAge())

print(p)