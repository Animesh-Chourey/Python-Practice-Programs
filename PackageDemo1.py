#single import of each package
'''from MyPackage import m1
m1.fibo(200)

from MyPackage import m2
m2.sum(30,6)
m2.sub(30,6)
m2.mul(30,6)
m2.div(30,6)'''

#Multiple import of packages
from MyPackage import m1,m2
m1.fibo(200)
m2.sum(30,6)
m2.sub(30,6)
m2.mul(30,6)
m2.div(30,6)