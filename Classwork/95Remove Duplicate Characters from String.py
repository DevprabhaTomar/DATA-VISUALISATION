def remove_duplicates(s):
    result = ""
    seen = set()
    for ch in s:
        if ch not in seen:
            seen.add(ch)
            result += ch
    return result

# Read input string
s = input()

# Print output
print(remove_duplicates(s))

#Input: programming → Output: progamin