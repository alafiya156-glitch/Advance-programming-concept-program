#1.Write a Python program to create a tuple of five integers and display it.
from Practical.string import count

numbers=(10,20,30,40,50,60)
print(numbers)
#2.Create a tuple containing five city names. Display:
#First city
#Last city
#Third city
city=("Ichalkaranji","kolhpaur","Mumbai","pune","Nashik")
print(city[0])
print(city[4])
print(city[3])
#3.Create a tuple of student names and display the total number of students using the len() function.
student=("Alafiya","neha","shivangi","Mahi")
print("Total number of student",len(student))
#4.Create a tuple of colors. Check whether a given color exists in the tuple
color=("Black","Brwon","white","Nevy blue")
color1=input("Enter color: ")
for i in color:
    if color1 in color:
        print(color1,"is present in tuple")
#5.Create a tuple of fruits and display each fruit using a loop.
fruits=("Mango","Banana","Cherry","Black berry")
for i in fruits:
    print(fruits)
#6.Create a tuple with repeated numbers and count how many times a particular number appears.
repeated_num=(10,20,10,30,10)
num=int(input("Enter a number: "))
print("Print how many time given number repeated:",repeated_num.count(num))
#7.Create a tuple of employee IDs and find the index of a given ID.
emp=(101,102,103,104,105)
id=int(input("enter ID to find index:"))
if id in emp:
    print(emp.index(id))
else:
    print(id,"Not present in tuple")
#8.Create two tuples of numbers and concatenate them into a single tuple.
num1=(10,20)
num2=(30,40)
print(num1+num2)
#9.Create a tuple containing three elements and repeat it four times.
numbers=(10,20,30)
resulr=numbers*4
print("tuple after repating for 4 times",resulr)
#10.Create a tuple of 10 numbers and display:
#First five elements
#Last five elements
#Middle four elements
#Alternate elements
#Reverse tuple
tup=(10,20,30,40,50,60,70,80,90,100)
print("first five element: ",tup[:5])
print("last five element:",tup[5:])
print("Middle four element:",tup[3:7])
print("Aleternate element:",tup[::2])
print("reverse tuple:",tup[::-1])
#11.Convert a tuple into a list and add a new element.
nums=(10,20)
nums1=list(nums)
nums1.append(30)
print(nums1)
#12.Accept five numbers from the user, store them in a list, and convert the list into a tuple.
numbers=[]
for i in range(5):
    num=int(input("Enter a five numbers: "))
    numbers.append(num)
numbers1=tuple(numbers)
print(numbers1)
#13.Modify a tuple by converting it into a list and then back into a tuple.
tup_modify=(10,20)
mod1=list(tup_modify)
mod1.append(30)
mod2=tuple(mod1)
print("tuple after modify:",mod2)
#14.Create a tuple and delete it completely.
tup_del=(10,20,30)
del tup_del
print("Tuple deletd sucessfully!!")
#15.Create a nested tuple containing student details and display each record.
students = (
    ("Aisha", 1, 85),
    ("Rahul", 2, 78),
    ("Sneha", 3, 92)
)

for student in students:
    print("Name:", student[0])
    print("Roll Number:", student[1])
    print("Marks:", student[2])
    print()
#16.Store ten numbers in a tuple and calculate their sum.
numbers = (10, 20, 30, 40, 50, 60, 70, 80, 90, 100)

total = 0

for num in numbers:
    total = total + num

print("Sum:", total)
#17.Find the largest and smallest number in a tuple without using max() and min().
numbers = (25, 10, 45, 5, 30)

largest = numbers[0]
smallest = numbers[0]

for num in numbers:
    if num > largest:
        largest = num

    if num < smallest:
        smallest = num

print("Largest:", largest)
print("Smallest:", smallest)
#18.Calculate the average of elements stored in a tuple.
numbers = (10, 20, 30, 40, 50)

total = sum(numbers)
average = total / len(numbers)

print("Average:", average)
#19.Store 15 integers in a tuple and count:
#Even numbers
#Odd numbers
numbers = (10, 21, 32, 43, 54, 65, 76, 87, 98, 11, 22, 33, 44, 55, 66)

even = 0
odd = 0

for num in numbers:
    if num % 2 == 0:
        even = even + 1
    else:
        odd = odd + 1

print("Even numbers:", even)
print("Odd numbers:", odd)
#20.Accept a number from the user and determine whether it exists in the tuple.
numbers = (10, 20, 30, 40, 50)

num = int(input("Enter number: "))

if num in numbers:
    print("Number exists in the tuple.")
else:
    print("Number does not exist in the tuple.")
#21.Store student details in a tuple:
#Roll Number
#Name
#Department
#Marks
#Display all the details.
student = (101, "Aisha", "Computer Science", 88)

print("Roll Number:", student[0])
print("Name:", student[1])
print("Department:", student[2])
print("Marks:", student[3])
#22.Create tuples containing:
#Employee ID
#Name
#Salary
#Display all employee information.
employees = (
    (101, "Aisha", 45000),
    (102, "Rahul", 52000),
    (103, "Sneha", 60000)
)

for employee in employees:
    print("Employee ID:", employee[0])
    print("Name:", employee[1])
    print("Salary:", employee[2])
    print()
#23.Store item prices in a tuple and calculate:
#Total bill
#Average price
#Highest-priced item
#Lowest-priced item
prices = (100, 250, 150, 500, 300)

total = sum(prices)
average = total / len(prices)
highest = max(prices)
lowest = min(prices)

print("Total bill:", total)
print("Average price:", average)
print("Highest-priced item:", highest)
print("Lowest-priced item:", lowest)
#24.Store temperatures of seven days in a tuple and determine:
#Maximum temperature
#Minimum temperature
#Average temperature
temperature = (30, 32, 29, 35, 31, 33, 28)

maximum = max(temperature)
minimum = min(temperature)
average = sum(temperature) / len(temperature)

print("Maximum temperature:", maximum)
print("Minimum temperature:", minimum)
print("Average temperature:", average)
#25.Store runs scored in 10 matches and calculate:
#Total runs
#Highest score
#Lowest score
#Average score
runs = (45, 100, 75, 30, 120, 55, 80, 150, 25, 65)

total = sum(runs)
highest = max(runs)
lowest = min(runs)
average = total / len(runs)

print("Total runs:", total)
print("Highest score:", highest)
print("Lowest score:", lowest)
print("Average score:", average)
#26.Create two tuples and find the common elements between them.
tuple1 = (10, 20, 30, 40, 50)
tuple2 = (30, 40, 50, 60, 70)

common = ()

for num in tuple1:
    if num in tuple2:
        common = common + (num,)

print("Common elements:", common)
#27.Merge two tuples and remove duplicate elements.
tuple1 = (10, 20, 30, 40)
tuple2 = (30, 40, 50, 60)

result = ()

for num in tuple1 + tuple2:
    if num not in result:
        result = result + (num,)

print("Merged tuple:", result)
#28.Count the frequency of each element in a tuple.
numbers = (10, 20, 10, 30, 20, 10, 40)

checked = ()

for num in numbers:
    if num not in checked:
        print(num, ":", numbers.count(num))
        checked = checked + (num,)
#29.Convert a tuple into a sorted tuple in ascending and descending order.
numbers = (50, 20, 80, 10, 40, 30)

ascending = tuple(sorted(numbers))
descending = tuple(sorted(numbers, reverse=True))

print("Ascending order:", ascending)
print("Descending order:", descending)
#30.Create a tuple containing patient records:
#Patient ID
#Name
#Age
#Blood Group
#Perform the following operations:
#Display all records
#Search for a patient by ID
#Count the total number of patients
#Display patients with a specific blood group
patients = (
    (101, "Aisha", 20, "B+"),
    (102, "Rahul", 25, "O+"),
    (103, "Sneha", 22, "A+"),
    (104, "Aman", 30, "B+")
)

print("All patient records:")

for patient in patients:
    print("ID:", patient[0])
    print("Name:", patient[1])
    print("Age:", patient[2])
    print("Blood Group:", patient[3])
    print()

id = int(input("Enter patient ID to search: "))

found = False

for patient in patients:
    if patient[0] == id:
        print("Patient found:")
        print("ID:", patient[0])
        print("Name:", patient[1])
        print("Age:", patient[2])
        print("Blood Group:", patient[2])
        print("Blood Group:", patient[3])
        found = True

if found == False:
    print("Patient not found.")

print("Total number of patients:", len(patients))

blood = input("Enter blood group: ")

print("Patients with", blood, "blood group:")

for patient in patients:
    if patient[3] == blood:
        print(patient)