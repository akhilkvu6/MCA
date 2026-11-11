my_dict = {"Banana": 20, "Apple": 10, "Orange": 30, "Grapes": 15}

print("Original Dictionary:", my_dict)

# Sort Ascending
asc = dict(sorted(my_dict.items()))
print("Ascending Order:", asc)

# Sort Descending (reverse=True)
desc = dict(sorted(my_dict.items(), reverse=True))
print("Descending Order:", desc)