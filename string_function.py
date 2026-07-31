# 1)1.String Length
# Write a program to input a string and display its length without using the len() function.
string=input("enter a string:")
count=0
for i in string:
    count=count+1
print("length of strin is: ",count)

#2)2.Character Count
#Count the number of vowels, consonants, digits, spaces, and special characters in a given string.
string=input("Enter string: ")
vowels=consonants=digit=spaces=special_charcater=0
for ch in string:
    if ch in 'aeiou':
        vowels=vowels+1


    elif ch.isalpha():

        consonants += 1
    elif ch in 'bcdf':
        digits=digits+1
    elif ch in 'df':
        spaces=spaces+1
    elif ch in 'dfg':
        special_charcater=special_charcater+1
    else:
        special_charcater=0
print("vowels: ",vowels)
print("consonants: ",consonants)
print("digits: ",digit)
print("spaces: ",spaces)
print("special_charcater: ",special_charcater)
print("count: ",count)

#3)3.Reverse a String
#Reverse the given string without using built-in reverse functions.
string = input("Enter a string: ")

reverse = ""

for i in string:
    reverse = i + reverse

print("Reversed string =", reverse)


#4)4.alindrome Check
#Check whether the entered string is a palindrome.
tring = input("Enter a string: ")

reverse = ""

for ch in string:
    reverse = ch + reverse

if string == reverse:
    print("The string is a Palindrome")
else:
    print("The string is Not a Palindrome")
#

#5)Uppercase and Lowercase Count
#Count the number of uppercase and lowercase letters in a string.
string = input("Enter a string: ")

uppercase = 0
lowercase = 0

for ch in string:
    if ch.isupper():
        uppercase += 1
    elif ch.islower():
        lowercase += 1



print("Uppercase letters =", uppercase)
print("Lowercase letters =", lowercase)

#6.Replace Characters
#Replace all occurrences of a given character with another character.

string = input("Enter a string: ")
old = input("Enter the character to replace: ")
new = input("Enter the new character: ")

result = ""

for ch in string:
    if ch == old:
        result = result + new
    else:
        result = result + ch

print("Updated string =", result)

#7. Remove Spaces
#Remove all spaces from the input string.


string = input("Enter a string: ")

result = ""

for ch in string:
    if ch != " ":
        result = result + ch

print("String without spaces =", result)



#8.Frequency of a Character
#Find the number of times a specified character appears in a string.


string = input("Enter a string: ")
ch = input("Enter the character to find: ")

count = 0

for i in string:
    if i == ch:
        count += 1

print("Frequency of", ch, "=", count)

#9. First and Last Character
#Print the first and last character of a string.


string = input("Enter a string: ")

print("First character =", string[0])
print("Last character =", string[-1])

#10.ASCII Values
#Display each character of a string along with its ASCII value


string = input("Enter a string: ")

for ch in string:
    print(ch, "=", ord(ch))
#11.Word Count
#Count the total number of words in a sentence.

sentence = input("Enter a sentence: ")

count = 0
in_word = False

for ch in sentence:
    if ch != " ":
        if not in_word:
            count += 1
            in_word = True
    else:
        in_word = False

print("Total words =", count)

#12.Longest Word
#a.Find the longest word in a given sentence.


sentence = input("Enter a sentence: ")

words = sentence.split()

longest = words[0]

for word in words:
    if len(word) > len(longest):
        longest = word

print("Longest word =", longest)
print("Length =", len(longest))

#13.Shortest Word
#a.Find the shortest word in a sentence.


sentence = input("Enter a sentence: ")

words = sentence.split()

shortest = words[0]

for word in words:
    if len(word) < len(shortest):
        shortest = word

print("Shortest word =", shortest)
print("Length =", len(shortest))

#14.Title Case
#a.Convert the first letter of every word to uppercase.


sentence = input("Enter a sentence: ")

result = ""
new_word = True

for ch in sentence:
    if new_word and ch.isalpha():
        result = result + ch.upper()
        new_word = False
    else:
        result = result + ch
        if ch == " ":
            new_word = True

print("Title Case =", result)

#15.Duplicate Characters
#a.Print all duplicate characters in a string.



string = input("Enter a string: ")

printed = ""

for ch in string:
    if string.count(ch) > 1 and ch not in printed:
        print(ch)
        printed += ch

#16.Character Frequency
#a.Display the frequency of every character in a string.

string = input("Enter a string: ")

printed = ""

for ch in string:
    if ch not in printed:
        print(ch, "=", string.count(ch))
        printed += ch

#17.Anagram Check
#a.Check whether two strings are anagrams.


str1 = input("Enter first string: ")
str2 = input("Enter second string: ")

if sorted(str1.lower()) == sorted(str2.lower()):
    print("Strings are Anagrams")
else:
    print("Strings are Not Anagrams")

#18.Remove Duplicate Characters
#a.Remove duplicate characters while maintaining the original order.


string = input("Enter a string: ")

result = ""

for ch in string:
    if ch not in result:
        result += ch

print("String after removing duplicates =", result)

#19.Substring Search
#Check whether a given substring exists in the main string.
string = input("Enter the main string: ")
substring = input("Enter the substring: ")

if string.find(substring) != -1:
    print("Substring found")
else:
    print("Substring not found")
#20.Count Occurrences of a Word
#Count how many times a specific word appears in a sentence
# Program to count the occurrences of a word using inbuilt function

sentence = input("Enter a sentence: ")
word = input("Enter the word to search: ")

count = sentence.split().count(word)

print("Occurrences =", count)
#21.Password Validator
#Validate a password based on these conditions:
#oMinimum 8 characters
#oAt least one uppercase letter
#oOne lowercase letter
#oOne digit
#oOne special character
# Program to validate a password

password = input("Enter password: ")

if (len(password) >= 8 and
    any(ch.isupper() for ch in password) and
    any(ch.islower() for ch in password) and
    any(ch.isdigit() for ch in password) and
    any(not ch.isalnum() for ch in password)):
    print("Valid Password")
else:
    print("Invalid Password")

#22.Run-Length Encoding
#Compress a string by counting consecutive repeated characters.
#Example:
#	Input: aaabbccccd
#	Output: a3b2c4d1
# Run-Length Encoding

s = input("Enter a string: ")

count = 1

for i in range(len(s)):
    if i < len(s) - 1 and s[i] == s[i + 1]:
        count += 1
    else:
        print(s[i] + str(count), end="")
        count = 1
#23.String Compression
#Compress repeated characters and return the original string if compression does not reduce the length.


string = input("Enter a string: ")

compressed = ""
count = 1

for i in range(len(string)):
    if i < len(string) - 1 and string[i] == string[i + 1]:
        count += 1
    else:
        compressed += string[i] + str(count)
        count = 1

if len(compressed) < len(string):
    print("Compressed String =", compressed)
else:
    print("Original String =", string)
#24.Most Frequent Character
#Find the character with the highest frequency.

string = input("Enter a string: ")

max_char = ""
max_count = 0

for ch in string:
    if string.count(ch) > max_count:
        max_count = string.count(ch)
        max_char = ch

print("Most frequent character =", max_char)
print("Frequency =", max_count)

#25.Second Most Frequent Character
#Find the second most frequently occurring character.
# Program to find the second most frequent character

string = input("Enter a string: ")

first_char = ""
second_char = ""
first_count = 0
second_count = 0

checked = ""

for ch in string:
    if ch not in checked:
        count = string.count(ch)

        if count > first_count:
            second_count = first_count
            second_char = first_char

            first_count = count
            first_char = ch

        elif count > second_count:
            second_count = count
            second_char = ch

        checked += ch

print("Second most frequent character =", second_char)
print("Frequency =", second_count)
#26.Caesar Cipher
#Encrypt and decrypt a message using the Caesar Cipher algorithm.


message = input("Enter the message: ")
shift = int(input("Enter the shift value: "))


encrypted = ""
for ch in message:
    if ch.isalpha():
        if ch.isupper():
            encrypted += chr((ord(ch) - 65 + shift) % 26 + 65)
        else:
            encrypted += chr((ord(ch) - 97 + shift) % 26 + 97)
    else:
        encrypted += ch

print("Encrypted Message =", encrypted)


decrypted = ""
for ch in encrypted:
    if ch.isalpha():
        if ch.isupper():
            decrypted += chr((ord(ch) - 65 - shift) % 26 + 65)
        else:
            decrypted += chr((ord(ch) - 97 - shift) % 26 + 97)
    else:
        decrypted += ch

print("Decrypted Message =", decrypted)

#27.Email Validator
#Validate whether a given email address follows a valid format.


email = input("Enter an email address: ")

if ("@" in email and
    "." in email and
    email.index("@") < email.rindex(".") and
    email.count("@") == 1):
    print("Valid Email")
else:
    print("Invalid Email")
#28.Word Frequency Dictionary
#Count the frequency of every word in a paragraph


paragraph = input("Enter a paragraph: ")

words = paragraph.split()
frequency = {}

for word in words:
    frequency[word] = words.count(word)

print("Word Frequencies:")
for word in frequency:
    print(word, "=", frequency[word])
#29.Sentence Reversal
#Reverse the order of words in a sentence without changing the words themselves.
#Example:
#Input: Python is easy
#Output: easy is Python
# Program to reverse the order of words in a sentence

sentence = input("Enter a sentence: ")

words = sentence.split()
words.reverse()

result = " ".join(words)

print("Reversed sentence =", result)
#30.String Rotation
#Check whether one string is a rotation of another.
#Example:
#ABCD
#CDAB
#Output: Yes
# Program to check whether one string is a rotation of another

str1 = input("Enter first string: ")
str2 = input("Enter second string: ")

if len(str1) == len(str2) and str2 in (str1 + str1):
    print("Yes, it is a rotation.")
else:
    print("No, it is not a rotation.")