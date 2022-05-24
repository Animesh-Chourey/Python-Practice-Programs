f=int(input("Enter first element : "))
l=int(input("Enter last elemnet : "))
while f<=l:
	n=2
	flag=0
	while n<f/2:
		if f%n==0:
			flag=1
			break
		n+=1
	if flag==0:
		print(f,"is prime no")
	f+=1	