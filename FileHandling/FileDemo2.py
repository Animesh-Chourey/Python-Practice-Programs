#Write+Read (w+) mode
f=open("Test2.txt","w+")
f.write("Hello Python")
f.write("\nWe are using write+read mode")
print("We are using write+read mode")

f.seek(0)
print("f.read():\n",f.read())
f.close()