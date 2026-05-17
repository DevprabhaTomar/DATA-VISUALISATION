# Program to calculate simple interest

# Take user input for principal, rate, and time
# Convert inputs to float to allow for decimal values
principal = float(input("Enter the principal amount: "))
rate = float(input("Enter the annual interest rate (%): "))
time = float(input("Enter the time in years: "))

# Calculate the simple interest using the formula
simple_interest = (principal * rate * time) / 100

# Print the result
print(f"The simple interest is: {simple_interest:.2f}")

#output
Enter the principal amount: 5
Enter the annual interest rate (%): 6
Enter the time in years: 7
The simple interest is: 2.10

