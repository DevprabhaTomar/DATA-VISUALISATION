#Check Palindrome String Using Function
def check_palindrome(s):
    if s == s[::-1]:
        return "Palindrome"
    else:
        return "Not Palindrome"

# Read input
string = input().strip()

# Print output
print(check_palindrome(string))

#output
5
pallindrome