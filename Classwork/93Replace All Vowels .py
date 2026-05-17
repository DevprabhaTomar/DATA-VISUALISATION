#Replace All Vowels with *
def replace_vowels(s):
    vowels = "aeiouAEIOU"
    result = ""
    for ch in s:
        if ch in vowels:
            result += "*"
        else:
            result += ch
    return result

# Read input string
s = input()

# Print output
print(replace_vowels(s))

#Input: Hello World → Output: H*ll* W*rld