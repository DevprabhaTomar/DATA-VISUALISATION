num = int(input())

count = 0
n = abs(num)

if n == 0:
    count = 1
else:
    while n > 0:
        count += 1
        n //= 10

print(count)

#input
567
#output
3