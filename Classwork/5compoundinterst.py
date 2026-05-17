# Read Principal, Rate, and Time
p = float(input())
r = float(input())
t = float(input())

# Calculate Compound Interest
amount = p * (1 + r/100) ** t
ci = amount - p

# Print result
print(ci)