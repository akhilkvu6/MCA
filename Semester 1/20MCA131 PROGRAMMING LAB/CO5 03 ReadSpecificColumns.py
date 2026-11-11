#pip install pandas
import pandas as pd

# Specify which column(s) to read
columns = ["Name"]

# Read only those columns from the CSV file
file = pd.read_csv("CO5_02_students.csv", usecols=columns)

# Print the selected column(s)
print(file)
