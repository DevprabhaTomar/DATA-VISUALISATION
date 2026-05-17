num = int(input())

reverse = 0
n = abs(num)

while n > 0:
    digit = n % 10
    reverse = reverse * 10 + digit
    n //= 10

print(reverse if num >= 0 else -reverse)

#input
456
#output
654