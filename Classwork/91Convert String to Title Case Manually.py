def to_title_case(s):
    words = s.split()
    title_words = []
    for word in words:
        if word:
            title_words.append(word[0].upper() + word[1:].lower())
    return " ".join(title_words)

# Read input string
s = input()

# Print output
print(to_title_case(s))

#Input: hello world from python → Output: Hello World From Python