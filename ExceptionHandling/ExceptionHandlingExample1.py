print("Statement 1")
a=100
#b=2
b=0 #Number cannot be zero
print("a= ",a)
print("b= ",b)
try:
	c=a/b
	print("Division = ",c)
except ZeroDivisionError:
	print("Number cannot be divided by zero")
print("End of program")