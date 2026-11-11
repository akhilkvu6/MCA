a = int(input("Enter First Number: "))
b = int(input("Enter Second Number: "))

print("Before Swapping: a =", a, "b =", b)

# Python allows swapping in a single line
a, b = b, a

print("After Swapping: a =", a, "b =", b)