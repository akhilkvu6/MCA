file1 = open("textfile1.txt", "r")      # reading file
file2 = open("textfile2.txt", "w")       # writing file

count = 0
for line in file1:
    count += 1
    if count % 2 != 0:                 # odd line
        file2.write(line)

file1.close()
file2.close()
