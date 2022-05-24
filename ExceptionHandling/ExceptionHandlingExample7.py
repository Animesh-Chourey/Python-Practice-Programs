#finally Example
print("Start if the program")
try:
	d1={1:"ABC",2:"XYZ"}
	print("Value at 5: ",d1[5])

except KeyError:
	print("key not present")

finally:
	print("Always executes")

print("End of prog")