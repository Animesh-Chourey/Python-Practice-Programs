import threading
def t1():
	print("Child Class")

t=threading.Thread(target=t1)
t.start()
print("t.getName(): ",t.getName())
t1=threading.Thread(target=t1)
t1.start()
print("t1.getName(): ",t1.getName())