
# 6. Write a program to count the total number of words present
# in a text file.

file = open("student.txt", "r")

data = file.read()

words = data.split()

print("Total Number of Words:", len(words))

file.close()

