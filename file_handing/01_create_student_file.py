
# 1. Write a Python program to create a file named student.txt and
# write the student's name, roll number, branch, and semester into the file.

file = open("student.txt", "w")

file.write("Name: Amit\n")
file.write("Roll Number: 101\n")
file.write("Branch: Computer Engineering\n")
file.write("Semester: 5\n")

file.close()

print("Student information written successfully.")
