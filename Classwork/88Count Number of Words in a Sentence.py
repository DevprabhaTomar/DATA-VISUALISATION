def count_words(sentence):
    words = sentence.split()
    return len(words)

# Read input sentence
sentence = input()

# Print output
print(count_words(sentence))

#Input: Hello world from Python → Output: 4