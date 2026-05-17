def max_in_tuple(tup):
    max_val = tup[0]
    for x in tup:
        if x > max_val:
            max_val = x
    return max_val

# Read input as space-separated numbers
tup = tuple(map(int, input().split()))

# Print output
print(max_in_tuple(tup))

#Input: 4 7 1 9 3 → Output: 9