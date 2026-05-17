#Create Dictionary from Two Lists
def create_dict(keys, values):
    return {keys[i]: values[i] for i in range(len(keys))}

# Read keys
keys = input().split()
# Read values
values = list(map(int, input().split()))

# Print dictionary
print(create_dict(keys, values))

#Input:

a b c
1 2 3

#Output: {'a': 1, 'b': 2, 'c': 3}