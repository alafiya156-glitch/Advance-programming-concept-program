
# 7. Write a program to count the total number of characters in a
# text file, including spaces.

file = open("student.txt", "r")

data = file.read()

print("Total Number of Characters:", len(data))

file.close()

