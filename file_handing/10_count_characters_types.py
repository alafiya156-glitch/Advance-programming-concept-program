
# 10. Read a text file and calculate the number of alphabets, digits,
# spaces, and special characters.

file = open("student.txt", "r")

data = file.read()

alphabets = 0
digits = 0
spaces = 0
special_characters = 0

for ch in data:
    if ch.isalpha():
        alphabets += 1
    elif ch.isdigit():
        digits += 1
    elif ch.isspace():
        spaces += 1
    else:
        special_characters += 1

print("Alphabets:", alphabets)
print("Digits:", digits)
print("Spaces:", spaces)
print("Special Characters:", special_characters)

file.close()