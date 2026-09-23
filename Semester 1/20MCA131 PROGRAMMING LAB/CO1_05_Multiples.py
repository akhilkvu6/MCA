num = int(input("Enter the number: "))
limit = int(input("Enter the limit: "))

print("Multiples of", num, ":")

for i in range(1, limit + 1):
    print(num * i)