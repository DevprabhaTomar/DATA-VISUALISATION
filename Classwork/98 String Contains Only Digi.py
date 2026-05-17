#Check Whether String Contains Only Digits
def is_only_digits(s):
    for ch in s:
        if not ch.isdigit():
            return False
    return True

# Read input string
s = input()

# Print output
print("Digits Only" if is_only_digits(s) else "Contains Other Characters")

#Input: 12345 → Output: Digits Only
#Input: 123a5 → Output: Contains Other Characters