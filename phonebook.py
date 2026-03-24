# Full Python Phonebook Program
phonebook = {}

def add_contact():
    name = input("Enter name: ")
    phone = input("Enter phone number: ")
    email = input("Enter email: ")
    phonebook[name] = {"phone": phone, "email": email}
    print(f"Contact {name} added successfully!")

def search_contact():
    name = input("Enter name to search: ")
    if name in phonebook:
        print(f"Name: {name}")
        print(f"Phone: {phonebook[name]['phone']}")
        print(f"Email: {phonebook[name]['email']}")
    else:
        print("Contact not found!")

def delete_contact():
    name = input("Enter name to delete: ")
    if name in phonebook:
        del phonebook[name]
        print(f"Contact {name} deleted successfully!")
    else:
        print("Contact not found!")

def show_all_contacts():
    if phonebook:
        for name, info in phonebook.items():
            print(f"Name: {name}, Phone: {info['phone']}, Email: {info['email']}")
    else:
        print("Phonebook is empty!")

# Main menu loop
while True:
    print("\n===== Phonebook Menu =====")
    print("1. Add Contact")
    print("2. Search Contact")
    print("3. Delete Contact")
    print("4. Show All Contacts")
    print("5. Exit")
    choice = input("Enter your choice (1-5): ")

    if choice == "1":
        add_contact()
    elif choice == "2":
        search_contact()
    elif choice == "3":
        delete_contact()
    elif choice == "4":
        show_all_contacts()
    elif choice == "5":
        print("Exiting phonebook. Goodbye!")
        break
    else:
        print("Invalid choice. Please enter 1-5.")