sentence = input("Enter a sentence: ").lower()

vowels = []
consonants = []

for ch in sentence:
    if ch.isalpha():
        if ch in "aeiou":
            vowels.append(ch)
        else:
            consonants.append(ch)

print("Vowels:", vowels)
print("Consonants:", consonants)