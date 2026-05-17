#Find Key with Maximum Value
def key_with_max_value(d):
    return max(d, key=d.get)

# Read dictionary
n = int(input())
d = {}
for _ in range(n):
    key, value = input().split()
    d[key] = int(value)

# Print key with maximum value
print(key_with_max_value(d))

#Input:

3
a 10
b 25
c 15

#Output: b