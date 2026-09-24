
# 19. Write a Python program to store student attendance records in a file
# and calculate the attendance percentage.

file = open("attendance.txt", "w")

file.write("Amit,80,100\n")
file.write("Rahul,75,100\n")
file.write("Priya,90,100\n")

file.close()

file = open("attendance.txt", "r")

print("Student Attendance:")

for line in file:
    data = line.strip().split(",")

    name = data[0]
    present = int(data[1])
    total = int(data[2])

    percentage = (present / total) * 100

    print("Name:", name)
    print("Attendance:", percentage, "%")
    print()

file.close()
