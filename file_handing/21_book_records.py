
# 21. Write a Python program to create a file to store book records
# containing book title, author, and price. Read and display the records.

file = open("books.txt", "w")

file.write("Python Programming,John Smith,450\n")
file.write("Data Structures,Robert Brown,550\n")
file.write("Computer Networks,James Lee,600\n")

file.close()

file = open("books.txt", "r")

print("Book Records:")

for line in file:
    data = line.strip().split(",")

    print("Book Title:", data[0])
    print("Author:", data[1])
    print("Price:", data[2])
    print()

file.close()
