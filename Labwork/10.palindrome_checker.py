# File Name: palindrome_checker.py

import string

text = input("Enter a string: ")

# Remove spaces and punctuation
cleaned = ""

for ch in text:
    if ch.isalnum():
        cleaned += ch.lower()

# Check palindrome
if cleaned == cleaned[::-1]:
    print("The string is a palindrome")
else:
    print("The string is not a palindrome")