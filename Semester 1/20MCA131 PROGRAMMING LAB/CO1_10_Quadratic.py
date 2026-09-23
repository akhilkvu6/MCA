import math

a = float(input("Enter a: "))
b = float(input("Enter b: "))
c = float(input("Enter c: "))

# Discriminant formula: b^2 - 4ac
d = (b * b) - (4 * a * c)

if d > 0:
    root1 = (-b + math.sqrt(d)) / (2 * a)
    root2 = (-b - math.sqrt(d)) / (2 * a)
    print("Roots are real and different:", root1, root2)

elif d == 0:
    root1 = -b / (2 * a)
    print("Roots are real and same:", root1)

else:
    print("Roots are complex (imaginary)")