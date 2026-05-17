# File Name: prime_numbers.py

n = int(input("Enter how many prime numbers you want: "))

count = 0
num = 2
sum_prime = 0

print("Prime numbers are:")

while count < n:
    prime = True

    for i in range(2, num):
        if num % i == 0:
            prime = False
            break

    if prime:
        print(num, end=" ")
        sum_prime += num
        count += 1

    num += 1

average = sum_prime / n

print("\nSum of prime numbers:", sum_prime)
print("Average of prime numbers:", average)