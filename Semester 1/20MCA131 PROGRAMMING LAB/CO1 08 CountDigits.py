num = int(input("Enter a number: "))
count = 0

while num > 0:
    num = num // 10  # Remove the last digit
    count = count + 1

print("Total number of digits:", count)