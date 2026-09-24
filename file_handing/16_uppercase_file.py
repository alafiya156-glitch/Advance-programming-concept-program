
# 16. Write a Python program to read a text file and convert all
# its contents into uppercase. Save the result in a new file.

file = open("student.txt", "r")

data = file.read()

file.close()

data = data.upper()

new_file = open("uppercase_student.txt", "w")

new_file.write(data)

new_file.close()

print("File converted to uppercase successfully.")
print("New file saved as uppercase_student.txt")
