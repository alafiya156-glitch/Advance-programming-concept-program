# Python program to print natural numbers up to n using a while loop. Natural numbers
n = int(input("Enter the value of n: "))
i = 1
while i <= n:
    print(i, end=" ")
    i += 1  
    
    
#Python program to print even and odd numbers separately up to n using a while
n = int(input("\n Enter the value of n: "))
print("Even numbers:")
i = 1
while i <= n:
    if i % 2 == 0:
        print(i, end=" ")
    i += 1

print("\n") 
print("Odd numbers:")
i = 1
while i <= n:
    if i % 2 != 0:
        print(i, end=" ")
    i += 1
    
    
    
#Python program to calculate and print the sum of natural numbers up to \(n\) using a while loop
n = int(input("\n Enter the value of n: "))

i = 1
sum = 0
while i <= n:
    sum += i  
    i += 1         
print(f"The sum of natural numbers up to {n} is: {sum}")



#Python program to calculate and print the sum of odd numbers up to n using a while loop
n = int(input("\n Enter the value of n: "))
i = 1
odd_sum = 0
while i <= n:
    odd_sum += i  
    i += 2        
print(f"The sum of odd numbers up to {n} is: {odd_sum}")


#Python program to calculate and print the sum of even numbers up to n using a while loop
n = int(input("\n Enter the value of n: "))
i = 2
even_sum = 0
while i <= n:
    even_sum += i  
    i += 2       
print(f"The sum of even numbers up to {n} is: {even_sum}")


#Python program to print natural numbers up to n in reverse order using a while loop
n = int(input("\n Enter the value of n: "))
i = n
while i >= 1:
    print(i, end=" ")
    i -= 1  


#Python program to print the Fibonacci series up to a maximum value of n using a while loop
n = int(input("\n Enter the maximum limit n: "))
a = 0
b = 1
print("Fibonacci series:", end=" ")
while a <= n:
    print(a, end=" ")
    next = a + b
    a = b
    b = next
    
    
# Python program to check whether a given number is prime or not using a while
num = int(input("Enter a number: "))
i = 2
while i * i <= num and num % i != 0:
    i += 1
if num > 1 and i * i > num:
    print(f"{num} is prime.")
else:
    print(f"{num} is not prime.")



#Python program to check if an entered number is a palindrome using a while loop
num = int(input("Enter a number: "))
temp = num
reverse_num = 0
while temp > 0:
    digit = temp % 10                 
    reverse_num = reverse_num * 10 + digit  
    temp //= 10                        
if num == reverse_num:
    print(f"{num} is a palindrome.")
else:
    print(f"{num} is not a palindrome.")
  


#Python program to print a multiplication table using a while loop
num = int(input("Enter the number for the table: "))
i = 1

print(f"\nMultiplication Table of {num}:")
while i <= 10:
    print(f"{num} x {i} = {num * i}")
    i += 1  



# Python program to find and print the largest and smallest numbers from a set of n numbers using a while loop
n = int(input("Enter how many numbers: "))

num = int(input("Enter number: "))
largest = num
smallest = num

i = 1

while i < n:
    num = int(input("Enter number: "))

    if num > largest:
        largest = num

    if num < smallest:
        smallest = num

    i = i + 1

print("Largest number =", largest)
print("Smallest number =", smallest)
