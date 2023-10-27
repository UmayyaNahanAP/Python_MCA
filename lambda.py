print("Square")
a=int(input("Enter side: "))
area=lambda a:a*a
print(f"Area : {area(a)}")
print("\nRectangle")
l = int(input("Enter length  : "))
b = int(input("Enter breadth : "))
area = lambda l,b:l*b
print(f"Area : {area(l,b)}")
print("\nTriangle")
b1 = int(input("Enter base : "))
h = int(input("Enter height : "))
area = lambda b1,h:b1*h/2
print(f"Area : {area(b1,h)}")
