l=4
for i in range(1,10):
	if i<=5:
		for j in range(5,i,-1):
			print(" ",end="")
		for k in range(1,(2*i)):
			if k%2==0:
				print(" ",end="")
			else:
				print("*",end="")
	else:
		for j in range(5,i):
			print(" ",end="")
		for k in range(12,l,-1):
			if k%2!=0:
				print(" ",end="")
			else:
				print("*",end="")
		l=l+2
	print()