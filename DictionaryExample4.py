#update values in dictionary
d1={1:{'A':500,'B':800},6:"ABC"}
d1[6]="XYZ"
print("updated value d1: ",d1)
d1[1]['A']=300
print("again updated value d1: ",d1)

#update dict i.e insert more items into dictionary
d1[4]=[2,4]
print("Updated dict d1: ",d1)

#update method
d1.update(a=34,b=78)
print("updated dict with method: ",d1) #or

d1.update({90+7j:True})
print("updated dict with method: ",d1)