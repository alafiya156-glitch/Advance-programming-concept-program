
# 14. Read a text file and replace all occurrences of a specified word
# with another word. Save the modified text in the same file or a new file.

old_word = input("Enter word to replace: ")
new_word = input("Enter new word: ")

file = open("student.txt", "r")

data = file.read()

file.close()

data = data.replace(old_word, new_word)

file = open("student_new.txt", "w")

file.write(data)

file.close()

print("Word replaced successfully.")
print("Modified file saved as student_new.txt")
