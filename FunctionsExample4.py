#Keyword Arg Function
def show(name,age):
	print("Name: ",name)
	print("Age: ",age)

show("Niki",32)
show("Miki",44)
#show(25,"Chiki") #Since here name can get stored into age and vice versa so for that keyword arg functions are used
show(age=25,name="Chiki")