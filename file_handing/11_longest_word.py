
# 11. Read a text file and find the longest word present in the file.

file = open("student.txt", "r")

words = file.read().split()

longest_word = max(words, key=len)

print("Longest Word:", longest_word)

file.close()

