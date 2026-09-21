#1. Write a function factorial(n) that accepts an integer and returns its factorial.

def factorial(n):
    fact = 1
    for i in range(1, n + 1):
        fact = fact * i
    return fact

n = int(input("Enter number: "))
print("Factorial:", factorial(n))


#2. Write a function check_even_odd(n) that determines whether a given number is even or odd.

def check_even_odd(n):
    if n % 2 == 0:
        return "Even"
    else:
        return "Odd"

n = int(input("Enter number: "))
print(check_even_odd(n))


#3. Define a function that accepts two numbers and returns the greater number.

def greater(a, b):
    if a > b:
        return a
    else:
        return b

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

print("Greater number:", greater(a, b))


#4. Create a function simple_interest(p, r, t) to calculate simple interest.

def simple_interest(p, r, t):
    return (p * r * t) / 100

p = float(input("Enter principal: "))
r = float(input("Enter rate: "))
t = float(input("Enter time: "))

print("Simple Interest:", simple_interest(p, r, t))


#5. Write a function is_prime(n) that returns True if a number is prime; otherwise, returns False.

def is_prime(n):
    if n < 2:
        return False

    for i in range(2, n):
        if n % i == 0:
            return False

    return True

n = int(input("Enter number: "))
print(is_prime(n))


#6. Define a function to calculate the area of a circle using its radius.

def area_circle(r):
    return 3.14 * r * r

r = float(input("Enter radius: "))

print("Area of circle:", area_circle(r))


#7. Write a function that accepts n and returns the sum of the first n natural numbers.

def natural_sum(n):
    total = 0

    for i in range(1, n + 1):
        total = total + i

    return total

n = int(input("Enter n: "))

print("Sum:", natural_sum(n))


#8. Create a function power(base, exponent) to calculate the value of base raised to exponent.

def power(base, exponent):
    return base ** exponent

base = int(input("Enter base: "))
exponent = int(input("Enter exponent: "))

print("Result:", power(base, exponent))


#9. Write a function that accepts a list of numbers and returns the largest element without using the built-in max() function.

def largest(numbers):
    large = numbers[0]

    for num in numbers:
        if num > large:
            large = num

    return large

numbers = [10, 25, 5, 40, 30]

print("Largest:", largest(numbers))


#10. Define a function that accepts a string and returns the number of vowels present in it.

def count_vowels(text):
    count = 0

    for ch in text:
        if ch.lower() in "aeiou":
            count = count + 1

    return count

text = input("Enter string: ")

print("Number of vowels:", count_vowels(text))


#11. Write a function that accepts a string and returns its reverse.

def reverse_string(text):
    return text[::-1]

text = input("Enter string: ")

print("Reverse:", reverse_string(text))


#12. Create a function that checks whether a given string or number is a palindrome.

def palindrome(value):
    value = str(value)

    if value == value[::-1]:
        return True
    else:
        return False

value = input("Enter string or number: ")

print(palindrome(value))


#13. Write a function that accepts a list of numbers and returns their average.

def average(numbers):
    return sum(numbers) / len(numbers)

numbers = [10, 20, 30, 40, 50]

print("Average:", average(numbers))


#14. Define a function that accepts a list and an element and returns the number of times that element occurs.

def count_element(numbers, element):
    count = 0

    for num in numbers:
        if num == element:
            count = count + 1

    return count

numbers = [10, 20, 10, 30, 10, 40]
element = int(input("Enter element: "))

print("Count:", count_element(numbers, element))


#15. Write a function that accepts a list and returns a new list containing only unique elements.

def unique_elements(numbers):
    result = []

    for num in numbers:
        if num not in result:
            result.append(num)

    return result

numbers = [10, 20, 10, 30, 20, 40]

print("Unique elements:", unique_elements(numbers))


#16. Create a function to find the second-largest number in a list.

def second_largest(numbers):
    numbers = list(set(numbers))
    numbers.sort()

    return numbers[-2]

numbers = [10, 50, 30, 80, 60, 80]

print("Second largest:", second_largest(numbers))


#17. Write a function that accepts n and returns the first n Fibonacci numbers.

def fibonacci(n):
    result = []
    a = 0
    b = 1

    for i in range(n):
        result.append(a)
        a, b = b, a + b

    return result

n = int(input("Enter n: "))

print("Fibonacci series:", fibonacci(n))


#18. Create a function that accepts marks in five subjects and returns the student's percentage and grade.

def student_result(marks):
    total = sum(marks)
    percentage = total / 5

    if percentage >= 90:
        grade = "A"
    elif percentage >= 75:
        grade = "B"
    elif percentage >= 60:
        grade = "C"
    elif percentage >= 50:
        grade = "D"
    else:
        grade = "F"

    return percentage, grade

marks = []

for i in range(5):
    marks.append(float(input("Enter marks: ")))

percentage, grade = student_result(marks)

print("Percentage:", percentage)
print("Grade:", grade)


#19. Write a function that accepts the number of units consumed and calculates the electricity bill according to predefined slabs.

def electricity_bill(units):
    if units <= 100:
        bill = units * 5
    elif units <= 200:
        bill = 100 * 5 + (units - 100) * 7
    else:
        bill = 100 * 5 + 100 * 7 + (units - 200) * 10

    return bill

units = int(input("Enter units consumed: "))

print("Electricity bill:", electricity_bill(units))


#20. Write a function that accepts basic salary and calculates gross salary after adding HRA and DA.

def gross_salary(basic):
    hra = basic * 0.20
    da = basic * 0.10

    return basic + hra + da

basic = float(input("Enter basic salary: "))

print("Gross salary:", gross_salary(basic))


#Functions and Recursion
#21. Create a function that accepts item prices and quantities and returns the total bill after applying a discount.

def total_bill(prices, quantities):
    total = 0

    for i in range(len(prices)):
        total = total + prices[i] * quantities[i]

    discount = total * 0.10
    return total - discount

prices = [100, 200, 300]
quantities = [2, 1, 3]

print("Total bill after discount:", total_bill(prices, quantities))


#22. Write a function that accepts a list of numbers and returns the minimum, maximum, sum, and average.

def calculate(numbers):
    minimum = min(numbers)
    maximum = max(numbers)
    total = sum(numbers)
    average = total / len(numbers)

    return minimum, maximum, total, average

numbers = [10, 20, 30, 40, 50]

minimum, maximum, total, average = calculate(numbers)

print("Minimum:", minimum)
print("Maximum:", maximum)
print("Sum:", total)
print("Average:", average)


#23. Write a program using separate functions to process student records containing name, roll number, and marks in five subjects. Calculate total, percentage, grade, class average, highest scorer, and lowest scorer.

def total_marks(marks):
    return sum(marks)

def percentage(marks):
    return sum(marks) / 5

def grade(percent):
    if percent >= 90:
        return "A"
    elif percent >= 75:
        return "B"
    elif percent >= 60:
        return "C"
    elif percent >= 50:
        return "D"
    else:
        return "F"

students = [
    ("Aisha", 1, [85, 90, 80, 88, 92]),
    ("Rahul", 2, [70, 75, 80, 72, 78]),
    ("Sneha", 3, [90, 95, 92, 88, 94])
]

percentages = []

for student in students:
    name = student[0]
    roll = student[1]
    marks = student[2]

    total = total_marks(marks)
    percent = percentage(marks)
    percentages.append(percent)

    print("Name:", name)
    print("Roll Number:", roll)
    print("Total:", total)
    print("Percentage:", percent)
    print("Grade:", grade(percent))
    print()

class_average = sum(percentages) / len(percentages)

highest = max(students, key=lambda x: percentage(x[2]))
lowest = min(students, key=lambda x: percentage(x[2]))

print("Class average:", class_average)
print("Highest scorer:", highest[0])
print("Lowest scorer:", lowest[0])


#24. Create functions for deposit, withdrawal, balance enquiry, and transaction history. Prevent withdrawal when the balance is insufficient and maintain a transaction record.

balance = 0
transactions = []

def deposit(amount):
    global balance
    balance = balance + amount
    transactions.append("Deposited " + str(amount))

def withdrawal(amount):
    global balance

    if amount <= balance:
        balance = balance - amount
        transactions.append("Withdrawn " + str(amount))
    else:
        print("Insufficient balance.")

def balance_enquiry():
    print("Balance:", balance)

def transaction_history():
    for transaction in transactions:
        print(transaction)

deposit(5000)
withdrawal(1500)
balance_enquiry()
transaction_history()


#25. Create functions to add books, issue books, return books, search books, and display available books. Maintain book availability using dictionaries.

books = {
    "Python": True,
    "Java": True,
    "C++": True
}

def add_book(name):
    books[name] = True

def issue_book(name):
    if name in books and books[name]:
        books[name] = False
        print("Book issued.")
    else:
        print("Book is not available.")

def return_book(name):
    if name in books:
        books[name] = True
        print("Book returned.")

def search_book(name):
    if name in books:
        print("Book found.")
    else:
        print("Book not found.")

def display_books():
    for name, available in books.items():
        if available:
            print(name)

add_book("HTML")
issue_book("Python")
return_book("Python")
search_book("Java")
display_books()


#26. Develop a modular program using functions to calculate electricity bills using different consumption slabs. Include fixed charges, taxes, and discounts.

def calculate_bill(units):
    if units <= 100:
        bill = units * 5
    elif units <= 200:
        bill = 100 * 5 + (units - 100) * 7
    else:
        bill = 100 * 5 + 100 * 7 + (units - 200) * 10

    fixed_charge = 100
    tax = bill * 0.05
    discount = bill * 0.02

    final_bill = bill + fixed_charge + tax - discount

    return final_bill

units = int(input("Enter units: "))

print("Final electricity bill:", calculate_bill(units))


#27. Create functions to calculate consultation charges, laboratory charges, medicine charges, room charges, and final bill. Apply discounts based on patient category.

def consultation():
    return 500

def laboratory():
    return 1000

def medicine():
    return 1500

def room():
    return 2000

def final_bill(category):
    total = consultation() + laboratory() + medicine() + room()

    if category == "senior":
        discount = total * 0.20
    elif category == "child":
        discount = total * 0.10
    else:
        discount = 0

    return total - discount

category = input("Enter patient category: ")

print("Final bill:", final_bill(category))


#28. Implement functions to add/remove products, calculate subtotal, apply coupon discounts, calculate GST, and generate the final invoice.

cart = []

def add_product(name, price):
    cart.append((name, price))

def remove_product(name):
    for product in cart:
        if product[0] == name:
            cart.remove(product)
            break

def subtotal():
    return sum(product[1] for product in cart)

def coupon_discount(amount):
    return amount * 0.10

def gst(amount):
    return amount * 0.18

def invoice():
    sub = subtotal()
    discount = coupon_discount(sub)
    taxable = sub - discount
    tax = gst(taxable)
    final = taxable + tax

    print("Subtotal:", sub)
    print("Discount:", discount)
    print("GST:", tax)
    print("Final amount:", final)

add_product("Pen", 100)
add_product("Book", 200)
add_product("Bag", 500)

invoice()


#29. Write a recursive function to search for an element in a sorted list using binary search.

def binary_search(numbers, low, high, key):
    if low > high:
        return -1

    mid = (low + high) // 2

    if numbers[mid] == key:
        return mid
    elif key < numbers[mid]:
        return binary_search(numbers, low, mid - 1, key)
    else:
        return binary_search(numbers, mid + 1, high, key)

numbers = [10, 20, 30, 40, 50, 60, 70]

key = int(input("Enter element: "))

result = binary_search(numbers, 0, len(numbers) - 1, key)

if result == -1:
    print("Element not found.")
else:
    print("Element found at index:", result)


#30. Convert a decimal number into binary using recursion without using Python's built-in conversion functions.

def decimal_binary(n):
    if n == 0:
        return ""

    return decimal_binary(n // 2) + str(n % 2)

n = int(input("Enter decimal number: "))

if n == 0:
    print("Binary: 0")
else:
    print("Binary:", decimal_binary(n))


#31. Check whether a string is a palindrome using recursion.

def palindrome(text):
    if len(text) <= 1:
        return True

    if text[0] != text[-1]:
        return False

    return palindrome(text[1:-1])

text = input("Enter string: ")

if palindrome(text):
    print("Palindrome")
else:
    print("Not palindrome")


#32. Create separate functions for addition, subtraction, multiplication, and division. Pass these functions as arguments to another function called calculate().

def addition(a, b):
    return a + b

def subtraction(a, b):
    return a - b

def multiplication(a, b):
    return a * b

def division(a, b):
    return a / b

def calculate(a, b, operation):
    return operation(a, b)

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

print("Addition:", calculate(a, b, addition))
print("Subtraction:", calculate(a, b, subtraction))
print("Multiplication:", calculate(a, b, multiplication))
print("Division:", calculate(a, b, division))
#Lambda fucntion
#33. Write a lambda function to calculate the square of a given number.

square = lambda x: x * x

n = int(input("Enter number: "))

print("Square:", square(n))


#34. Create a lambda function that returns the cube of a number.

cube = lambda x: x * x * x

n = int(input("Enter number: "))

print("Cube:", cube(n))


#35. Write a lambda function that returns True if a number is even and False otherwise.

even = lambda x: x % 2 == 0

n = int(input("Enter number: "))

print(even(n))


#36. Use a lambda function to find the maximum of two numbers.

maximum = lambda a, b: a if a > b else b

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

print("Maximum:", maximum(a, b))


#37. Create a lambda function to calculate simple interest using principal, rate, and time.

simple_interest = lambda p, r, t: (p * r * t) / 100

p = float(input("Enter principal: "))
r = float(input("Enter rate: "))
t = float(input("Enter time: "))

print("Simple Interest:", simple_interest(p, r, t))


#38. Take a list of numbers, use map() and a lambda function to generate a list containing their squares.

numbers = [1, 2, 3, 4, 5]

squares = list(map(lambda x: x * x, numbers))

print("Squares:", squares)


#39. Use map() with lambda to calculate the cube of every element in a list.

numbers = [1, 2, 3, 4, 5]

cubes = list(map(lambda x: x * x * x, numbers))

print("Cubes:", cubes)


#40. Take two lists of numbers, use map() and lambda to create a third list containing the sum of corresponding elements.

list1 = [10, 20, 30, 40]
list2 = [1, 2, 3, 4]

result = list(map(lambda x, y: x + y, list1, list2))

print("Result:", result)


#41. Take a list of integers, use filter() and lambda to extract all even numbers.

numbers = [10, 15, 20, 25, 30, 35, 40]

even = list(filter(lambda x: x % 2 == 0, numbers))

print("Even numbers:", even)


#42. Take a list of integers, use filter() with an appropriate lambda expression to identify prime numbers.

numbers = [2, 3, 4, 5, 6, 7, 8, 9, 11, 13]

prime = list(filter(
    lambda n: n > 1 and all(n % i != 0 for i in range(2, n)),
    numbers
))

print("Prime numbers:", prime)


#43. Use filter() and lambda to extract positive numbers from a list.

numbers = [-10, 20, -5, 30, -15, 40]

positive = list(filter(lambda x: x > 0, numbers))

print("Positive numbers:", positive)


#44. Take a list of numbers, use filter() and lambda to find numbers greater than 50.

numbers = [20, 55, 40, 70, 90, 35, 60]

result = list(filter(lambda x: x > 50, numbers))

print("Numbers greater than 50:", result)


#45. Take a list of words, use filter() and lambda to find words having more than five characters.

words = ["Python", "Java", "Programming", "Code", "Computer", "AI"]

result = list(filter(lambda word: len(word) > 5, words))

print("Words having more than five characters:", result)


#46. Take a list of words; sort them according to their length using lambda.

words = ["Python", "Java", "Programming", "C", "Computer"]

result = sorted(words, key=lambda word: len(word))

print("Sorted words:", result)


#47. Take a list of tuples containing student names and marks, sort the students according to their marks using lambda.

students = [
    ("Aisha", 85),
    ("Rahul", 70),
    ("Sneha", 92),
    ("Aman", 78)
]

result = sorted(students, key=lambda student: student[1])

print("Students sorted by marks:")

for student in result:
    print(student)


#48. Take employee records containing name and salary, sort them according to salary using lambda.

employees = [
    ("Aisha", 45000),
    ("Rahul", 60000),
    ("Sneha", 52000),
    ("Aman", 40000)
]

result = sorted(employees, key=lambda employee: employee[1])

print("Employees sorted by salary:")

for employee in result:
    print(employee)


#49. Take a list containing student names and marks, use functions and lambda expressions to:
#    a) Calculate average marks.
#    b) Filter students scoring above 75.
#    c) Sort students according to marks.

students = [
    ("Aisha", 85),
    ("Rahul", 70),
    ("Sneha", 92),
    ("Aman", 78)
]

def average_marks(students):
    marks = list(map(lambda student: student[1], students))
    return sum(marks) / len(marks)

above_75 = list(filter(lambda student: student[1] > 75, students))

sorted_students = sorted(students, key=lambda student: student[1])

print("Average marks:", average_marks(students))
print("Students scoring above 75:", above_75)
print("Students sorted by marks:", sorted_students)


#50. Take employee records containing name, department, and salary, use filter(), map(), and sorted() with lambda functions to:
#    a) Find employees earning more than ₹50,000.
#    b) Increase salaries by 10%.
#    c) Sort employees according to salary.

employees = [
    ("Aisha", "IT", 60000),
    ("Rahul", "HR", 45000),
    ("Sneha", "IT", 75000),
    ("Aman", "Sales", 50000)
]

above_50000 = list(filter(lambda employee: employee[2] > 50000, employees))

increased = list(map(
    lambda employee: (employee[0], employee[1], employee[2] * 1.10),
    employees
))

sorted_employees = sorted(employees, key=lambda employee: employee[2])

print("Employees earning more than ₹50,000:", above_50000)
print("Salaries after 10% increase:", increased)
print("Employees sorted according to salary:", sorted_employees)


#51. Take a list of products with names, prices, and quantities, use functions and lambda expressions to:
#    a) Calculate total value of each product.
#    b) Filter products costing more than ₹1,000.
#    c) Sort products according to total value.

products = [
    ("Laptop", 50000, 2),
    ("Mouse", 800, 3),
    ("Keyboard", 1500, 2),
    ("Monitor", 12000, 1)
]

def total_value(product):
    return product[1] * product[2]

values = list(map(
    lambda product: (product[0], total_value(product)),
    products
))

above_1000 = list(filter(
    lambda product: total_value(product) > 1000,
    products
))

sorted_products = sorted(
    products,
    key=lambda product: total_value(product)
)

print("Total value of products:", values)
print("Products costing more than ₹1,000:", above_1000)
print("Products sorted according to total value:", sorted_products)


#52. Write a program using functions, map(), filter(), and lambda expressions to process a list of words and:
#    a) Find the length of every word.
#    b) Extract words having more than five characters.
#    c) Sort words according to their length.

words = ["Python", "Java", "Programming", "Code", "Computer", "AI"]

def word_lengths(words):
    return list(map(lambda word: len(word), words))

long_words = list(filter(lambda word: len(word) > 5, words))

sorted_words = sorted(words, key=lambda word: len(word))

print("Length of every word:", word_lengths(words))
print("Words having more than five characters:", long_words)
print("Words sorted according to length:", sorted_words)