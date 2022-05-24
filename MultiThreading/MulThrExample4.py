#MultiThreading through function
from threading import *
def display():
	for i in range(20):
		print("Child Thread")

t=Thread(target=display)
t.start()
for i in range(20):
	print("Main Thread")