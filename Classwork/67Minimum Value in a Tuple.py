def min_in_tuple(tup):
    min_val = tup[0]
    for x in tup:
        if x < min_val:
            min_val = x
    return min_val

# Read input as space-separated numbers
tup = tuple(map(int, input().split()))

# Print output
print(min_in_tuple(tup))

#Input: 4 7 1 9 3 → Output: 1