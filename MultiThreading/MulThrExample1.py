import threading
t=threading.current_thread()
print(t)
#print(threading.current_thread().getName()) #or
print(t.getName())

t.setName("MyThread")
print("thread t name after renaming: ",t.getName())