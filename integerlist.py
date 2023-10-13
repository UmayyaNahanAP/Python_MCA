#Program to checkl wheather the list are of same length,sum of list are same and any value occur in both
l1=[]
l2=[]
n1=int(input("Enter the number of elements in list one :"))
n2=int(input("Enter the number of elements in list two :"))
print("Enter the elements of list one : ")
for i in range(0,n1):
    e1=int(input())
    l1.append(e1)
print("Enter the elements of list two : ")
for i in range(0,n2):
    e2=int(input())
    l2.append(e2)
print("List one :")
for i in l1:
        print(i,end=" ")
print("\nList two :")
for i in l2:
        print(i,end=" ")
if len(l1)==len(l2):
    print("\nBoth list have same length ",l1)
else:
     print("\nLength of list are different :\nlength of list one = ",len(l1),"and length of list two = ",len(l2))
if sum(l1)==sum(l2):
    print("\nBoth lists have same sum",sum(l1))
else:
    print("\nSum of list are different :\nSum of list one = ",sum(l1),"\nSum of list two = ",sum(l2))
for i in l1:
    for j in l2:
        if i==j:
           print("\n",i,"is in both at list1 in position",l1.index(i),"and list2 in position",l2.index(j))
    
