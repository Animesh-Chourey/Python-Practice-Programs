#If we want to pass any number of variables to the function

def any_number_of_variable(*args):
	sum =0
	for i in args:
		sum += i

	return sum

print("Sum = ",any_number_of_variable(3,4,5,6,7))
print("Sum = ",any_number_of_variable(3,4,5,6,7,8))
print("Sum = ",any_number_of_variable(3,4,5,6,7,9,7,234))