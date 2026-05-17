def second_largest(lst):
    unique_lst = list(set(lst))  # remove duplicates
    if len(unique_lst) < 2:
        return None  # no second largest
    unique_lst.sort()
    return unique_lst[-2]

# Read input as space-separated numbers
lst = list(map(int, input().split()))

# Print output
print(second_largest(lst))


#input: 4 7 1 9 3 9 → Output: 7