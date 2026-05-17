num = int(input("Enter a number: "))

total = 0
num = abs(num)

while num > 0:
    total += num % 10
    num //= 10

print("Sum of digits:", total)

#output
Enter a number: 5
Sum of digits: 5
