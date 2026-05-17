#Safely Remove a Key from Dictionary
def safe_remove_key(d, key):
    if key in d:
        del d[key]
    return d

# Read dictionary
n = int(input())
d = {}
for _ in range(n):
    key, value = input().split()
    d[key] = int(value)

# Read key to remove
key_to_remove = input()

# Print dictionary after removal
print(safe_remove_key(d, key_to_remove))

#Input:

3
a 1
b 2
c 3
b

#Output: {'a': 1, 'c': 3}