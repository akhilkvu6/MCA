import csv

# A list of dictionaries
mydict = [
    {"first": "Harry", "last": "Potter"},
    {"first": "Ron", "last": "Weasely"}, 
    {"first": "Hermione", "last": "Granger"}
]

# Write the csv file
with open("CO5_04.csv", "w", newline="") as file:
    writer = csv.DictWriter(file, fieldnames=["first", "last"])
    writer.writeheader()
    writer.writerows(mydict)

# Read the file
with open("CO5_04.csv", "r") as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        print(row)
