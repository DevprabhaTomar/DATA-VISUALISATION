def sum_list(lst):
    total = 0
    for num in lst:
        total += num
    return total

# Read input
lst = list(map(int, input().split()))

# Print output
print(sum_list(lst))

#input: 1 2 3 4 5 → Output: 15