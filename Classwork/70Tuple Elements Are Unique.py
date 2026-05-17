def are_elements_unique(tup):
    return len(tup) == len(set(tup))

# Read input as space-separated numbers
tup = tuple(map(int, input().split()))

# Print output
print("Unique" if are_elements_unique(tup) else "Not Unique")

#Input: 1 2 3 4 → Output: Unique
