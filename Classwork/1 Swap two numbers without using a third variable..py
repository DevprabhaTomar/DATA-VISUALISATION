# Read two numbers
a = int(input())
b = int(input())

# Swap without third variable
a = a + b
b = a - b
a = a - b

# Print swapped numbers
print(a)
print(b)