l=[2,7,1,9,23,76,15,21,37,62]
print("Original list : ",l)
for i in l :
	if(i%2==0):
		l.remove(i)
print("List after removing even number : ",l)
