#if we want to import all packages at a same time
from MyPackage import *
m1.fibo(200)
m2.sum(30,6)
m2.sub(30,6)
m2.mul(30,6)
m2.div(30,6)

#To import a subpackage
from MyPackage.SubPack import m3
m3.pow(5,3)