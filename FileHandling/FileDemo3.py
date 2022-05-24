#Read (r) mode
f=open("Test3.txt","r")
#f=open("ab.txt","r")
print("f.read():\n",f.read())
f.close()
print("f.name: ",f.name)
print("f.mode: ",f.mode)
print("f.closed: ",f.closed)