limit = int(input("Enter the number of terms: "))

a = 0
b = 1

print("Fibonacci Series:")

for i in range(limit):
    print(a)
    c = a + b
    a = b
    b = c