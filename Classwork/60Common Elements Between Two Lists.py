def common_elements(lst1, lst2):
    return list(set(lst1) & set(lst2))

# Read input as space-separated numbers
lst1 = list(map(int, input().split()))
lst2 = list(map(int, input().split()))

# Print output
print(common_elements(lst1, lst2))

#Input:

1 2 3
2 3 4

#Output: [2, 3]