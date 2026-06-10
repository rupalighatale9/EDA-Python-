import json

# Load contacts from file
def load_contacts():
    try:
        with open("contacts.json", "r") as file:
            return json.load(file)
    except:
        return {}

# Save contacts to file
def save_contacts(contacts):
    with open("contacts.json", "w") as file:
        json.dump(contacts, file)

contacts = load_contacts()

# Add contact
def add_contact():
    name = input("Enter Name: ")
    phone = input("Enter Phone: ")
    email = input("Enter Email: ")
    
    contacts[name] = {
        "phone": phone,
        "email": email
    }
    
    save_contacts(contacts)
    print("Contact saved successfully!\n")

# View contacts
def view_contacts():
    if not contacts:
        print("No contacts found.\n")
    else:
        for name, details in contacts.items():
            print("Name:", name)
            for key, value in details.items():
                print(key, ":", value)
            print()

# Search contact
def search_contact():
    name = input("Enter name: ")
    
    if name in contacts:
        print("Contact found:")
        for key, value in contacts[name].items():
            print(key, ":", value)
    else:
        print("Contact not found.\n")

# Delete contact
def delete_contact():
    name = input("Enter name: ")
    
    if name in contacts:
        del contacts[name]
        save_contacts(contacts)
        print("Contact deleted.\n")
    else:
        print("Contact not found.\n")

# Menu
while True:
    print("Contact Book Menu")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Delete Contact")
    print("5. Exit")
    
    choice = input("Enter choice: ")
    
    if choice == "1":
        add_contact()
    elif choice == "2":
        view_contacts()
    elif choice == "3":
        search_contact()
    elif choice == "4":
        delete_contact()
    elif choice == "5":
        break
    else:
        print("Invalid choice\n")