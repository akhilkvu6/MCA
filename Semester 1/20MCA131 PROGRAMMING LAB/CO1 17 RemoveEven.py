# List of numbers
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print("Original List:", numbers)

# List Comprehension: Keep 'x' only if 'x % 2' is NOT 0
odd_numbers = [x for x in numbers if x % 2 != 0]

print("List after removing even numbers:", odd_numbers)