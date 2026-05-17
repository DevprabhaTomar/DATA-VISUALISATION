def count_frequency(lst):
    freq = {}
    for item in lst:
        if item in freq:
            freq[item] += 1
        else:
            freq[item] = 1
    return freq

# Read input as space-separated numbers
lst = list(map(int, input().split()))

# Print output
print(count_frequency(lst))

#input: 1 2 2 3 1 2 → Output: {1: 2, 2: 3, 3: 1}