
# 3. Write a Python program to create a module containing functions
# to calculate the area of a circle and rectangle. Import the module
# and use the functions.




# main.py

import area_module

radius = float(input("Enter radius of circle: "))
length = float(input("Enter length of rectangle: "))
width = float(input("Enter width of rectangle: "))

print("Area of Circle:", area_module.circle_area(radius))
print("Area of Rectangle:", area_module.rectangle_area(length, width))
