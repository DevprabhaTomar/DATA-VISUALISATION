n = int(input("Enter number of rows: "))

num = 1
total = 0

for i in range(1, n + 1):
    for j in range(i):
        print(num, end=" ")
        total += num
        num += 1
    print()

print("Sum of numbers:", total)