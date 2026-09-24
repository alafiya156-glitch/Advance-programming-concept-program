
# 8. Write a Python program to create a module containing functions
# to convert temperature from Celsius to Fahrenheit and Fahrenheit
# to Celsius. Import the module and use the functions.




# main.py

import temperature_module

celsius = float(input("Enter temperature in Celsius: "))
fahrenheit = float(input("Enter temperature in Fahrenheit: "))

print("Fahrenheit:", temperature_module.celsius_to_fahrenheit(celsius))
print("Celsius:", temperature_module.fahrenheit_to_celsius(fahrenheit))
