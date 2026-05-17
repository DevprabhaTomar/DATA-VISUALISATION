    
def find_gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

# Read input
x = int(input())
y = int(input())

# Print output
print(find_gcd(x, y))


#Input: 12 and 18 
# # Output: 6    
