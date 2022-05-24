#Else Clause example
print("Start of the program")
try:
	print(int("Hello"))
	print("Stat 1")

except ValueError or TypeError as e:
	print(e)

else:
	print("End of prog")

finally:
	print("Always excute")