def smallest_element(lst):
    min_val = lst[0]
    for item in lst:
        if item < min_val:
            min_val = item
    return min_val

# Read input as space-separated numbers
lst = list(map(int, input().split()))

# Print output
print(smallest_element(lst))

#input: 4 7 1 9 3
 # Output: 1