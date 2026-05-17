def difference_sets(set1, set2):
    return set1 - set2

# Read input as space-separated numbers
set1 = set(map(int, input().split()))
set2 = set(map(int, input().split()))

# Print output
print(difference_sets(set1, set2))

#Input:

1 2 3 4
3 4 5

#Output: {1, 2}