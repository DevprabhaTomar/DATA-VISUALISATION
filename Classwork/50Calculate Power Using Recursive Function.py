def power(x, n):
    if n == 0:
        return 1
    else:
        return x * power(x, n-1)

# Read input
base = int(input())
exp = int(input())

# Print output
print(power(base, exp))

#Input: 2 3
#  #Output: 8