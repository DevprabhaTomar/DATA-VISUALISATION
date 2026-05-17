#Check Whether Two Strings Are Anagrams
def are_anagrams(s1, s2):
    s1_clean = s1.replace(" ", "").lower()
    s2_clean = s2.replace(" ", "").lower()
    return sorted(s1_clean) == sorted(s2_clean)

# Read two strings
s1 = input()
s2 = input()

# Print output
print("Anagrams" if are_anagrams(s1, s2) else "Not Anagrams")


#input:

listen
silent

#Output:
Anagrams