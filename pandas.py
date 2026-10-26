#1.Student Marks Using Pandas DataFrame
import pandas as pd
data = {
    'Student_ID': [101, 102, 103, 104, 105],
    'Student_Name': ['Amit', 'Priya', 'Rahul', 'Sneha', 'Neha'],
    'Python': [85, 70, 90, 78, 65],
    'DBMS': [80, 75, 88, 82, 70],
    'Mathematics': [90, 80, 92, 85, 75]
}
df = pd.DataFrame(data)
df['Total'] = df[['Python', 'DBMS', 'Mathematics']].sum(axis=1)
df['Average'] = df[['Python', 'DBMS', 'Mathematics']].mean(axis=1)
print("Student DataFrame:")
print(df)
print("\nStudents with average above 75:")
print(df[df['Average'] > 75])

#2.Employee Salary and Experience
import pandas as pd
data = {
    'Employee_ID': [1, 2, 3, 4, 5],
    'Employee_Name': ['Amit', 'Priya', 'Rahul', 'Sneha', 'Neha'],
    'Department': ['CSE', 'IT', 'HR', 'CSE', 'Finance'],
    'Salary': [45000, 60000, 55000, 75000, 40000],
    'Experience': [2, 5, 4, 8, 3]
}
df = pd.DataFrame(data)
print("Employees with salary greater than 50000:")
print(df[df['Salary'] > 50000])
print("\nAverage Salary:")
print(df['Salary'].mean())
print("\nHighest Salary:")
print(df['Salary'].max())
print("\nEmployee with highest experience:")
print(df.loc[df['Experience'].idxmax()])

#3.Product Sales Calculation
import pandas as pd
data = {
    'Product_ID': [101, 102, 103, 104, 105],
    'Product_Name': ['Laptop', 'Mobile', 'Keyboard', 'Monitor', 'Mouse'],
    'Category': ['Electronics', 'Electronics', 'Accessories', 'Electronics', 'Accessories'],
    'Price': [50000, 20000, 1500, 12000, 500],
    'Quantity': [5, 10, 20, 8, 30]
}

df = pd.DataFrame(data)
df['Total_Amount'] = df['Price'] * df['Quantity']
print("Product DataFrame:")
print(df)
print("\nProduct with highest total sales:")
print(df.loc[df['Total_Amount'].idxmax()])

#4.Patient Medical Charges
import pandas as pd
data = {
    'Patient_ID': [1, 2, 3, 4, 5],
    'Patient_Name': ['Amit', 'Priya', 'Rahul', 'Sneha', 'Neha'],
    'Age': [65, 45, 72, 30, 61],
    'Disease': ['Diabetes', 'Fever', 'Heart Disease', 'Asthma', 'Diabetes'],
    'Medical_Charges': [60000, 15000, 85000, 20000, 55000]
}

df = pd.DataFrame(data)
print("Patients above 60 years:")
print(df[df['Age'] > 60])
print("\nAverage Medical Charge:")
print(df['Medical_Charges'].mean())
print("\nMaximum Medical Charge:")
print(df['Medical_Charges'].max())
print("\nPatients with charges greater than 50000:")
print(df[df['Medical_Charges'] > 50000])

#5.Order Amount and Discount Calculation
import pandas as pd
data = {
    'Order_ID': [101, 102, 103, 104, 105],
    'Customer': ['Amit', 'Priya', 'Rahul', 'Sneha', 'Neha'],
    'Product': ['Laptop', 'Mobile', 'Tablet', 'Monitor', 'Printer'],
    'Quantity': [2, 3, 1, 2, 4],
    'Price': [40000, 15000, 25000, 10000, 5000],
    'Discount': [2000, 1000, 1500, 500, 1000]
}

df = pd.DataFrame(data)
df['Final_Amount'] = df['Quantity'] * df['Price'] - df['Discount']
print("All Orders:")
print(df)
print("\nOrders above 5000:")
print(df[df['Final_Amount'] > 5000])
print("\nHighest-value Order:")
print(df.loc[df['Final_Amount'].idxmax()])
print("\nAverage Order Value:")
print(df['Final_Amount'].mean())

#6.Student Attendance Percentage
import pandas as pd
data = {
    'Student_ID': [101, 102, 103, 104, 105],
    'Name': ['Amit', 'Priya', 'Rahul', 'Sneha', 'Neha'],
    'Department': ['CSE', 'IT', 'CSE', 'ENTC', 'IT'],
    'Total_Classes': [100, 100, 100, 100, 100],
    'Classes_Attended': [80, 65, 90, 70, 95]
}

df = pd.DataFrame(data)
df['Attendance_Percentage'] = (
    df['Classes_Attended'] / df['Total_Classes']
) * 100

print("Student Attendance:")
print(df)
print("\nStudents with attendance below 75%:")
print(df[df['Attendance_Percentage'] < 75])

#7.Retail Shop Sales Analysis
import pandas as pd
data = {
    'Product_ID': [101, 102, 103, 104, 105],
    'Product_Name': ['Laptop', 'Mobile', 'Keyboard', 'Monitor', 'Printer'],
    'Category': ['Electronics', 'Electronics', 'Accessories', 'Electronics', 'Office'],
    'Price': [50000, 20000, 1000, 15000, 8000],
    'Quantity': [2, 5, 10, 3, 4]
}

df = pd.DataFrame(data)
df['Total_Sales'] = df['Price'] * df['Quantity']

print("Product DataFrame:")
print(df)
print("\nProducts with sales greater than 10000:")
print(df[df['Total_Sales'] > 10000])
print("\nProduct with maximum sales:")
print(df.loc[df['Total_Sales'].idxmax()])
print("\nAverage Sales:")
print(df['Total_Sales'].mean())

#8.Employee Salaries Using Pandas Series
import pandas as pd

marks = {
    'Amit': 85,
    'Priya': 92,
    'Rahul': 68,
    'Sneha': 78,
    'Neha': 95
}

s = pd.Series(marks)

print("Student Marks:")
print(s)
print("\nMarks of Priya:")
print(s['Priya'])
print("\nMaximum Marks:")
print(s.max())
print("\nMinimum Marks:")
print(s.min())
print("\nAverage Marks:")
print(s.mean())
print("\nStudents scoring more than 75:")
print(s[s > 75])

#9.Employee Salaries Using Pandas Series
import pandas as pd

salaries = {
    'Amit': 45000,
    'Priya': 65000,
    'Rahul': 55000,
    'Sneha': 75000,
    'Neha': 40000
}

s = pd.Series(salaries)

print("Employee Salaries:")
print(s)
print("\nHighest Salary:")
print(s.max())
print("\nLowest Salary:")
print(s.min())
print("\nAverage Salary:")
print(s.mean())
print("\nEmployees earning more than 50000:")
print(s[s > 50000])

#10.Product Prices Using Pandas Series
import pandas as pd
prices = {
    'Laptop': 50000,
    'Mobile': 20000,
    'Keyboard': 1500,
    'Monitor': 12000,
    'Mouse': 500
}

s = pd.Series(prices)

print("Products and Prices:")
print(s)

s = s * 1.10

print("\nPrices after 10% increase:")
print(s)
print("\nMost Expensive Product:")
print(s.idxmax())
print("Price:", s.max())
print("\nProducts costing more than 1000:")
print(s[s > 1000])

#11.Patient Ages Using Pandas Series
import pandas as pd

ages = {
    101: 45,
    102: 67,
    103: 72,
    104: 35,
    105: 61
}

s = pd.Series(ages)

print("Patient Ages:")
print(s)
print("\nAverage Age:")
print(s.mean())
print("\nOldest Patient:")
print(s.idxmax(), "Age:", s.max())
print("\nYoungest Patient:")
print(s.idxmin(), "Age:", s.min())
print("\nPatients above 60 years:")
print(s[s > 60])

#12.Student Attendance Using Pandas Series
import pandas as pd

attendance = {
    'Amit': 85,
    'Priya': 95,
    'Rahul': 68,
    'Sneha': 92,
    'Neha': 72
}

s = pd.Series(attendance)

print("Student Attendance:")
print(s)
print("\nAverage Attendance:")
print(s.mean())
print("\nStudents with attendance below 75%:")
print(s[s < 75])
print("\nStudents with attendance above 90%:")
print(s[s > 90])
print("\nHighest Attendance:")
print(s.idxmax(), s.max())

#13.Student Data Analysis Using students.csv
import pandas as pd

df = pd.read_csv('students.csv')

print("First 5 Records:")
print(df.head())
print("\nLast 5 Records:")
print(df.tail())

df['Total'] = df[['Python', 'DBMS', 'Maths']].sum(axis=1)
df['Average'] = df[['Python', 'DBMS', 'Maths']].mean(axis=1)

print("\nTotal and Average Marks:")
print(df)
print("\nStudents with average marks greater than 75:")
print(df[df['Average'] > 75])
print("\nStudent with Highest Average:")
print(df.loc[df['Average'].idxmax()])
print("\nAverage Marks for Each Subject:")
print(df[['Python', 'DBMS', 'Maths']].mean())

#14.Employee Data Analysis Using employees.csv
import pandas as pd

df = pd.read_csv('employees.csv')

print("Employees from CSE Department:")
print(df[df['Department'] == 'CSE'])
print("\nAverage Salary:")
print(df['Salary'].mean())
print("\nHighest Salary:")
print(df['Salary'].max())
print("\nLowest Salary:")
print(df['Salary'].min())
print("\nEmployees with salary greater than 50000:")
print(df[df['Salary'] > 50000])
print("\nDepartment-wise Average Salary:")
print(df.groupby('Department')['Salary'].mean())

#15.Patient Data Analysis Using patients.csv
import pandas as pd
df = pd.read_csv('patients.csv')
print("Patients above 60 years:")
print(df[df['Age'] > 60])
print("\nAverage Medical Expense:")
print(df['Medical_Expense'].mean())
print("\nPatient with Highest Medical Expense:")
print(df.loc[df['Medical_Expense'].idxmax()])
print("\nNumber of Patients for Each Disease:")
print(df['Disease'].value_counts())
print("\nPatients with medical expense greater than 50000:")
print(df[df['Medical_Expense'] > 50000])

#16.Weather Data Analysis Using weather.csv
import pandas as pd
df = pd.read_csv('weather.csv')

print("Maximum Temperature:")
print(df['Temperature'].max())
print("\nMinimum Temperature:")
print(df['Temperature'].min())
print("\nAverage Temperature:")
print(df['Temperature'].mean())
print("\nRecords with temperature above 35°C:")
print(df[df['Temperature'] > 35])
print("\nCity-wise Average Temperature:")
print(df.groupby('City')['Temperature'].mean())
