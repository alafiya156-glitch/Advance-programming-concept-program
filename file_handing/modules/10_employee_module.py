
# 10. Write a Python program to create a module containing functions
# to calculate the gross salary and net salary of an employee.
# Import the module and use the functions.




# main.py

import salary_module

basic = float(input("Enter basic salary: "))
allowance = float(input("Enter allowance: "))
deduction = float(input("Enter deduction: "))

gross = salary_module.gross_salary(basic, allowance)
net = salary_module.net_salary(gross, deduction)

print("Gross Salary:", gross)
print("Net Salary:", net)
