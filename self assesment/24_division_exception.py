def divide(a, b):
    try:
        result = a / b
        print("Result:", result)
    except ZeroDivisionError:
        print("Error: Cannot divide by zero")
    except ValueError:
        print("Error: Invalid input")
    except Exception as e:
        print("Unexpected error:", e)

try:
    x = float(input("Enter first number: "))
    y = float(input("Enter second number: "))
    divide(x, y)
except ValueError:
    print("Please enter numeric values only")