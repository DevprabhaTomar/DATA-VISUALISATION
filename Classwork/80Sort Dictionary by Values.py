#Sort Dictionary by Values
def sort_dict_by_values(d):
    return dict(sorted(d.items(), key=lambda item: item[1]))

# Read dictionary
n = int(input())
d = {}
for _ in range(n):
    key, value = input().split()
    d[key] = int(value)

# Print sorted dictionary
print(sort_dict_by_values(d))

#Input:

3
a 3
b 1
c 2

#Output: {'b': 1, 'c': 2, 'a': 3}