str1 = input("Enter First String: ")
str2 = input("Enter Second String: ")

# Create new strings by swapping the first character (index 0)
new_a = str2[0] + str1[1:]
new_b = str1[0] + str2[1:]

# Join them with a space
result = new_a + " " + new_b

print("Result:", result)