l1=[23,45,67]
l2=['A','B','C']
z=zip(l1,l2)

print("z: ",z)

d=list(z)
print("d= ",d)

'''d=list(z)
print("d as list: ",d)
'''
l,m=zip(*d)
print("l= ",l)
print("m= ",m)