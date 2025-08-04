contacts = []

def add_contact():
    print("\nAdd Contact")
    name = input(" Name: ")
    phone = input("Phone Number: ")
    email = input("Email: ")
    address = input("Address: ")
    contacts.append({
        "name": name,
        "phone": phone,
        "email": email,
        "address": address
    })
    print("Contact added successfully")

def view_contacts():
    print("\nContact List")
    if not contacts:
        print("No contacts available")
    else:
        for i, contact in enumerate(contacts, start=1):
            print(f"{i}. {contact['name']} - {contact['phone']}")

def search_contact():
    print("\n Search Contact")
    keyword = input("Enter name or phone to search: ").lower()
    found = False
    for contact in contacts:
        if keyword in contact['name'].lower() or keyword in contact['phone']:
            print(f"\nName: {contact['name']}\nPhone: {contact['phone']}\nEmail: {contact['email']}\nAddress: {contact['address']}")
            found = True
    if not found:
        print("Contact not found.")

def update_contact():
    print("\nUpdate Contact")
    name = input("Enter the  name to update: ")
    for contact in contacts:
        if contact["name"].lower() == name.lower():
            contact["phone"] = input("New Phone Number: ")
            contact["email"] = input("New Email: ")
            contact["address"] = input("New Address: ")
            print("Contact updated successfully")
            return
    print("Contact not found.")

def delete_contact():
    print("\n Delete Contact")
    name = input("Enter the  name to delete: ")
    for i, contact in enumerate(contacts):
        if contact["name"].lower() == name.lower():
            del contacts[i]
            print("Contact deleted successfully")
            return
    print("Contact not found.")

def main():
    while True:
        print("\nContact Management")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")
        choice = input("Enter your choice (1-6): ")

        if choice == "1":
            add_contact()
        elif choice == "2":
            view_contacts()
        elif choice == "3":
            search_contact()
        elif choice == "4":
            update_contact()
        elif choice == "5":
            delete_contact()
        elif choice == "6":
            print("Exiting program")
            break
        else:
            print("Invalid choice")

if _name_ == "_main_":
    main()
