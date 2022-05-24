#Handle those user defined exception
class AgeException(Exception):

	def __init__(self,value):
		self.value=value

age=int(input("Enter your age: "))
if(age>18):
	print("Valid Age")
else:
	try:
		raise AgeException("Invalid Age")
	except AgeException as e:
		print(e)

print("End of prog")