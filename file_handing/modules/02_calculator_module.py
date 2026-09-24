#2. Write a Python program to create a module containing a function
# to calculate the square and cube of a number. Import the module
# and use the functions.



# main.py

import calculator_module

num = int(input("Enter a number: "))

print("Square:", calculator_module.square(num))
print("Cube:", calculator_module.cube(num))