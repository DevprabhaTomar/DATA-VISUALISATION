#check whether Key Exists in Dictionary
def key_exists(d, key):
    return key in d

# Read dictionary
n = int(input())
d = {}
for _ in range(n):
    key, value = input().split()
    d[key] = int(value)

# Read key to check
key_to_check = input()

# Print output
print("Key Exists" if key_exists(d, key_to_check) else "Key Does Not Exist")

#Input:

2
a 10
b 20
b

#Output: Key Exists