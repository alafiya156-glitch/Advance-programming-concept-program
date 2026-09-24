
# 5. Write a program to count and display the total number of lines
# present in a text file.

file = open("student.txt", "r")

lines = file.readlines()

print("Total Number of Lines:", len(lines))

file.close()
