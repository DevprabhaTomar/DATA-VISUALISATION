# Read four numbers
a = float(input())
b = float(input())
c = float(input())
d = float(input())

# Find greatest
if a >= b and a >= c and a >= d:
    print(a)
elif b >= a and b >= c and b >= d:
    print(b)
elif c >= a and c >= b and c >= d:
    print(c)
else:
    print(d)

    #input
    56
    30
    10
    20
    #output
    56