#Merge Two Dictionaries Manually
def merge_dicts(dict1, dict2):
    merged = dict1.copy()
    for key, value in dict2.items():
        merged[key] = value
    return merged

# Read first dictionary
n1 = int(input("Number of items in first dict: "))
dict1 = {}
for _ in range(n1):
    key, value = input().split()
    dict1[key] = int(value)

# Read second dictionary
n2 = int(input("Number of items in second dict: "))
dict2 = {}
for _ in range(n2):
    key, value = input().split()
    dict2[key] = int(value)

# Print merged dictionary
print(merge_dicts(dict1, dict2))

#Input:

2
a 1
b 2
2
b 3
c 4

#Output: {'a': 1, 'b': 3, 'c': 4}