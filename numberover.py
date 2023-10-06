#Prompt the user for a list of integers for all values greater than 100
n=int(input("Enter the number of elements in the list :"))
list=[]
i=0
while i<n:
    element=int(input("Enter the element : "))
    if element>100:
        list.append("'over'")
    else:
        list.append(element)
    i=i+1
    for l in list:
        print(l,end="  ")
    print("\n")
