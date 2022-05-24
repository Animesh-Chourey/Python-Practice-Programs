#Default Arg Function
def showDetails(name,add,age=18):
	print("Name: ",name,end="\t")
	print("Address: ",add,end="\t")
	print("Age: ",age)

showDetails("ABC","Vijaynagar",20)
showDetails("XYZ","Palasiya")