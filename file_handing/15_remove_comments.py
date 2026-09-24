
# 15. Write a Python program to remove all comments from a Python file
# and save the modified content into a new file.

file = open("program.py", "r")

lines = file.readlines()

file.close()

new_file = open("program_without_comments.py", "w")

for line in lines:
    if not line.strip().startswith("#"):
        new_file.write(line)

new_file.close()

print("Comments removed successfully.")
print("Modified file saved as program_without_comments.py")
