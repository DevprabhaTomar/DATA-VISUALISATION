#Count Character Frequency Using Dictionary
def char_frequency(s):
    freq = {}
    for ch in s:
        if ch in freq:
            freq[ch] += 1
        else:
            freq[ch] = 1
    return freq

# Read input string
s = input()

# Print output
print(char_frequency(s))


#Input: hello → Output: {'h': 1, 'e': 1, 'l': 2, 'o': 1}