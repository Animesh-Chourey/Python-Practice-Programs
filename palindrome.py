num=int(input("Enter a number= "))
a=int(num/100)
b=int((num%100)/10)
c=num%10
rev=a+10*b+100*c
print("Rev= ",rev)