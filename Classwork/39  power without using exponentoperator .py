# Read base and exponent
base = int(input())
exp = int(input())

result = 1

# Calculate power using loop
for i in range(exp):
    result = result * base

print(result)

#input
5
6

#output
15625