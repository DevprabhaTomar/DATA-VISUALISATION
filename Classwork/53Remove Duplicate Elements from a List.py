def remove_duplicates(lst):
    seen = set()
    result = []
    for item in lst:
        if item not in seen:
            seen.add(item)
            result.append(item)
    return result

# Read input as space-separated numbers
lst = list(map(int, input().split()))

# Print output
print(remove_duplicates(lst))

#Input: 1 2 2 3 4 3 → Output: [1, 2, 3, 4]