
# 6. Write a Python program to create a module containing functions
# to find the largest and smallest element in a list. Import the module
# and use the functions.




# main.py

import list_module

numbers = [10, 25, 5, 40, 15]

print("List:", numbers)
print("Largest Element:", list_module.largest(numbers))
print("Smallest Element:", list_module.smallest(numbers))