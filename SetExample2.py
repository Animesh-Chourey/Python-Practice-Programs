s={10,20,30,True,"Hello",78+5j}
print("s: ",s)
#print("s[3]: ",s[3]) #error : because indexing is not supported in set

#list can't be stored in set
#s1={10,20,30,["ab",40.43]} #we can't store list type in set because list are mutable(i.e unhashable)in set data stored should be hashable(i.e immutable)

#tuples can be stored in set
s1={10,20,30,(100,200,300)}
print("s1: ",s1)