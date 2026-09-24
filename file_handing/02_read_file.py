
# 2. Write a program to open a text file and display its complete contents.

file = open("student.txt", "r")

data = file.read()

print("File Contents:")
print(data)

file.close()

