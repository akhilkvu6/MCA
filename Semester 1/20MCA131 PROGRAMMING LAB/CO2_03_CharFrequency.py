text = input("Enter a string: ")
freq = {}

for char in text:
    if char in freq:
        freq[char] = freq[char] + 1
    else:
        freq[char] = 1

print("Character Frequency:", freq)