from package import sum
from package import avg
from package import power
n1=int(input("Enter the first number : "))
n2=int(input("Enter the secound number : "))

print("Sum : ",sum.sum(n1,n2))
print("Average : ",avg.avg(n1,n2))
print(f"Power of {n1}: {power.power(n1)}")
print(f"Power of {n2}: {power.power(n2)}")
