
# 4. Write a program to read a text file line by line and display
# each line separately.

file = open("student.txt", "r")

for line in file:
    print(line.strip())

file.close()
