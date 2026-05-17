def sum_of_digits(n):
    total = 0
    n = abs(n)   # handle negative numbers
    while n > 0:
        total += n % 10
        n //= 10
    return total

# Read input
num = int(input())

# Print output
print(sum_of_digits(num))

#input
67
#output
 13