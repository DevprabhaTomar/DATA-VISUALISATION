def count_occurrence(tup, element):
    count = 0
    for x in tup:
        if x == element:
            count += 1
    return count

# Read input as space-separated numbers
tup = tuple(map(int, input().split()))
element = int(input())

# Print output
print(count_occurrence(tup, element))

#Input:

1 2 3 2 4
2

#Output: 2