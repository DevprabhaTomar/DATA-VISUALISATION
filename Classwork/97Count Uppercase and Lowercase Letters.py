def count_case(s):
    upper = 0
    lower = 0
    for ch in s:
        if ch.isupper():
            upper += 1
        elif ch.islower():
            lower += 1
    return upper, lower

# Read input string
s = input()

# Print output
upper, lower = count_case(s)
print("Uppercase:", upper)
print("Lowercase:", lower)

#Input: Hello World → 
# Output:

Uppercase: 2
Lowercase: 8