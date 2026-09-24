
# 13. Accept a word from the user and search for it in a text file.
# Display the number of occurrences and the line numbers where it appears.

search_word = input("Enter word to search: ")

file = open("student.txt", "r")

count = 0
line_numbers = []

for line_number, line in enumerate(file, 1):
    words = line.lower().split()

    if search_word.lower() in words:
        count += words.count(search_word.lower())
        line_numbers.append(line_number)

file.close()

print("Number of Occurrences:", count)
print("Line Numbers:", line_numbers)
