# 1. Create a class Student with attributes roll_no, name, and marks.
# Create objects for multiple students and display their details and percentage.

class Student:
    def __init__(self, roll_no, name, marks):
        self.roll_no = roll_no
        self.name = name
        self.marks = marks

    def display(self):
        percentage = sum(self.marks) / len(self.marks)
        print("Roll No:", self.roll_no)
        print("Name:", self.name)
        print("Marks:", self.marks)
        print("Percentage:", percentage, "%")
        print()

s1 = Student(1, "Ali", [80, 75, 90, 85, 88])
s2 = Student(2, "Sara", [85, 82, 78, 90, 88])

s1.display()
s2.display()


# 2. Create a class Employee with attributes emp_id, name, and basic_salary.
# Define methods to calculate HRA, DA, and gross salary.

class Employee:
    def __init__(self, emp_id, name, basic_salary):
        self.emp_id = emp_id
        self.name = name
        self.basic_salary = basic_salary

    def calculate_salary(self):
        hra = self.basic_salary * 0.20
        da = self.basic_salary * 0.10
        gross = self.basic_salary + hra + da

        print("Employee ID:", self.emp_id)
        print("Name:", self.name)
        print("HRA:", hra)
        print("DA:", da)
        print("Gross Salary:", gross)
        print()

e = Employee(101, "Rahul", 30000)
e.calculate_salary()


# 3. Create a class Rectangle with attributes length and breadth.
# Define methods to calculate area and perimeter.

class Rectangle:
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def area(self):
        return self.length * self.breadth

    def perimeter(self):
        return 2 * (self.length + self.breadth)

r = Rectangle(10, 5)
print("Rectangle Area:", r.area())
print("Rectangle Perimeter:", r.perimeter())
print()


# 4. Create a class Circle with an attribute radius.
# Define methods to calculate area and circumference.

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius

    def circumference(self):
        return 2 * 3.14 * self.radius

c = Circle(7)
print("Circle Area:", c.area())
print("Circle Circumference:", c.circumference())
print()


# 5. Create a class Book containing book_id, title, author, and price.
# Create objects for three books and display their information.

class Book:
    def __init__(self, book_id, title, author, price):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.price = price

    def display(self):
        print("Book ID:", self.book_id)
        print("Title:", self.title)
        print("Author:", self.author)
        print("Price:", self.price)
        print()

b1 = Book(1, "Python Basics", "John", 450)
b2 = Book(2, "Data Structures", "James", 550)
b3 = Book(3, "Cloud Computing", "Robert", 600)

b1.display()
b2.display()
b3.display()


# 6. Create a class ElectricityBill containing consumer number,
# consumer name, and units consumed.
# Define a method to calculate electricity bill according to different unit slabs.

class ElectricityBill:
    def __init__(self, consumer_no, consumer_name, units):
        self.consumer_no = consumer_no
        self.consumer_name = consumer_name
        self.units = units

    def calculate_bill(self):
        if self.units <= 100:
            bill = self.units * 2
        elif self.units <= 200:
            bill = 100 * 2 + (self.units - 100) * 3
        else:
            bill = 100 * 2 + 100 * 3 + (self.units - 200) * 5

        print("Consumer No:", self.consumer_no)
        print("Consumer Name:", self.consumer_name)
        print("Units Consumed:", self.units)
        print("Electricity Bill:", bill)
        print()

eb = ElectricityBill(101, "Amit", 250)
eb.calculate_bill()


# 7. Create a class MobilePhone with attributes brand, model, storage, and price.
# Define methods to display specifications and calculate price after discount.

class MobilePhone:
    def __init__(self, brand, model, storage, price):
        self.brand = brand
        self.model = model
        self.storage = storage
        self.price = price

    def display(self):
        print("Brand:", self.brand)
        print("Model:", self.model)
        print("Storage:", self.storage)
        print("Price:", self.price)

    def discounted_price(self, discount):
        return self.price - (self.price * discount / 100)

m = MobilePhone("Samsung", "S24", "256 GB", 70000)
m.display()
print("Price after 10% discount:", m.discounted_price(10))
print()


# 8. Create a class Patient containing patient ID, name, age, disease,
# and consultation fee.
# Define methods to display patient information and calculate total bill.

class Patient:
    def __init__(self, patient_id, name, age, disease, consultation_fee):
        self.patient_id = patient_id
        self.name = name
        self.age = age
        self.disease = disease
        self.consultation_fee = consultation_fee

    def display(self):
        print("Patient ID:", self.patient_id)
        print("Name:", self.name)
        print("Age:", self.age)
        print("Disease:", self.disease)
        print("Consultation Fee:", self.consultation_fee)

    def total_bill(self, medicine_charge):
        return self.consultation_fee + medicine_charge

p = Patient(1, "Ahmed", 25, "Fever", 500)
p.display()
print("Total Bill:", p.total_bill(800))
print()


# 9. Design an ATM class that allows a user to:
# a) Check balance
# b) Deposit money
# c) Withdraw money
# d) Display account details
# Implement the operations through a menu-driven program.

class ATM:
    def __init__(self, account_no, name, balance):
        self.account_no = account_no
        self.name = name
        self.balance = balance

    def check_balance(self):
        print("Balance:", self.balance)

    def deposit(self, amount):
        self.balance += amount
        print("Amount Deposited:", amount)

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print("Amount Withdrawn:", amount)
        else:
            print("Insufficient Balance")

    def account_details(self):
        print("Account No:", self.account_no)
        print("Name:", self.name)
        print("Balance:", self.balance)


atm = ATM(1001, "Ali", 10000)

while True:
    print("\n1. Check Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Account Details")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        atm.check_balance()
    elif choice == 2:
        amount = float(input("Enter amount: "))
        atm.deposit(amount)
    elif choice == 3:
        amount = float(input("Enter amount: "))
        atm.withdraw(amount)
    elif choice == 4:
        atm.account_details()
    elif choice == 5:
        print("Thank you!")
        break
    else:
        print("Invalid Choice")


# 10. Create a class Vehicle containing vehicle number, model,
# rental rate, and availability.
# Implement methods to rent and return a vehicle and calculate rental charges.

class Vehicle:
    def __init__(self, vehicle_no, model, rental_rate):
        self.vehicle_no = vehicle_no
        self.model = model
        self.rental_rate = rental_rate
        self.available = True

    def rent(self):
        if self.available:
            self.available = False
            print("Vehicle rented successfully.")
        else:
            print("Vehicle is not available.")

    def return_vehicle(self):
        self.available = True
        print("Vehicle returned successfully.")

    def rental_charge(self, days):
        return self.rental_rate * days

v = Vehicle("MH12AB1234", "Honda City", 2000)

v.rent()
print("Rental Charge for 3 days:", v.rental_charge(3))
v.return_vehicle()
print()


# 11. Create a class ShoppingCart with customer name and cart ID.
# Initialize values using a constructor.
# Implement methods to add products, remove products, and calculate total bill.
# Use a destructor to display a message when the object is destroyed.

class ShoppingCart:
    def __init__(self, customer_name, cart_id):
        self.customer_name = customer_name
        self.cart_id = cart_id
        self.products = []

    def add_product(self, name, price):
        self.products.append([name, price])
        print(name, "added.")

    def remove_product(self, name):
        for product in self.products:
            if product[0] == name:
                self.products.remove(product)
                print(name, "removed.")
                return
        print("Product not found.")

    def total_bill(self):
        return sum(product[1] for product in self.products)

    def __del__(self):
        print("Shopping cart object destroyed.")


cart = ShoppingCart("Ali", 101)
cart.add_product("Laptop", 50000)
cart.add_product("Mouse", 1000)
print("Total Bill:", cart.total_bill())
cart.remove_product("Mouse")
print("Total Bill:", cart.total_bill())


# 12. Create a class FoodOrder with order ID, customer name,
# food item, quantity, and price.
# Use a constructor to initialize the order.
# Calculate total bill including tax.
# Implement a destructor to display an order completion message.

class FoodOrder:
    def __init__(self, order_id, customer_name, food_item, quantity, price):
        self.order_id = order_id
        self.customer_name = customer_name
        self.food_item = food_item
        self.quantity = quantity
        self.price = price

    def total_bill(self):
        total = self.quantity * self.price
        tax = total * 0.05
        return total + tax

    def display(self):
        print("Order ID:", self.order_id)
        print("Customer:", self.customer_name)
        print("Food Item:", self.food_item)
        print("Quantity:", self.quantity)
        print("Total Bill including tax:", self.total_bill())

    def __del__(self):
        print("Order completed.")


order = FoodOrder(101, "Sara", "Pizza", 2, 300)
order.display()


# 13. Create a class StudentResult with student name and marks in five subjects.
# Use a constructor to initialize the details.
# Define methods to calculate total, percentage, and grade.
# Implement a destructor to display a suitable message.

class StudentResult:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def total(self):
        return sum(self.marks)

    def percentage(self):
        return self.total() / 5

    def grade(self):
        percentage = self.percentage()

        if percentage >= 90:
            return "A+"
        elif percentage >= 80:
            return "A"
        elif percentage >= 70:
            return "B"
        elif percentage >= 60:
            return "C"
        elif percentage >= 50:
            return "D"
        else:
            return "F"

    def display(self):
        print("Student Name:", self.name)
        print("Total Marks:", self.total())
        print("Percentage:", self.percentage(), "%")
        print("Grade:", self.grade())

    def __del__(self):
        print("Student result object destroyed.")


result = StudentResult("Ali", [85, 90, 78, 88, 92])
result.display()