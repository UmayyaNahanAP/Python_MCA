#Factorial of a number 
n=int(input("Enter the number :"))
if n<0 :
    print("Enter a possitive number")
elif n==0:
     print("Factorial of zero is 1")
else:
    f=1
    for i in range(1,n+1) :
        f=f*i
    print("Factorial ",f)
