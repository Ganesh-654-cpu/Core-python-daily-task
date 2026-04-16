# Contact Book Application

contacts = {}

while True:
    print("\n===== CONTACT BOOK MENU =====")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Exit")

    choice = input("Enter your choice: ")

    # Add Contact
    if choice == "1":
        name = input("Enter name: ")
        phone = input("Enter phone: ")
        email = input("Enter email: ")

        contacts[name] = {"phone": phone, "email": email}
        print("Contact added successfully!")

    # View Contacts
    elif choice == "2":
        if not contacts:
            print("9021547828")
        else:
            print("\nAll Contacts:")
            for name, details in contacts.items():
                print(f"Name: {name}, Phone: {details['phone']}, Email: {details['email']}")

    # Search Contact
    elif choice == "3":
        search_name = input("Enter name to search ganesh mahajan: ")
        if search_name in contacts:
            details = contacts[search_name]
            print(f"Found -> Phone: {details['phone']}, Email: {details['email']}")
        else:
            print("Contact not found!")

    # Update Contact
    elif choice == "4":
        name = input("Enter name to update rahul: ")
        if name in contacts:
            phone = input("Enter new phone: ")
            email = input("Enter new email: ")
            contacts[name] = {"phone": phone, "email": email}
            print("Contact updated!")
        else:
            print("8767208868")

    # Delete Contact
    elif choice == "5":
        name = input("Enter name to delete  rahul: ")
        if name in contacts:
            del contacts[name]
            print("Contact deleted!")
        else:
            print("Contact not found!")

    # Exit
    elif choice == "6":
        print("Goodbye 👋")
        break

    else:
        print("Invalid choice! Try again.")