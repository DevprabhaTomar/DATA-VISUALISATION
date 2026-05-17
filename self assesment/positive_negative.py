# The following code checks if a number is positive, negative, or 0
# Taking user input
number = float(input("Enter a number: "))

# Condition checking
if number > 0:
    print(number, "is a positive number.")
elif number < 0:
    print(number, "is a negative number.")
else:
    print(number, "is zero.")
