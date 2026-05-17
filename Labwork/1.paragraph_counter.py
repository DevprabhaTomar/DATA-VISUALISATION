# File Name: paragraph_counter.py

# Python program to count uppercase, lowercase, digits,
# spaces, and special characters in a paragraph

paragraph = input("Enter a paragraph: ")

uppercase = 0
lowercase = 0
digits = 0
spaces = 0
special = 0

for ch in paragraph:
    if ch.isupper():
        uppercase += 1
    elif ch.islower():
        lowercase += 1
    elif ch.isdigit():
        digits += 1
    elif ch.isspace():
        spaces += 1
    else:
        special += 1

print("Uppercase letters:", uppercase)
print("Lowercase letters:", lowercase)
print("Digits:", digits)
print("Spaces:", spaces)
print("Special characters:", special)