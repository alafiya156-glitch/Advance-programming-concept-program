# Question 1: Extract all digits from a given string
import re
text = "My roll number is 123 and my age is 20"
digits = re.findall(r'\d', text)
print("Digits:", digits)

# Question 2: Display all words beginning with A or a
import re
sentence = input("Enter a sentence: ")
words = re.findall(r'\b[Aa]\w*', sentence)
print("Words beginning with A or a:", words)

# Question 3: Count occurrences of vowels using regular expressions
import re
text = input("Enter a string: ")
vowels = re.findall(r'[aeiouAEIOU]', text)
print("Total vowels:", len(vowels))

# Question 4: Extract all uppercase letters from a string
import re
text = input("Enter a string: ")
uppercase = re.findall(r'[A-Z]', text)
print("Uppercase letters:", uppercase)

# Question 5: Identify spaces, tabs, and newline characters
import re
text = "Hello World\tPython\nProgramming"
spaces = re.findall(r' ', text)
tabs = re.findall(r'\t', text)
newlines = re.findall(r'\n', text)
print("Spaces:", len(spaces))
print("Tabs:", len(tabs))
print("Newlines:", len(newlines))

# Question 6: Replace multiple spaces with a single space
import re
text = "Python    is     very   easy"
result = re.sub(r' +', ' ', text)
print("Original text:", text)
print("Updated text:", result)

# Question 7: Display words containing exactly five characters
import re
sentence = input("Enter a sentence: ")
words = re.findall(r'\b[A-Za-z]{5}\b', sentence)
print("Five-character words:", words)

# Question 8: Identify all words ending with the letter s
import re
sentence = input("Enter a sentence: ")
words = re.findall(r'\b\w*s\b', sentence, re.IGNORECASE)
print("Words ending with s:", words)

# Question 9: Remove special characters while retaining letters, digits, and spaces
import re
text = input("Enter a string: ")
result = re.sub(r'[^A-Za-z0-9 ]', '', text)
print("Result:", result)

# Question 10: Count the number of words using regular expressions
import re
sentence = input("Enter a sentence: ")
words = re.findall(r'\b\w+\b', sentence)
print("Total words:", len(words))

# Question 11: Validate a 10-digit Indian mobile number
import re
mobile = input("Enter mobile number: ")
if re.fullmatch(r'[6-9]\d{9}', mobile):
    print("Valid mobile number")
else:
    print("Invalid mobile number")

# Question 12: Validate an email address
import re
email = input("Enter email address: ")
pattern = r'[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}'
if re.fullmatch(pattern, email):
    print("Valid email address")
else:
    print("Invalid email address")

# Question 13: Extract dates in DD-MM-YYYY format
import re
text = "Dates are 15-08-2026 and 26-10-2026"
dates = re.findall(r'\b\d{2}-\d{2}-\d{4}\b', text)
print("Dates:", dates)

# Question 14: Extract HTTP and HTTPS web addresses
import re
text = "Visit https://google.com and http://example.com"
urls = re.findall(r'https?://[^\s]+', text)
print("Web addresses:", urls)

# Question 15: Extract all hashtags from a social media post
import re
post = input("Enter a social media post: ")
hashtags = re.findall(r'(?<!\w)#[A-Za-z0-9_]+', post)
print("Hashtags:", hashtags)

# Question 16: Check password requirements using regular expressions

import re
password = input("Enter password: ")
pattern = r'(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[^A-Za-z0-9]).{8,}'
if re.fullmatch(pattern, password):
    print("Strong password")
else:
    print("Weak password")

# Question 17: Identify consecutive repeated words, ignoring case

import re
sentence = input("Enter a sentence: ")
pattern = r'\b(\w+)\s+\1\b'
matches = re.findall(pattern, sentence, re.IGNORECASE)
print("Repeated words:", matches)

# Question 18: Extract six-digit Indian PIN codes
import re
text = "My PIN codes are 422001 and 110001"
pins = re.findall(r'(?<!\d)[1-9]\d{5}(?!\d)', text)
print("PIN codes:", pins)

# Question 19: Validate an Indian vehicle registration number
import re
number = input("Enter vehicle number: ").upper()
pattern = r'[A-Z]{2}\d{2}[A-Z]{1,3}\d{4}'
if re.fullmatch(pattern, number):
    print("Valid vehicle registration format")
else:
    print("Invalid vehicle registration format")

# Question 20: Extract file extensions from filenames
import re
text = "Files: report.pdf, photo.jpg, data.csv, program.py"
extensions = re.findall(r'\.([A-Za-z0-9]+)\b', text)
print("File extensions:", extensions)

# Question 21: Clean text by removing HTML tags, extra whitespace, and punctuation
import re
text = "<p>Hello!!!   World.</p>  <b>Python, is great!</b>"
# Remove HTML tags
text = re.sub(r'<[^>]+>', '', text)
# Remove punctuation
text = re.sub(r'[^\w\s]', '', text)
# Replace extra whitespace with a single space
text = re.sub(r'\s+', ' ', text).strip()
print("Cleaned text:", text)


# Question 22: Extract invoice numbers, dates, and monetary amounts
import re
text = """
Invoice No: INV-1025
Date: 26-10-2026
Amount: Rs. 1500.50
"""
invoice = re.findall(r'INV-\d+', text)
dates = re.findall(r'\b\d{2}-\d{2}-\d{4}\b', text)
amounts = re.findall(r'Rs\.?\s*\d+(?:\.\d{2})?', text)
print("Invoice numbers:", invoice)
print("Dates:", dates)
print("Amounts:", amounts)

# Question 23: Identify single-line comments in Python source code
import re
code = """
# This is a comment
x = 10
print(x)  # Display value
# Another comment
"""
comments = re.findall(r'^\s*#.*$', code, re.MULTILINE)
print("Single-line comments:")
for comment in comments:
    print(comment.strip())

# Question 23: Identify single-line comments in Python source code
import re
code = """
# This is a comment
x = 10
print(x)  # Display value
# Another comment
"""
comments = re.findall(r'^\s*#.*$', code, re.MULTILINE)
print("Single-line comments:")
for comment in comments:
    print(comment.strip())

# Question 24: Validate product codes in ABC-1234-XY format
import re
code = input("Enter product code: ")
pattern = r'[A-Z]{3}-\d{4}-[A-Z]{2}'
if re.fullmatch(pattern, code):
    print("Valid product code")
else:
    print("Invalid product code")

# Question 24: Validate product codes in ABC-1234-XY format
import re
code = input("Enter product code: ")
pattern = r'[A-Z]{3}-\d{4}-[A-Z]{2}'
if re.fullmatch(pattern, code):
    print("Valid product code")
else:
    print("Invalid product code")

# Question 25: Extract student details using regular expressions
import re
text = """
Name: Rahul, Roll: 101, Marks: 85
Name: Priya, Roll: 102, Marks: 92
Name: Amit, Roll: 103, Marks: 78
"""
pattern = r'Name:\s*([A-Za-z ]+),\s*Roll:\s*(\d+),\s*Marks:\s*(\d+)'
students = re.findall(pattern, text)
for name, roll, marks in students:
    print("Name:", name.strip())
    print("Roll Number:", roll)
    print("Marks:", marks)
    print()

# Question 26: Extract DOI identifiers, publication years, emails, and URLs
import re
text = """
Research Paper (2024)
DOI: 10.1234/abcd.5678
Email: author@example.com
URL: https://example.com/paper
"""
doi = re.findall(r'\b10\.\d{4,9}/[-._;()/:A-Z0-9]+\b', text, re.IGNORECASE)
years = re.findall(r'\b(?:19|20)\d{2}\b', text)
emails = re.findall(
    r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b',
    text
)
urls = re.findall(r'https?://[^\s]+', text)
print("DOI:", doi)
print("Publication years:", years)
print("Emails:", emails)
print("URLs:", urls)