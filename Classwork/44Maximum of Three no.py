#Maximum of Three Numbers Using Function
def find_max(a, b, c):
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c

# Read input
a = int(input())
b = int(input())
c = int(input())

# Print output
print(find_max(a, b, c))

#input
5
12
6

#output
12