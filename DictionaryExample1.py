d1={}
print("d1: ",d1)

d2=dict()
print("d2: ",d2)

#d3={1:"Hello",2:"Python",[1,2]:32} Since list is mutable we cannot set it as key in dictionary
#print("d3: ",d3)

#d3={1:"Hello",2:"Python",{1,2}:32} Since set is mutable we cannot set it as key in dictionary
#print("d3: ",d3)

d3={1:"Hello",2:"Python",(1,2):32} #Since tuple is immutable we can set it as key in dictionary
print("d3: ",d3)