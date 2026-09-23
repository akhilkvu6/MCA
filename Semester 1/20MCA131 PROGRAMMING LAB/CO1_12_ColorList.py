# Accept comma-separated input (e.g., "red,green,blue")
input_string = input("Enter colors separated by comma: ")

# Split the string into a list
colors = input_string.split(",")

print("First Color:", colors[0])
print("Last Color:",  colors[-1])