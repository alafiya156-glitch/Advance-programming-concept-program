
# 14. Write a Python program to create a module containing functions
# for addition, subtraction, multiplication, and division. Import only
# the required functions from the module and use them.




# main.py

from calculator import add, multiply

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

print("Addition:", add(a, b))
print("Multiplication:", multiply(a, b))
