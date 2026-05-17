# Read three numbers in one line
a, b, c = map(float, input().split())

# Find largest
if a >= b and a >= c:
    print(a)
elif b >= a and b >= c:
    print(b)
else:
    print(c)