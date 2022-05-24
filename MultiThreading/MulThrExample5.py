#Thread using inheritence
from threading import *

class MyThread(Exception):
	def display(self):
		for i in range(20):
			print("Child Thread")

obj=MyThread()
t=Thread(target=obj.display())
t.start()
for i in range(20):
	print("Main Thread")