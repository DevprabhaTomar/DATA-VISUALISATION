#Find First Non-Repeating Character in String
def first_non_repeating(s):
    freq = {}
    for ch in s:
        freq[ch] = freq.get(ch, 0) + 1
    for ch in s:
        if freq[ch] == 1:
            return ch
    return None

# Read input string
s = input()

# Print output
print(first_non_repeating(s))

#Input: swiss → Output: w