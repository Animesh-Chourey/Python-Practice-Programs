for i in range(1,10):
	if i<=5:
		for j in range(1,i+1):
			print("*",end="")
	else:
		for k in range(10,i,-1):
			print("*",end="")
	print()