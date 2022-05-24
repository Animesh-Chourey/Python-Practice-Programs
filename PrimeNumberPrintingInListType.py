a=int(input("Enter the starting number: "))
b=int(input("Enter the ending range: "))
list1=[]
for i in range(a,b+1):
	flag=0
	for j in range(2,i):
		if i%j==0:
			flag=1
			break
	if flag==0:
		list1.append(i)

print("Prime Numbers in list: ",list1)