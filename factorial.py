n=int(input("Enter the number : "))
def fact(n):
    if n==1:
        return 1
    else:
        f=n*fact(n-1)
        return f
f=fact(n)
print(f"Factorial of {n} is : {f}")
