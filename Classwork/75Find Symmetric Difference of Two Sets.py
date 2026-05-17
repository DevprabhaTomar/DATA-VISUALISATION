#Find Symmetric Difference of Two Sets
def symmetric_difference(set1, set2):
    return set1 ^ set2  # elements in either set1 or set2 but not both

# Read input as space-separated numbers
set1 = set(map(int, input().split()))
set2 = set(map(int, input().split()))

# Print output
print(symmetric_difference(set1, set2))

#Input:

1 2 3
3 4 5

#Output: {1, 2, 4, 5}