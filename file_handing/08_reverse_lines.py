
# 8. Write a program to read a text file and display its lines in
# reverse order.

file = open("student.txt", "r")

lines = file.readlines()

for line in reversed(lines):
    print(line.strip())

file.close()

