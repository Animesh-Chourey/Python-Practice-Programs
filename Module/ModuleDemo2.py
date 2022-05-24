#if we want to import multiple modules
'''import m1,m2
m1.fibo(100)
m2.sum(30,6)
m2.sub(30,6)
m2.mul(30,6)
m2.div(30,6)'''

#if we want to import a particular attribute from a module
from m2 import sub,div
sub(220,100) #here calling of function can be done directly without the help module
div(220,10)