#Thread using Class
from threading import *
class MyThread(Exception):
	def display(self):
		for i in range(20):
			print("Child Thread")

obj=MyThread()
t1=Thread(target=obj.display())
t1.start()
for i in range(20):
	print("Main Thread")