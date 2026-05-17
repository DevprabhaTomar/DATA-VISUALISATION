def replace_negatives(lst):
    return [0 if x < 0 else x for x in lst]

# Read input as space-separated numbers
lst = list(map(int, input().split()))

# Print output
print(replace_negatives(lst))

#input: 3 -1 5 -7 2 → Output: [3, 0, 5, 0, 2]