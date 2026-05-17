from collections import Counter

file = open("text.txt", "r")
text = file.read().lower()

words = text.split()
freq = Counter(words)

print("Top 5 words:")
for word, count in freq.most_common(5):
    print(word, ":", count)