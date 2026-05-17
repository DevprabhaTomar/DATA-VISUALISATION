def rotate_list(lst, k):
    n = len(lst)
    k = k % n  # handle k > n
    return lst[-k:] + lst[:-k]

# Read input
lst = list(map(int, input().split()))
k = int(input())

# Print output
print(rotate_list(lst, k))

#Input:

1 2 3 4 5
2

#Output: [4, 5, 1, 2, 3]