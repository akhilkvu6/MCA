text = input("Enter a string: ")

if text.endswith("ing"):
    result = text + "ly"
else:
    result = text + "ing"

print("Modified String:", result)