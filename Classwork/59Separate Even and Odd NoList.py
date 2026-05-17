def separate_even_odd(lst):
    even = []
    odd = []
    for num in lst:
        if num % 2 == 0:
            even.append(num)
        else:
            odd.append(num)
    return even, odd

# Read input as space-separated numbers
lst = list(map(int, input().split()))

# Print output
even, odd = separate_even_odd(lst)
print("Even:", even)
print("Odd:", odd)

#Input: 1 2 3 4 5 
#Output:

Even: [2, 4]
Odd: [1, 3, 5]