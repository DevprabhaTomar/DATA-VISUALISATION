def reverse_list(lst):
    rev = []
    for i in range(len(lst)-1, -1, -1):
        rev.append(lst[i])
    return rev

# Read input as space-separated numbers
lst = list(map(int, input().split()))

# Print output
print(reverse_list(lst))

#input: 1 2 3 4 5 → Output: [5, 4, 3, 2, 1]