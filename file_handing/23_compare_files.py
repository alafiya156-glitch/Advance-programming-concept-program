
# 23. Write a Python program to compare the contents of two text files
# and check whether they are identical or different.

file1 = open("file1.txt", "r")
data1 = file1.read()
file1.close()

file2 = open("file2.txt", "r")
data2 = file2.read()
file2.close()

if data1 == data2:
    print("Both files are identical.")
else:
    print("Both files are different.")

