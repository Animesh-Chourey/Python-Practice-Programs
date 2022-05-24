a={'10','20','56','78'}
b={'40','20','56','78','10'}
print("a: ",a)
print("b: ",b)
#Union method
print("b.union(a): ",b.union(a)) #or
print("a|b: ",a|b)

#intersection method
print("b.intersection(a): ",b.intersection(a)) #or
print("a&b: ",a&b)

#difference method
print("b.difference(a): ",b.difference(a)) #or
print("b-a: ",b-a)

#symmetric_difference method
print("a.symmetric_difference(b): ",a.symmetric_difference(b)) #or
print("a^b: ",a^b)

#issubset method
print("a.issubset(b): ",a.issubset(b))

#update method
a.update('30')
print("a after update: ",a)