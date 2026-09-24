# 11. Write a Python program to create a module containing a function
# to calculate the discount and final price of a product.
# Import the module and use the function.




# main.py

import discount_module

price = float(input("Enter product price: "))
discount = float(input("Enter discount percentage: "))

discount_amount = discount_module.calculate_discount(price, discount)
total = discount_module.final_price(price, discount)

print("Discount Amount:", discount_amount)
print("Final Price:", total)
