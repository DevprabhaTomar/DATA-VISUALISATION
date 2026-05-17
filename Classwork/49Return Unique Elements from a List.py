def unique_elements(lst):
    unique = []
    for item in lst:
        if item not in unique:
            unique.append(item)
    return unique

# Read input as space-separated numbers
lst = list(map(int, input().split()))

# Print output
print(unique_elements(lst))

#Input 1 2 2 3 4 3 
#Output [1, 2, 3, 4]