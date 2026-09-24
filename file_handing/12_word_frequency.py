
# 12. Read a text file and count how many times each word occurs.
# Display the result using a dictionary.

file = open("student.txt", "r")

words = file.read().lower().split()

frequency = {}

for word in words:
    if word in frequency:
        frequency[word] += 1
    else:
        frequency[word] = 1

print("Word Frequency:")
print(frequency)

file.close()
