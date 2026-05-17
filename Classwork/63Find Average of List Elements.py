def average_list(lst):
    total = sum(lst)
    return total / len(lst) if lst else 0

# Read input
lst = list(map(int, input().split()))

# Print output
print(average_list(lst))

#Input: 1 2 3 4 5 → Output: 3.0