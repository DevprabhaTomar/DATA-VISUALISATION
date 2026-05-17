def longest_word(sentence):
    words = sentence.split()
    max_len = 0
    longest = ""
    for word in words:
        if len(word) > max_len:
            max_len = len(word)
            longest = word
    return longest

# Read input sentence
sentence = input()

# Print output
print(longest_word(sentence))

#Input: Python programming is fun → Output: programming