contacts = {}

while True:
    print("\n1. Add Contact")
    print("2. Update Contact")
    print("3. Search Contact")
    print("4. Delete Contact")
    print("5. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        name = input("Name: ")
        phone = input("Phone: ")
        contacts[name] = phone

    elif choice == "2":
        name = input("Name: ")
        if name in contacts:
            contacts[name] = input("New Phone: ")

    elif choice == "3":
        name = input("Search Name: ")
        print(contacts.get(name, "Not found"))

    elif choice == "4":
        name = input("Delete Name: ")
        contacts.pop(name, None)

    elif choice == "5":
        break