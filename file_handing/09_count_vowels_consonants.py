
# 9. Read a text file and count the number of vowels and consonants
# present in the file.

file = open("student.txt", "r")

data = file.read().lower()

vowels = 0
consonants = 0

for ch in data:
    if ch.isalpha():
        if ch in "aeiou":
            vowels += 1
        else:
            consonants += 1

print("Total Vowels:", vowels)
print("Total Consonants:", consonants)

file.close()

