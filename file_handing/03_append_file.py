
# 3. Write a program to append additional student information to an
# existing file without deleting its previous contents.

file = open("student.txt", "a")

file.write("College: ABC College\n")
file.write("City: Pune\n")

file.close()

print("Additional information appended successfully.")
