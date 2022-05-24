#Factorial of anumber using recursion
def factorial(x):
	if x==1:
		return 1
	else:
		return x*factorial(x-1)

a=int(input("Enter a number: "))
print("Factorial of %d= %d"%(a,factorial(a)))