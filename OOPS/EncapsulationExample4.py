class Person:
	__name= None
	__age=None
	city="Indore"

	def __init__(self,n,a):
		self.__name= n
		self.__age=a

	def getName(self):
		return self.__name
	
	def getAge(self):
		return self.__age

p= Person("Sumit",10)
p1= Person("Amit",13)

print(p.getName())
print(p.getAge())
print(p.city)

print(p1.getName())
print(p1.getAge())
print(p1.city)
