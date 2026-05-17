#Generate Fibonacci Series Using Function
def fibonacci_series(n):
    a, b = 0, 1
    series = []
    for _ in range(n):
        series.append(a)
        a, b = b, a + b
    return series

# Read input
n = int(input())

# Print output
print(fibonacci_series(n))

#input
5
#output
[0, 1, 1, 2, 3]