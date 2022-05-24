d1=dict({1:34,4:67,"Hello":90})
print("d1: ",d1)

d2=dict([(1,23),(2,45),(78,100)])
print("d2= ",d2)

d3=dict([(1,23),(2,45),(78,100),(1,45),(3,400)]) #Since keys is same value will be overridden & no error will be shown
print("d3= ",d3)

for i in d1:
	print("i= ",i) #while looping through dict keys will be returned by default and not values