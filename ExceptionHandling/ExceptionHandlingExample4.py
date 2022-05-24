#Different types of Exceptions

print("Start of program")
try:
	print("int('10')= ",int("10"))
	print("int('ten')= ",int("ten"))#Value Execption

except ValueError as e:
	print(e)

print("End of prog")