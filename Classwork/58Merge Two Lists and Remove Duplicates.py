def merge_remove_duplicates(lst1, lst2):
    merged = lst1 + lst2
    return list(set(merged))

# Read input as space-separated numbers
lst1 = list(map(int, input().split()))
lst2 = list(map(int, input().split()))

# Print output
print(merge_remove_duplicates(lst1, lst2))

#output
6
7
[6, 7]