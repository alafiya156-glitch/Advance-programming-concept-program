#Write a PYTHON program that reads a value of n and check the number is zero or non zero value.
n = int(input("Enter the value : "))
if (n == 0):
    print("Zero")
else:
    print("Non Zero")
    
#Write a PYTHON program to find a largest of two numbers.
n1 = int(input("Enter the 1st number : "))
n2 = int(input("Enter the 2nd number : "))
if (n1<n2):
    print("largest number :",n2)
else :
    print("Largest number :",n1)
    
#Write a PYTHON program that reads the number and check the no is positive or negative0

n3 = int(input("Enter the number : "))
if(n3>0):
    print("number is positive")
else:
    print("number is negative")
    
#Write a PYTHON program to check entered character is vowel or consonant.
s = input("Enter the charater : ")
if(s=="A" or s=="a" or s=="E" or s=="e" or s=="I" or s=="i" or s=="O" or s=="o" or s=="U" or s=="u"):
    print("Vowel")
else:
    print("Consonant")
    
#Write a PYTHON program to evaluate the student performance
     #If % is >=80 then  Very Good performance
      #If % is >=70 then Good performance
      #If % is >=60 then average performance
      #else Poor performance.

m = int(input("enter the Percentage : "))
if (m >= 80):
      print("Very Good Perfornmance") 
elif (m >=70):
      print(" Good Perfornmance")
elif (m >=60):
      print(" Avarage Perfornmance")

else:
      print("Poor Perforance")
      
      
#Write a PYTHON program to find largest of three numbers.
n1 = int(input("enter the 1st number : "))
n2 = int(input("enter the 2nd number : "))
n3 = int(input("enter the 3rd number : "))
if (n1>n2 and n1>n3):
    print(n1," is largest")
elif(n2>n1 and n2>n3):
    print(n2," is largest")
else:
    print(n3," is largest")


#Write a PYTHON program to find smallest of three numbers
n1 = int(input("enter the 1st number : "))
n2 = int(input("enter the 2nd number : "))
n3 = int(input("enter the 3rd number : "))
if (n1<n2 and n1<n3):
    print(n1," is smallest")
elif(n2<n1 and n2<n3):
    print(n2," is smallest")
else:
    print(n3," is lsmallest")


#Write a PYTHON program to check weather number is even or odd.
n1 = int(input("enter the 1st number : "))
if (n1%2==0):
    print(n1," is Even")
else:
    print(n1," is Odd")
    
#Write a PYTHON program to check a year for leap year.
year = int(input("Enter a year: "))
if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
    print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.")
    

marital_status = input("Is the driver married? (yes/no): ")
gender = input("Enter driver's gender (male/female): ")
age = int(input("Enter driver's age: "))

if marital_status == "yes":
    print("The driver is insured.")
elif marital_status == "no" and gender == "male" and age > 30:
    print("The driver is insured.")
elif marital_status == "no" and gender == "female" and age > 25:
    print("The driver is insured.")
else:
    print("The driver is not insured.")
    
