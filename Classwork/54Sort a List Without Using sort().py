def sort_list(lst):
    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            if lst[i] > lst[j]:
                lst[i], lst[j] = lst[j], lst[i]
    return lst

# Read input as space-separated numbers
lst = list(map(int, input().split()))

# Print output
print(sort_list(lst))

#Input: 4 1 9 3 7 → Output: [1, 3, 4, 7, 9]
