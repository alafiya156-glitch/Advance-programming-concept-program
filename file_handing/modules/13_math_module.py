
# 13. Write a Python program to create a module containing functions
# to calculate the power, square root, and absolute value of a number.
# Import the module and use the functions.




# main.py

import math_operation

num = float(input("Enter a number: "))
power_value = int(input("Enter power: "))

print("Power:", math_operation.power(num, power_value))
print("Square Root:", math_operation.square_root(num))
print("Absolute Value:", math_operation.absolute(num))
