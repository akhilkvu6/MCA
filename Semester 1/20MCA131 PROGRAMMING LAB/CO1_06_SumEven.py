# Assuming we want the sum of even numbers within the range 1 to 100
total_sum = 0

for i in range(1, 101):
    if i % 2 == 0:
        total_sum = total_sum + i

print("Sum of even numbers up to 100 is:", total_sum)