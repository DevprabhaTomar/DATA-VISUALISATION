def tuple_to_list(tup):
    return list(tup)

# Read input as space-separated numbers
tup = tuple(map(int, input().split()))

# Print output
print(tuple_to_list(tup))

#Input: 1 2 3 4 5 → Output: [1, 2, 3, 4, 5]