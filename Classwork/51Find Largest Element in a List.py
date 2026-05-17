def largest_element(lst):
    max_val = lst[0]
    for item in lst:
        if item > max_val:
            max_val = item
    return max_val

# Read input as space-separated numbers
lst = list(map(int, input().split()))

# Print output
print(largest_element(lst))

#Input: 4 7 1 9 3 
#Output: 9