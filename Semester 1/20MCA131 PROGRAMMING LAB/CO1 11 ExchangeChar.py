text = input("Enter a string: ")

# Get first and last characters
start = text[0]
end   = text[-1]

# Get the middle part (everything between first and last)
middle = text[1:-1]

# Combine them in reverse order
new_text = end + middle + start

print("New String:", new_text)