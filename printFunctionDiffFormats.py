#for integer values
x=10
y=20
print("Integer Values:")
print("Value of x and y = ",x,y)
print("Value of x=%d and y=%d"%(x,y))
print("Value of x={} and y={}".format(x,y)) #This type is used when format specifier of a data type is not known

#for float values
x=10.23
y=34.23
print("Float Values:")
print("Values of x and y= ",x,y)
print("Values of x=%f and y=%f"%(x,y))
print("Values of x={} and y={}".format(x,y))

#for complex values
x=10+7j
print("Complex Values:")
print("Value of x=",x)
print("Value of x=%d+%dj"%(x.real,x.imag))
print("Value of x={}+{}j".format(x.real,x.imag))