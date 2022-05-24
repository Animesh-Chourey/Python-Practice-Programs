#Different types of Exceptions

print("Start of program")
try:
	print("len([10,20,30]): ",len([10,20,30]))
	print("len(34)= ",len(34))#TypeError

except TypeError as e:
	print(e)

print("End of program")