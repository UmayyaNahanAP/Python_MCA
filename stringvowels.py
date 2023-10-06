s=input("Enter the string : ")
i=0
l1=[]
flag=0
for i in s:
    if i in "aeiouAEIOU":
        l1.append(i)
        flag=1
if flag==1:
    print("Vowels in the string are : ")
    for i in l1:
        print(i,end=" ")
else:
    print("No vowels in the string")
