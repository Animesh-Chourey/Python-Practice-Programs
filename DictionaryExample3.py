d={1:{'A':500,'B':800},6:"ABC"}
print("Value at key 1: ",d[1])
print("Value at key 6: ",d[6])
print("Value at key A: ",d[1]['A'])
print("Value at key B: ",d[1]['B'])

#get method
print("Value at key 1: ",d.get(1))