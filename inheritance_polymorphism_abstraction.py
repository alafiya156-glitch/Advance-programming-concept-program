# INHERITANCE


# 1. Create a class Employee with attributes emp_id, name, and salary.
# Create a derived class Manager that inherits from Employee and contains
# an additional attribute department. Display all employee and manager
# details and calculate the manager's annual salary.

class Employee:
    def __init__(self, emp_id, name, salary):
        self.emp_id = emp_id
        self.name = name
        self.salary = salary

class Manager(Employee):
    def __init__(self, emp_id, name, salary, department):
        Employee.__init__(self, emp_id, name, salary)
        self.department = department

    def display(self):
        print("Employee ID:", self.emp_id)
        print("Name:", self.name)
        print("Salary:", self.salary)
        print("Department:", self.department)
        print("Annual Salary:", self.salary * 12)

m = Manager(101, "Ali", 50000, "IT")
m.display()


# 2. Create a base class Vehicle with attributes brand and model.
# Create a derived class Car with additional attributes fuel_type and price.
# Define methods to display vehicle details and calculate the discounted
# price of the car.

class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

class Car(Vehicle):
    def __init__(self, brand, model, fuel_type, price):
        Vehicle.__init__(self, brand, model)
        self.fuel_type = fuel_type
        self.price = price

    def display(self):
        print("Brand:", self.brand)
        print("Model:", self.model)
        print("Fuel Type:", self.fuel_type)
        print("Price:", self.price)
        print("Discounted Price:", self.price * 0.90)

c = Car("Toyota", "Fortuner", "Diesel", 3000000)
c.display()


# 3. Create two classes Academic and Sports. The Academic class should
# store marks obtained by a student, while the Sports class should store
# sports points. Create a class Student that inherits from both classes
# and calculates the student's overall performance.

class Academic:
    def __init__(self, marks):
        self.marks = marks

class Sports:
    def __init__(self, points):
        self.points = points

class Student(Academic, Sports):
    def __init__(self, marks, points):
        Academic.__init__(self, marks)
        Sports.__init__(self, points)

    def display(self):
        print("Academic Marks:", self.marks)
        print("Sports Points:", self.points)
        print("Overall Performance:", self.marks + self.points)

s = Student(80, 15)
s.display()


# 4. Create classes PersonalDetails and ProfessionalDetails.
# Store personal information such as name and age in the first class
# and employee ID, designation, and salary in the second class.
# Create an Employee class that inherits from both classes and displays
# complete employee information.

class PersonalDetails:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class ProfessionalDetails:
    def __init__(self, emp_id, designation, salary):
        self.emp_id = emp_id
        self.designation = designation
        self.salary = salary

class Employee(PersonalDetails, ProfessionalDetails):
    def __init__(self, name, age, emp_id, designation, salary):
        PersonalDetails.__init__(self, name, age)
        ProfessionalDetails.__init__(self, emp_id, designation, salary)

    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("Employee ID:", self.emp_id)
        print("Designation:", self.designation)
        print("Salary:", self.salary)

e = Employee("Ali", 25, 101, "Developer", 50000)
e.display()


# 5. Create a class Person containing name and age. Derive a class Student
# from Person with roll number and course. Further derive a class
# ResearchStudent from Student with research topic and guide name.
# Display all details.

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Student(Person):
    def __init__(self, name, age, roll_no, course):
        Person.__init__(self, name, age)
        self.roll_no = roll_no
        self.course = course

class ResearchStudent(Student):
    def __init__(self, name, age, roll_no, course, topic, guide):
        Student.__init__(self, name, age, roll_no, course)
        self.topic = topic
        self.guide = guide

    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("Roll No:", self.roll_no)
        print("Course:", self.course)
        print("Research Topic:", self.topic)
        print("Guide:", self.guide)

r = ResearchStudent("Ali", 22, 101, "B.Tech", "AI", "Dr. Khan")
r.display()


# 6. Create a base class BankAccount with account number and balance.
# Derive SavingsAccount from it with an interest rate. Further derive
# PremiumSavingsAccount with additional benefits. Define methods to
# calculate interest and display account details.

class BankAccount:
    def __init__(self, account_no, balance):
        self.account_no = account_no
        self.balance = balance

class SavingsAccount(BankAccount):
    def __init__(self, account_no, balance, rate):
        BankAccount.__init__(self, account_no, balance)
        self.rate = rate

    def interest(self):
        return self.balance * self.rate / 100

class PremiumSavingsAccount(SavingsAccount):
    def display(self):
        print("Account No:", self.account_no)
        print("Balance:", self.balance)
        print("Interest:", self.interest())
        print("Benefits: Free transactions")

p = PremiumSavingsAccount(1001, 50000, 5)
p.display()


# 7. Create a base class Shape containing a method to display the name
# of the shape. Create three derived classes Circle, Rectangle, and
# Triangle. Each class should implement its own method to calculate the area.

class Shape:
    def display(self):
        print("This is a shape")

class Circle(Shape):
    def area(self):
        r = 5
        print("Circle Area:", 3.14 * r * r)

class Rectangle(Shape):
    def area(self):
        l = 10
        b = 5
        print("Rectangle Area:", l * b)

class Triangle(Shape):
    def area(self):
        b = 10
        h = 5
        print("Triangle Area:", 0.5 * b * h)

c = Circle()
c.display()
c.area()

r = Rectangle()
r.display()
r.area()

t = Triangle()
t.display()
t.area()


# 8. Create a base class Employee containing employee ID, name, and
# basic salary. Create derived classes Manager, Developer, and Tester.
# Each derived class should calculate salary differently based on its
# respective allowances.

class Employee:
    def __init__(self, emp_id, name, salary):
        self.emp_id = emp_id
        self.name = name
        self.salary = salary

class Manager(Employee):
    def salary_calculation(self):
        return self.salary + self.salary * 30 / 100

class Developer(Employee):
    def salary_calculation(self):
        return self.salary + self.salary * 20 / 100

class Tester(Employee):
    def salary_calculation(self):
        return self.salary + self.salary * 10 / 100

m = Manager(101, "Ali", 50000)
d = Developer(102, "Sara", 50000)
t = Tester(103, "John", 50000)

print("Manager Salary:", m.salary_calculation())
print("Developer Salary:", d.salary_calculation())
print("Tester Salary:", t.salary_calculation())


# 9. Create a class Person. Derive Student and Faculty from Person.
# Create another class TeachingAssistant that inherits from both Student
# and Faculty. Display the details and demonstrate the use of multiple
# and hierarchical inheritance together.

class Person:
    def __init__(self, name):
        self.name = name

class Student(Person):
    def study(self):
        print(self.name, "is studying")

class Faculty(Person):
    def teach(self):
        print(self.name, "is teaching")

class TeachingAssistant(Student, Faculty):
    def display(self):
        print("Name:", self.name)
        self.study()
        self.teach()

ta = TeachingAssistant("Ali")
ta.display()


# 10. Create a base class Vehicle. Derive Car and Bike from Vehicle.
# Create a class SportsCar that inherits from Car and another class
# ElectricBike that inherits from Bike. Add suitable attributes and
# methods to demonstrate a combination of inheritance types.

class Vehicle:
    def __init__(self, brand):
        self.brand = brand

class Car(Vehicle):
    def car_info(self):
        print("Car Brand:", self.brand)

class Bike(Vehicle):
    def bike_info(self):
        print("Bike Brand:", self.brand)

class SportsCar(Car):
    def speed(self):
        print("Sports Car Speed: 250 km/h")

class ElectricBike(Bike):
    def battery(self):
        print("Battery: 5 kWh")

sc = SportsCar("BMW")
sc.car_info()
sc.speed()

eb = ElectricBike("Ola")
eb.bike_info()
eb.battery()


# 11. Create a base class Student with attributes roll_no, name, and course.
# Derive a class Result that stores marks in three subjects and calculates
# total marks, percentage, and grade.

class Student:
    def __init__(self, roll_no, name, course):
        self.roll_no = roll_no
        self.name = name
        self.course = course

class Result(Student):
    def __init__(self, roll_no, name, course, marks):
        Student.__init__(self, roll_no, name, course)
        self.marks = marks

    def display(self):
        total = sum(self.marks)
        percentage = total / 3

        if percentage >= 75:
            grade = "A"
        elif percentage >= 60:
            grade = "B"
        elif percentage >= 50:
            grade = "C"
        else:
            grade = "F"

        print("Name:", self.name)
        print("Total Marks:", total)
        print("Percentage:", percentage)
        print("Grade:", grade)

r = Result(101, "Ali", "B.Tech", [80, 75, 85])
r.display()


# 12. Create a class Product with product ID, name, and price.
# Derive ElectronicProduct with additional attributes such as brand
# and warranty. Calculate the final price after applying a discount.

class Product:
    def __init__(self, product_id, name, price):
        self.product_id = product_id
        self.name = name
        self.price = price

class ElectronicProduct(Product):
    def __init__(self, product_id, name, price, brand, warranty):
        Product.__init__(self, product_id, name, price)
        self.brand = brand
        self.warranty = warranty

    def display(self):
        print("Product ID:", self.product_id)
        print("Name:", self.name)
        print("Brand:", self.brand)
        print("Warranty:", self.warranty)
        print("Final Price:", self.price * 0.90)

e = ElectronicProduct(101, "Laptop", 50000, "Dell", 2)
e.display()


# 13. Create classes Printer and Scanner with suitable methods for printing
# and scanning documents. Create a MultifunctionDevice class that inherits
# from both and supports both operations.

class Printer:
    def print_document(self):
        print("Printing document")

class Scanner:
    def scan_document(self):
        print("Scanning document")

class MultifunctionDevice(Printer, Scanner):
    pass

m = MultifunctionDevice()
m.print_document()
m.scan_document()


# 14. Create classes Camera and Phone. The Camera class should provide
# methods for taking photographs, while Phone should provide methods
# for making calls. Create a Smartphone class inheriting from both.

class Camera:
    def take_photo(self):
        print("Photo taken")

class Phone:
    def make_call(self):
        print("Calling...")

class Smartphone(Camera, Phone):
    pass

s = Smartphone()
s.take_photo()
s.make_call()


# 15. Create a class Person with name and age. Derive Student with
# roll number and course. Further derive ResearchStudent with research
# topic and guide name.

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Student(Person):
    def __init__(self, name, age, roll_no, course):
        Person.__init__(self, name, age)
        self.roll_no = roll_no
        self.course = course

class ResearchStudent(Student):
    def __init__(self, name, age, roll_no, course, topic, guide):
        Student.__init__(self, name, age, roll_no, course)
        self.topic = topic
        self.guide = guide

    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("Roll No:", self.roll_no)
        print("Course:", self.course)
        print("Research Topic:", self.topic)
        print("Guide:", self.guide)

r = ResearchStudent("Sara", 24, 102, "B.Tech", "Cloud Computing", "Dr. Khan")
r.display()


# 16. Create a class Person with name and age. Derive Student with
# roll number and course. Further derive ResearchStudent with research
# topic and guide name.

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Student(Person):
    def __init__(self, name, age, roll_no, course):
        Person.__init__(self, name, age)
        self.roll_no = roll_no
        self.course = course

class ResearchStudent(Student):
    def __init__(self, name, age, roll_no, course, topic, guide):
        Student.__init__(self, name, age, roll_no, course)
        self.topic = topic
        self.guide = guide

    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("Roll No:", self.roll_no)
        print("Course:", self.course)
        print("Research Topic:", self.topic)
        print("Guide:", self.guide)

r = ResearchStudent("Ahmed", 23, 103, "B.Tech", "Machine Learning", "Dr. Sharma")
r.display()


# 17. Create a base class Animal with common attributes and methods.
# Derive Dog, Cat, and Cow classes and implement their specific sounds
# and behaviors.

class Animal:
    def __init__(self, name):
        self.name = name

    def eat(self):
        print(self.name, "is eating")

class Dog(Animal):
    def sound(self):
        print("Dog says: Woof")

class Cat(Animal):
    def sound(self):
        print("Cat says: Meow")

class Cow(Animal):
    def sound(self):
        print("Cow says: Moo")

d = Dog("Dog")
d.eat()
d.sound()

c = Cat("Cat")
c.eat()
c.sound()

co = Cow("Cow")
co.eat()
co.sound()


# 18. Create a class Person and derive Doctor and Patient.
# Create additional classes representing Surgeon and MedicalResearcher.
# Design the hierarchy so that the program demonstrates multiple
# inheritance along with hierarchical inheritance.

class Person:
    def __init__(self, name):
        self.name = name

class Doctor(Person):
    def treat(self):
        print(self.name, "treats patients")

class Patient(Person):
    def checkup(self):
        print(self.name, "is under checkup")

class Surgeon(Doctor):
    def surgery(self):
        print(self.name, "performs surgery")

class MedicalResearcher(Doctor, Patient):
    def research(self):
        print(self.name, "does medical research")

s = Surgeon("Dr. Ali")
s.treat()
s.surgery()

m = MedicalResearcher("Dr. Sara")
m.treat()
m.checkup()
m.research()

# POLYMORPHISM


# 1. Create a base class Shape with a method area(). Derive Circle,
# Rectangle, and Triangle classes and override the area() method in each
# class. Create objects of each class and demonstrate runtime polymorphism.

class Shape:
    def area(self):
        pass

class Circle(Shape):
    def area(self):
        print("Circle Area:", 3.14 * 5 * 5)

class Rectangle(Shape):
    def area(self):
        print("Rectangle Area:", 10 * 5)

class Triangle(Shape):
    def area(self):
        print("Triangle Area:", 0.5 * 10 * 5)

shapes = [Circle(), Rectangle(), Triangle()]

for s in shapes:
    s.area()


# 2. Create a base class Employee with a method calculate_salary().
# Derive Manager, Developer, and Tester classes. Override the method
# in each class to calculate salary according to the employee's role.

class Employee:
    def calculate_salary(self):
        pass

class Manager(Employee):
    def calculate_salary(self):
        print("Manager Salary:", 60000)

class Developer(Employee):
    def calculate_salary(self):
        print("Developer Salary:", 50000)

class Tester(Employee):
    def calculate_salary(self):
        print("Tester Salary:", 40000)

employees = [Manager(), Developer(), Tester()]

for e in employees:
    e.calculate_salary()


# 3. Create a base class Vehicle with a method start(). Derive Car,
# Bike, and Bus classes and override start() to display the starting
# behavior of each vehicle.

class Vehicle:
    def start(self):
        pass

class Car(Vehicle):
    def start(self):
        print("Car starts with a key")

class Bike(Vehicle):
    def start(self):
        print("Bike starts with a button")

class Bus(Vehicle):
    def start(self):
        print("Bus starts with a key")

vehicles = [Car(), Bike(), Bus()]

for v in vehicles:
    v.start()


# 4. Create a base class Animal with a method sound(). Create subclasses
# Dog, Cat, Cow, and Lion. Override sound() in each class to display
# the appropriate sound.

class Animal:
    def sound(self):
        pass

class Dog(Animal):
    def sound(self):
        print("Dog: Woof")

class Cat(Animal):
    def sound(self):
        print("Cat: Meow")

class Cow(Animal):
    def sound(self):
        print("Cow: Moo")

class Lion(Animal):
    def sound(self):
        print("Lion: Roar")

animals = [Dog(), Cat(), Cow(), Lion()]

for a in animals:
    a.sound()


# 5. Create a base class Notification with a method send().
# Derive EmailNotification, SMSNotification, and PushNotification.
# Override send() to display the appropriate notification method.

class Notification:
    def send(self):
        pass

class EmailNotification(Notification):
    def send(self):
        print("Sending Email")

class SMSNotification(Notification):
    def send(self):
        print("Sending SMS")

class PushNotification(Notification):
    def send(self):
        print("Sending Push Notification")

notifications = [EmailNotification(), SMSNotification(), PushNotification()]

for n in notifications:
    n.send()


# 6. Create a base class Student with a method calculate_grade().
# Derive EngineeringStudent, MedicalStudent, and ManagementStudent.
# Override the method according to different grading criteria.

class Student:
    def calculate_grade(self):
        pass

class EngineeringStudent(Student):
    def calculate_grade(self):
        print("Engineering Grade: A")

class MedicalStudent(Student):
    def calculate_grade(self):
        print("Medical Grade: B")

class ManagementStudent(Student):
    def calculate_grade(self):
        print("Management Grade: A")

students = [EngineeringStudent(), MedicalStudent(), ManagementStudent()]

for s in students:
    s.calculate_grade()


# 7. Create a base class BankAccount with a method calculate_interest().
# Derive SavingsAccount, CurrentAccount, and FixedDepositAccount.
# Override the method to calculate interest differently for each account type.

class BankAccount:
    def calculate_interest(self):
        pass

class SavingsAccount(BankAccount):
    def calculate_interest(self):
        print("Savings Account Interest: 5%")

class CurrentAccount(BankAccount):
    def calculate_interest(self):
        print("Current Account Interest: 2%")

class FixedDepositAccount(BankAccount):
    def calculate_interest(self):
        print("Fixed Deposit Interest: 7%")

accounts = [SavingsAccount(), CurrentAccount(), FixedDepositAccount()]

for a in accounts:
    a.calculate_interest()


# 8. Create a base class Report with a method generate().
# Derive PDFReport, ExcelReport, and HTMLReport. Override generate()
# in each class. Write a function that accepts any report object
# and calls generate().

class Report:
    def generate(self):
        pass

class PDFReport(Report):
    def generate(self):
        print("PDF Report Generated")

class ExcelReport(Report):
    def generate(self):
        print("Excel Report Generated")

class HTMLReport(Report):
    def generate(self):
        print("HTML Report Generated")

def create_report(report):
    report.generate()

create_report(PDFReport())
create_report(ExcelReport())
create_report(HTMLReport())


# 9. Create a class Distance with feet and inches. Overload the +
# operator to add two distance objects and display the result in
# normalized form.

class Distance:
    def __init__(self, feet, inches):
        self.feet = feet
        self.inches = inches

    def __add__(self, other):
        feet = self.feet + other.feet
        inches = self.inches + other.inches

        if inches >= 12:
            feet += inches // 12
            inches = inches % 12

        return Distance(feet, inches)

    def display(self):
        print(self.feet, "feet", self.inches, "inches")

d1 = Distance(5, 8)
d2 = Distance(3, 7)

d3 = d1 + d2
d3.display()


# 10. Create a class Student containing the student's name and total marks.
# Overload the > and < operators to compare the marks of two students.

class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def __gt__(self, other):
        return self.marks > other.marks

    def __lt__(self, other):
        return self.marks < other.marks

s1 = Student("Ali", 85)
s2 = Student("Sara", 75)

print("Ali has greater marks:", s1 > s2)
print("Ali has lower marks:", s1 < s2)


# 11. Create a class Product with product name and price.
# Overload the == and > operators to compare two products
# based on their prices.

class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __eq__(self, other):
        return self.price == other.price

    def __gt__(self, other):
        return self.price > other.price

p1 = Product("Laptop", 50000)
p2 = Product("Mobile", 30000)

print("Prices are equal:", p1 == p2)
print("Laptop is more expensive:", p1 > p2)


# 12. Develop an online shopping payment module using polymorphism.
# Create a base class Payment and derived classes UPIPayment,
# CardPayment, and WalletPayment. Each class should implement its
# own make_payment() method. Demonstrate polymorphism using a
# common function.

class Payment:
    def make_payment(self):
        pass

class UPIPayment(Payment):
    def make_payment(self):
        print("Payment made using UPI")

class CardPayment(Payment):
    def make_payment(self):
        print("Payment made using Card")

class WalletPayment(Payment):
    def make_payment(self):
        print("Payment made using Wallet")

def payment_method(payment):
    payment.make_payment()

payment_method(UPIPayment())
payment_method(CardPayment())
payment_method(WalletPayment())


# 13. Create a base class Person with a method display_role().
# Derive Student, Faculty, and Administrator. Override the method
# to display the respective role. Store all objects in a list and
# invoke the same method using a loop.

class Person:
    def display_role(self):
        pass

class Student(Person):
    def display_role(self):
        print("Role: Student")

class Faculty(Person):
    def display_role(self):
        print("Role: Faculty")

class Administrator(Person):
    def display_role(self):
        print("Role: Administrator")

people = [Student(), Faculty(), Administrator()]

for p in people:
    p.display_role()


# 14. Create a base class Media with a method play().
# Derive Audio, Video, and Podcast. Override play() according
# to the media type.

class Media:
    def play(self):
        pass

class Audio(Media):
    def play(self):
        print("Playing Audio")

class Video(Media):
    def play(self):
        print("Playing Video")

class Podcast(Media):
    def play(self):
        print("Playing Podcast")

media = [Audio(), Video(), Podcast()]

for m in media:
    m.play()


# 15. Create a base class SmartDevice with methods turn_on() and
# turn_off(). Derive Light, Fan, AC, and TV. Override the methods
# according to each device.

class SmartDevice:
    def turn_on(self):
        pass

    def turn_off(self):
        pass

class Light(SmartDevice):
    def turn_on(self):
        print("Light ON")

    def turn_off(self):
        print("Light OFF")

class Fan(SmartDevice):
    def turn_on(self):
        print("Fan ON")

    def turn_off(self):
        print("Fan OFF")

class AC(SmartDevice):
    def turn_on(self):
        print("AC ON")

    def turn_off(self):
        print("AC OFF")

class TV(SmartDevice):
    def turn_on(self):
        print("TV ON")

    def turn_off(self):
        print("TV OFF")

devices = [Light(), Fan(), AC(), TV()]

for d in devices:
    d.turn_on()
    d.turn_off()

    # ABSTRACTION

    from abc import ABC, abstractmethod


    # 1. Create an abstract class Shape with an abstract method area().
    # Derive Circle, Rectangle, and Triangle classes and implement the
    # area() method for each shape. Create objects of the derived classes
    # and display their areas.

    class Shape(ABC):
        @abstractmethod
        def area(self):
            pass


    class Circle(Shape):
        def area(self):
            print("Circle Area:", 3.14 * 5 * 5)


    class Rectangle(Shape):
        def area(self):
            print("Rectangle Area:", 10 * 5)


    class Triangle(Shape):
        def area(self):
            print("Triangle Area:", 0.5 * 10 * 5)


    c = Circle()
    r = Rectangle()
    t = Triangle()

    c.area()
    r.area()
    t.area()


    # 2. Create an abstract class Vehicle with abstract methods start()
    # and stop(). Derive Car, Bike, and Bus classes and implement
    # these methods.

    class Vehicle(ABC):
        @abstractmethod
        def start(self):
            pass

        @abstractmethod
        def stop(self):
            pass


    class Car(Vehicle):
        def start(self):
            print("Car Started")

        def stop(self):
            print("Car Stopped")


    class Bike(Vehicle):
        def start(self):
            print("Bike Started")

        def stop(self):
            print("Bike Stopped")


    class Bus(Vehicle):
        def start(self):
            print("Bus Started")

        def stop(self):
            print("Bus Stopped")


    c = Car()
    c.start()
    c.stop()

    b = Bike()
    b.start()
    b.stop()

    bus = Bus()
    bus.start()
    bus.stop()


    # 3. Create an abstract class BankAccount with abstract methods
    # deposit() and withdraw(). Derive SavingsAccount and CurrentAccount
    # and implement the required operations.

    class BankAccount(ABC):
        @abstractmethod
        def deposit(self, amount):
            pass

        @abstractmethod
        def withdraw(self, amount):
            pass


    class SavingsAccount(BankAccount):
        def deposit(self, amount):
            print("Savings Deposit:", amount)

        def withdraw(self, amount):
            print("Savings Withdrawal:", amount)


    class CurrentAccount(BankAccount):
        def deposit(self, amount):
            print("Current Deposit:", amount)

        def withdraw(self, amount):
            print("Current Withdrawal:", amount)


    s = SavingsAccount()
    s.deposit(5000)
    s.withdraw(1000)

    c = CurrentAccount()
    c.deposit(10000)
    c.withdraw(2000)


    # 4. Create an abstract class FoodOrder with abstract methods
    # calculate_bill() and delivery_charge(). Derive RestaurantOrder
    # and HomeDeliveryOrder and implement the methods appropriately.

    class FoodOrder(ABC):
        @abstractmethod
        def calculate_bill(self):
            pass

        @abstractmethod
        def delivery_charge(self):
            pass


    class RestaurantOrder(FoodOrder):
        def calculate_bill(self):
            print("Food Bill: 500")

        def delivery_charge(self):
            print("Delivery Charge: 0")


    class HomeDeliveryOrder(FoodOrder):
        def calculate_bill(self):
            print("Food Bill: 500")

        def delivery_charge(self):
            print("Delivery Charge: 50")


    r = RestaurantOrder()
    r.calculate_bill()
    r.delivery_charge()

    h = HomeDeliveryOrder()
    h.calculate_bill()
    h.delivery_charge()


    # 5. Create an abstract class Patient with abstract methods
    # calculate_bill() and treatment(). Derive InPatient, OutPatient,
    # and EmergencyPatient classes and implement the methods according
    # to the patient type.

    class Patient(ABC):
        @abstractmethod
        def calculate_bill(self):
            pass

        @abstractmethod
        def treatment(self):
            pass


    class InPatient(Patient):
        def calculate_bill(self):
            print("In-Patient Bill: 5000")

        def treatment(self):
            print("In-Patient Treatment")


    class OutPatient(Patient):
        def calculate_bill(self):
            print("Out-Patient Bill: 1000")

        def treatment(self):
            print("Out-Patient Treatment")


    class EmergencyPatient(Patient):
        def calculate_bill(self):
            print("Emergency Bill: 10000")

        def treatment(self):
            print("Emergency Treatment")


    i = InPatient()
    i.calculate_bill()
    i.treatment()

    o = OutPatient()
    o.calculate_bill()
    o.treatment()

    e = EmergencyPatient()
    e.calculate_bill()
    e.treatment()


    # 6. Create an abstract class Transport with an abstract method
    # calculate_fare(distance). Implement subclasses:
    # a) Bus
    # b) Train
    # c) Taxi
    # d) Flight
    # Calculate the fare according to the transportation type.

    class Transport(ABC):
        @abstractmethod
        def calculate_fare(self, distance):
            pass


    class Bus(Transport):
        def calculate_fare(self, distance):
            print("Bus Fare:", distance * 2)


    class Train(Transport):
        def calculate_fare(self, distance):
            print("Train Fare:", distance * 3)


    class Taxi(Transport):
        def calculate_fare(self, distance):
            print("Taxi Fare:", distance * 10)


    class Flight(Transport):
        def calculate_fare(self, distance):
            print("Flight Fare:", distance * 20)


    distance = 100

    Bus().calculate_fare(distance)
    Train().calculate_fare(distance)
    Taxi().calculate_fare(distance)
    Flight().calculate_fare(distance)


    # 7. Create an abstract class Question with an abstract method
    # evaluate_answer(). Derive:
    # a) MCQQuestion
    # b) TrueFalseQuestion
    # c) DescriptiveQuestion
    # Implement answer evaluation for each question type.

    class Question(ABC):
        @abstractmethod
        def evaluate_answer(self):
            pass


    class MCQQuestion(Question):
        def evaluate_answer(self):
            print("MCQ Answer Evaluated")


    class TrueFalseQuestion(Question):
        def evaluate_answer(self):
            print("True/False Answer Evaluated")


    class DescriptiveQuestion(Question):
        def evaluate_answer(self):
            print("Descriptive Answer Evaluated")


    MCQQuestion().evaluate_answer()
    TrueFalseQuestion().evaluate_answer()
    DescriptiveQuestion().evaluate_answer()


    # 8. Create an abstract class Authentication with an abstract method
    # authenticate(). Implement the method using:
    # a) Password authentication
    # b) OTP authentication
    # c) Biometric authentication
    # Demonstrate abstraction by interacting with objects through the
    # abstract interface.

    class Authentication(ABC):
        @abstractmethod
        def authenticate(self):
            pass


    class PasswordAuthentication(Authentication):
        def authenticate(self):
            print("Login using Password")


    class OTPAuthentication(Authentication):
        def authenticate(self):
            print("Login using OTP")


    class BiometricAuthentication(Authentication):
        def authenticate(self):
            print("Login using Biometric")


    PasswordAuthentication().authenticate()
    OTPAuthentication().authenticate()
    BiometricAuthentication().authenticate()


    # 9. Create an abstract class CloudStorage with abstract methods:
    # a) upload_file()
    # b) download_file()
    # c) delete_file()
    # Create subclasses representing different storage services
    # and implement the operations.

    class CloudStorage(ABC):
        @abstractmethod
        def upload_file(self):
            pass

        @abstractmethod
        def download_file(self):
            pass

        @abstractmethod
        def delete_file(self):
            pass


    class GoogleDrive(CloudStorage):
        def upload_file(self):
            print("File uploaded to Google Drive")

        def download_file(self):
            print("File downloaded from Google Drive")

        def delete_file(self):
            print("File deleted from Google Drive")


    class OneDrive(CloudStorage):
        def upload_file(self):
            print("File uploaded to OneDrive")

        def download_file(self):
            print("File downloaded from OneDrive")

        def delete_file(self):
            print("File deleted from OneDrive")


    g = GoogleDrive()
    g.upload_file()
    g.download_file()
    g.delete_file()

    o = OneDrive()
    o.upload_file()
    o.download_file()
    o.delete_file()


    # 10. Create an abstract class Appointment with abstract methods
    # book_appointment() and calculate_fee(). Derive GeneralAppointment,
    # SpecialistAppointment, and EmergencyAppointment.

    class Appointment(ABC):
        @abstractmethod
        def book_appointment(self):
            pass

        @abstractmethod
        def calculate_fee(self):
            pass


    class GeneralAppointment(Appointment):
        def book_appointment(self):
            print("General Appointment Booked")

        def calculate_fee(self):
            print("Fee: 500")


    class SpecialistAppointment(Appointment):
        def book_appointment(self):
            print("Specialist Appointment Booked")

        def calculate_fee(self):
            print("Fee: 1000")


    class EmergencyAppointment(Appointment):
        def book_appointment(self):
            print("Emergency Appointment Booked")

        def calculate_fee(self):
            print("Fee: 2000")


    g = GeneralAppointment()
    g.book_appointment()
    g.calculate_fee()

    s = SpecialistAppointment()
    s.book_appointment()
    s.calculate_fee()

    e = EmergencyAppointment()
    e.book_appointment()
    e.calculate_fee()