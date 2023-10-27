l1= ['Blue', 'Green', 'Red', 'Yellow', 'Purple', 'Orange']
l2= ['Red', 'Green', 'Blue']
print(f"List one : {l1}")
print(f"List two : {l2}")
l3=set(l1).difference(set(l2))
print(f"New list : {l3}")

