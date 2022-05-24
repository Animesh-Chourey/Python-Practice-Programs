#Creating a User Defined Exception

class AgeException(Exception):
	def __init__(self,value):
		self.value=value

age=int(input("Enter your age: "))
if age>18:
	print("Valid Age")
else:
	raise AgeException("Invalid Age")

print("End of program")