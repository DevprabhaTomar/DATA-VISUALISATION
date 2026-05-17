pin = "1234"
attempts = 3

while attempts > 0:
    entered = input("Enter PIN: ")

    if entered == pin:
        print("Access Granted")
        break
    else:
        attempts -= 1
        print("Wrong PIN. Attempts left:", attempts)

if attempts == 0:
    print("Account Locked!")