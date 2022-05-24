#Append + Read (a+) mode
f=open("Test4.txt","a+")
f.write("Hello Python")
print("Data written in appned + read mode")
f.seek(0)
print("f.read(): ",f.read())
f.close()