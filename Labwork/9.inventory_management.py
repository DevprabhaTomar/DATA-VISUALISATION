# File Name: inventory_management.py

inventory = {}

while True:
    print("\n--- Inventory Menu ---")
    print("1. Add Product")
    print("2. Update Quantity")
    print("3. Search Product")
    print("4. Display Low Stock Items")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        product = input("Enter product name: ")
        quantity = int(input("Enter quantity: "))

        inventory[product] = quantity
        print("Product added successfully")

    elif choice == 2:
        product = input("Enter product name: ")

        if product in inventory:
            quantity = int(input("Enter new quantity: "))
            inventory[product] = quantity
            print("Quantity updated")
        else:
            print("Product not found")

    elif choice == 3:
        product = input("Enter product name: ")

        if product in inventory:
            print(product, "Quantity:", inventory[product])
        else:
            print("Product not found")

    elif choice == 4:
        print("Low Stock Items:")

        for product, quantity in inventory.items():
            if quantity < 5:
                print(product, ":", quantity)

    elif choice == 5:
        print("Exiting program")
        break

    else:
        print("Invalid choice")