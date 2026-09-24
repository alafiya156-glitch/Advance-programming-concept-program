
# 4. Write a Python program to create a module containing functions
# to count vowels and consonants in a string. Import the module
# and use the functions.


# main.py

import string_module

text = input("Enter a string: ")

print("Vowels:", string_module.count_vowels(text))
print("Consonants:", string_module.count_consonants(text))
