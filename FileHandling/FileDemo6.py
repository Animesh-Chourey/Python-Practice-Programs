#Binary Mode Example
f=open("Naru.jpg","rb")
f1=open("NewNaruCopy.png","ab")
f2=open("NewNaruCopy33.png","ab")
a=f.read()
print("a= ",a)
f1.write(a)
print("Copy Created")