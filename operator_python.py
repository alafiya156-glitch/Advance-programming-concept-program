#Arithmatic operator
print("arithmatic operator")
a=10
b=20
print("addition is:",a+b)
print("substarction is:",a-b)
print("multiplication is:",a*b)
print("division is:",a/b)
print("modulas is:",a%b)
print("exponantion is:",a**2)
print("____Assignment operator___")
print("==:",a==5)
c=10
print("=:",c)
a+=11
print("+=:",a)
a-=10
print("-=:",a)
a*=10
print("*=:",a)
a/=10
print("/=:",a)
a%=10
print("%=:",a)
print("____Comparison operators___")
x = 10
y = 12

print("== (Equal to)             :", x == y)
print("!= (Not equal to)         :", x != y)
print(">  (Greater than)         :", x > y)
print("<  (Less than)            :", x < y)
print(">= (Greater than or equal):", x >= y)
print("<= (Less than or equal)   :", x <= y)

print("____Logical operators___")
has_ticket = True
has_id = False

print("and (Both must be True)     :", has_ticket and has_id)
print("or  (At least one is True)  :", has_ticket or has_id)
print("not (Inverts the outcome)   :", not has_ticket)

print("____Identity operators___")
list1 = [1, 2, 3]
list2 = [1, 2, 3]
list3 = list1

print("is     (Same memory address?)    :", list1 is list3)
print("is     (Same values but separate):", list1 is list2)
print("is not (Different object?)       :", list1 is not list2)

print("____Membership operators___")
message = "Hello World"
numbers = [10, 20, 30, 40]

print("in     (Item exists in list?)   :", 20 in numbers)
print("in     (Letter exists in text?) :", "z" in message)
print("not in (Item does missing?)     :", 50 not in numbers)