#Print positive list of integers from list of integers
l1=[1,-4,5,9,32,-7,-12,0,25,-74]
l2=[]
for i in l1:
    if i>0:
        l2.append(i)
print("Positive numbers are : ",l2)
