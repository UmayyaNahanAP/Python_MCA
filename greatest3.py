a=int(input("Enter the first number :"))
b=int(input("Enter the secound number :"))
c=int(input("Enter the third number :"))
if a>b:
    if a>c:
        print(a,"is big")
    else:
        print(c,"is big")
elif b>a:
    if b>c:
        print(b,"is big")
    else:
        print(c,"is big")
