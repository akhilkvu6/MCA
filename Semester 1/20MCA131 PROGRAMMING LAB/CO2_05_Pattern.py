n = int(input("Enter number of rows: "))

print("Pattern:")

for i in range(1, n + 1):
    for j in range(1, i + 1):
        # Calculates steps: 1*1, then 2*1, 2*2, etc.
        print(i * j, end=" ")
    
    # Move to next line
    print()