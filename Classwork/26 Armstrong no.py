num = int(input())

n = abs(num)
original = n
sum = 0

while n > 0:
    digit = n % 10
    sum += digit ** 3
    n //= 10

if sum == original:
    print("Armstrong")
else:
    print("Not Armstrong")

    #input
    56
    #output
Not Armstrong