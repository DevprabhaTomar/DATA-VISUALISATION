#Sort Dictionary by Keys
def sort_dict_by_keys(d):
    return dict(sorted(d.items()))

# Read dictionary
n = int(input())
d = {}
for _ in range(n):
    key, value = input().split()
    d[key] = int(value)

# Print sorted dictionary
print(sort_dict_by_keys(d))

#Input:

3
b 2
a 1
c 3

#Output: {'a': 1, 'b': 2, 'c': 3}