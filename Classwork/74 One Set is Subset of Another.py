#Check Whether One Set is Subset of Another
def is_subset(set1, set2):
    return set1 <= set2  # True if set1 is subset of set2

# Read input as space-separated numbers
set1 = set(map(int, input().split()))
set2 = set(map(int, input().split()))

# Print output
print("Subset" if is_subset(set1, set2) else "Not Subset")

#Input:

1 2
1 2 3 4

#Output: Subset