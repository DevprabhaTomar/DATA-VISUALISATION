def is_palindrome(lst):
    return lst == lst[::-1]

# Read input as space-separated numbers
lst = list(map(int, input().split()))

# Print output
print("Palindrome" if is_palindrome(lst) else "Not Palindrome")


#output
5
pallindrome