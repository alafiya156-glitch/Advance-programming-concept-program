# 17. Write a Python program to create a file to store student records
# containing name, roll number, and marks. Read and display the records.

file = open("students.txt", "w")

file.write("Amit,101,85\n")
file.write("Rahul,102,78\n")
file.write("Priya,103,92\n")

file.close()

file = open("students.txt", "r")

print("Student Records:")

for line in file:
    data = line.strip().split(",")

    print("Name:", data[0])
    print("Roll Number:", data[1])
    print("Marks:", data[2])
    print()

file.close()
