def remove_spaces(s):
    result = ""
    for ch in s:
        if ch != " ":
            result += ch
    return result

# Read input string
s = input()

# Print output
print(remove_spaces(s))


#Input: Hello World → Output: HelloWorld