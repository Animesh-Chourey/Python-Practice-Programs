for i in range(1,6):
	for j in range(5,i,-1):
		print(" ",end="")
	for k in range(1,(2*i)): #here 2*i is used and not 2*i-1 because loop runs iterates till -1 position
		if k%2==0:
			print(" ",end="")
		else:
			print("*",end="")
	print()