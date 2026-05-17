try:
    age = input("Enter your age: ")

    if not age.isdigit():
        raise ValueError("Not a number")

    age = int(age)

    if age >= 18:
        print("Eligible to vote")
    else:
        print("Not eligible to vote")

except ValueError:
    print("Invalid input! Please enter a valid number.")