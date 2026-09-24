
# 5. Write a Python program to create a module containing functions
# to check whether a number is even, odd, or prime. Import the module
# and use the functions.


# main.py

import number_module

num = int(input("Enter a number: "))

if number_module.is_even(num):
    print("Number is Even.")
else:
    print("Number is Odd.")

if number_module.is_prime(num):
    print("Number is Prime.")
else:
    print("Number is not Prime.")
