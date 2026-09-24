
# 22. Write a Python program to merge the contents of two text files
# into a third file.

file1 = open("file1.txt", "r")
data1 = file1.read()
file1.close()

file2 = open("file2.txt", "r")
data2 = file2.read()
file2.close()

file3 = open("merged.txt", "w")

file3.write(data1)
file3.write("\n")
file3.write(data2)

file3.close()

print("Files merged successfully.")
print("Merged file saved as merged.txt")
