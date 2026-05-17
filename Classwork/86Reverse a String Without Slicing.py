def reverse_string(s):
    rev = ""
    for i in range(len(s)-1, -1, -1):
        rev += s[i]
    return rev

# Read input string
s = input()

# Print reversed string
print(reverse_string(s))

#Input: hello → Output: olleh