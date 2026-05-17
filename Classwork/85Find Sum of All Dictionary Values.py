#Find Sum of All Dictionary Values
def sum_dict_values(d):
    total = 0
    for value in d.values():
        total += value
    return total

# Read dictionary
n = int(input())
d = {}
for _ in range(n):
    key, value = input().split()
    d[key] = int(value)

# Print sum
print(sum_dict_values(d))

#Input:

3
a 10
b 20
c 30

#Output: 60