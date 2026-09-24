
# 18. Write a Python program to create a file to store employee records
# containing employee name, ID, and salary. Read and display the records.

file = open("employees.txt", "w")

file.write("Amit,101,35000\n")
file.write("Rahul,102,42000\n")
file.write("Priya,103,38000\n")

file.close()

file = open("employees.txt", "r")

print("Employee Records:")

for line in file:
    data = line.strip().split(",")

    print("Name:", data[0])
    print("Employee ID:", data[1])
    print("Salary:", data[2])
    print()

file.close()
