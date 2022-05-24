f=int(input("Enter first element: "))
l=int(input("Enter last element: "))
for a in range(f,l+1):
	flag=0
	for b in range(2,a):
		if a%b==0:
			flag=1
			break
	if flag==0:
		print(a,"is prime")
