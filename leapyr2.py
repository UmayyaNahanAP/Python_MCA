#Display future leap years from current year to a final year entered by the user
cy=int(input("Enter the current year : "))
fy=int(input("Enter the final year : "))
print("Leap year from",cy,"to",fy,"are : ")
for y in range(cy,fy+1):
    if(y%4==0 and y%100!=0 or y%400==0):
         print(y,end=" ")
