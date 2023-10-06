#Program to swap first and last element in the list
n=int(input("Enter the number of elements in the string :"))
print("Enter the elements")
l=[]
for i in range(0,n):
    e=input()
    l.append(e)
print("Current list :")
for i in l:
        print(i,end=" ")
temp=l[0]
l[0]=l[n-1]
l[n-1]=temp
print("\nList after swapping of first and last element :")
for i in l:
        print(i,end=" ")
