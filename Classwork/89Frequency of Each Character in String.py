def char_frequency(s):
    freq = {}
    for ch in s:
        if ch != " ":
            freq[ch] = freq.get(ch, 0) + 1
    return freq

# Read input string
s = input()

# Print output
print(char_frequency(s))

#Input: hello → Output: {'h': 1, 'e': 1, 'l': 2, 'o': 1}