# Read three sides
a = float(input())
b = float(input())
c = float(input())

# Check triangle validity first
if a + b > c and a + c > b and b + c > a:
    
    if a == b == c:
        print("Equilateral")
    elif a == b or b == c or a == c:
        print("Isosceles")
    else:
        print("Scalene")

else:
    print("Invalid Triangle")


#input
5
5
5
#output
Equilateral