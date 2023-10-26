n=int(input("Enter the number : "))
a=0
b=0
c=1
i=0
print(f"Fibonacci series : ")
while i<=n :
	print(b,end=" ")
	a=b
	b=c
	c=a+b
	i=i+1
