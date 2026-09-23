import math

num1 = int(input("Enter Number 1: "))
num2 = int(input("Enter Number 2: "))

# Use Python's built-in math library
gcd = math.gcd(num1, num2)

print("GCD of", num1, "and", num2, "is:", gcd)