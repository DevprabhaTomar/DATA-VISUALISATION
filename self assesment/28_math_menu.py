def factorial(n):
    fact = 1
    for i in range(1, n+1):
        fact *= i
    return fact

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def is_armstrong(n):
    digits = str(n)
    power = len(digits)
    total = sum(int(d)**power for d in digits)
    return total == n

while True:
    print("\n1. Factorial")
    print("2. Prime Check")
    print("3. Armstrong Check")
    print("4. Exit")

    choice = int(input("Enter choice: "))

    if choice == 1:
        n = int(input("Enter number: "))
        print("Factorial:", factorial(n))

    elif choice == 2:
        n = int(input("Enter number: "))
        print("Prime:", is_prime(n))

    elif choice == 3:
        n = int(input("Enter number: "))
        print("Armstrong:", is_armstrong(n))

    elif choice == 4:
        break