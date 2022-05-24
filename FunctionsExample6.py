#var-arg function
def sum(*data):
	sum=0
	for i in data:
		sum+=i
	print("Sum= ",sum)

sum(100,200,300)
sum(1,3,5,7)
sum(20,70)