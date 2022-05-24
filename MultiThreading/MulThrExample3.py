import time
from threading import *

def cube(lnum):
	for i in lnum:
		time.sleep(2)
		print("Cube= ",i*i*i)

def square(lnum):
	for i in lnum:
		time.sleep(2)
		print("Square= ",i*i)

l1=[1,2,3,4,5]
print("Thread.current_thread(): ",current_thread())
beginT=time.time()
print("Thread.current_thread(): ",current_thread())
t1=Thread(target=cube,args=(l1,))
t1.start()
print("Thread.current_thread(): ",current_thread())
t2=Thread(target=square,args=(l1,))
t2.start()
print("Thread.current_thread(): ",current_thread())
endT=time.time()
print("Total time taken: ",endT-beginT)