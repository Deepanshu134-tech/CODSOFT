# contact_book.py

class Contact:
    def __init__(self, name, phone, email, address):
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address

    def __str__(self):
        return f"{self.name}: {self.phone}, {self.email}, {self.address}"

class ContactBook:
    def __init__(self):
        self.contacts = []

    def add_contact(self):
        name = input("Enter name: ")
        phone = input("Enter phone: ")
        email = input("Enter email: ")
        address = input("Enter address: ")
        new_contact = Contact(name, phone, email, address)
        self.contacts.append(new_contact)
        print(f"Contact {name} added successfully!")

    def view_contacts(self):
        if not self.contacts:
            print("Contact book is empty!")
        else:
            for i, contact in enumerate(self.contacts, start=1):
                print(f"{i}. {contact.name}: {contact.phone}")

    def search_contact(self):
        query = input("Enter search query: ")
        results = [contact for contact in self.contacts if query.lower() in contact.name.lower() or query.lower() in contact.phone.lower()]
        if not results:
            print("No contacts found!")
        else:
            for contact in results:
                print(contact)

    def update_contact(self):
        name = input("Enter name of contact to update: ")
        for contact in self.contacts:
            if contact.name.lower() == name.lower():
                print("Enter new details (press enter to keep current value):")
                contact.name = input(f"Enter new name ({contact.name}): ") or contact.name
                contact.phone = input(f"Enter new phone ({contact.phone}): ") or contact.phone
                contact.email = input(f"Enter new email ({contact.email}): ") or contact.email
                contact.address = input(f"Enter new address ({contact.address}): ") or contact.address
                print(f"Contact {contact.name} updated successfully!")
                return
        print("Contact not found!")

    def delete_contact(self):
        name = input("Enter name of contact to delete: ")
        for contact in self.contacts:
            if contact.name.lower() == name.lower():
                self.contacts.remove(contact)
                print(f"Contact {contact.name} deleted successfully!")
                return
        print("Contact not found!")

def main():
    contact_book = ContactBook()

    while True:
        print("\nContact Book Menu:")
        print("1. Add Contact")
        print("2. View Contact List")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            contact_book.add_contact()
        elif choice == "2":
            contact_book.view_contacts()
        elif choice == "3":
            contact_book.search_contact()
        elif choice == "4":
            contact_book.update_contact()
        elif choice == "5":
            contact_book.delete_contact()
        elif choice == "6":
            print("Exiting contact book...")
            break
        else:
            print("Invalid choice. Please try again!")

if __name__ == "__main__":
    main()