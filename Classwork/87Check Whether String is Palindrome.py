def is_palindrome(s):
    return s == reverse_string(s)

def reverse_string(s):
    rev = ""
    for i in range(len(s)-1, -1, -1):
        rev += s[i]
    return rev

# Read input string
s = input()

# Print output
print("Palindrome" if is_palindrome(s) else "Not Palindrome")

#Input: madam → Output: Palindrome
#Input: hello → Output: Not Palindrome