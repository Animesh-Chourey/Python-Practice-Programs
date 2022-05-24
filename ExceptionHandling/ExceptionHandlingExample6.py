print("Start of the program")
try:
	print("int('ten'): ",int("ten")) #ValueError
	print("len(22): ",len(22)) #TypeError

except TypeError or ValueError as e:
	print(e)

print("End of program")