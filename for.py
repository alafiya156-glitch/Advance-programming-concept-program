#1) Write a PYTHON program to print the natural numbers up to n

n=int(input("enter value of N: "))
for i in range(1,n+1):
    print(i)
# 2)Program to print even numbers up to n

n = int(input("Enter the value of n: "))

for i in range(2, n + 1, 2):
    print(i)


# 3)Program to print odd numbers up to n

n = int(input("Enter the value of n: "))

for i in range(1, n + 1, 2):
    print(i)

# 4)Program to print the series 1, 2, 4, 8, 16, ... up to 2^n

n = int(input("Enter the value of n: "))

for i in range(n + 1):
    print(2 ** i, end=" ")

# 5)Program to find the sum of the series:
# 1 + 1/1! + 1/2! + 1/3! + ... + 1/n!

n = int(input("Enter the value of n: "))

fact = 1
sum = 1

for i in range(1, n + 1):
    fact = fact * i
    sum = sum + (1 / fact)

print("Sum of the series =", sum)

# 6)Program to compute cos(x) using the cosine series
# cos(x) = 1 - x^2/2! + x^4/4! - x^6/6! + ... up to n terms

x = float(input("Enter the value of x (in radians): "))
n = int(input("Enter the number of terms: "))

sum = 1
fact = 1
sign = -1

for i in range(2, 2 * n + 1, 2):
    fact = 1
    for j in range(1, i + 1):
        fact = fact * j
    sum = sum + sign * (x ** i) / fact
    sign = sign * -1

print("cos(", x, ") =", sum)

# 7)Program to check whether the square root of a number is prime or not

import math

n = int(input("Enter a number: "))
r = int(math.sqrt(n))

if r * r != n:
    print("Square root is not a whole number.")
else:
    prime = True
    if r < 2:
        prime = False
    else:
        for i in range(2, int(math.sqrt(r)) + 1):
            if r % i == 0:
                prime = False
                break

    if prime:
        print("Square root", r, "is Prime")
    else:
        print("Square root", r, "is Not Prime")

# 8)Program to print the pattern

for i in range(3):
    print("A B C")

#9) Program to print the pattern:

n = int(input("Enter the value of n: "))

for i in range(1, n + 1):
    for j in range(i):
        print(chr(65 + j), end=" ")
    print()

# 10)Program to print the pattern:

n = int(input("Enter the value of n: "))

for i in range(n, 0, -1):
    for j in range(i):
        print(chr(65 + j), end=" ")
    print()

# 11) Program to print the pattern:
n = int(input("Enter the value of n: "))

for i in range(1, n + 1):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()

#12) Program to print the pattern:
n = int(input("Enter the value of n: "))

for i in range(1, n + 1):
    for j in range(i):
        print(i, end=" ")
    print()
