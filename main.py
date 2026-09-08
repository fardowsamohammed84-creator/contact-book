from contacts import Contact, ContactBook

DATA_FILE = "contacts.txt"


def show_contacts(contact_book: ContactBook) -> None:
    """Display all contacts in the book."""
    contacts = contact_book.list_contacts()
    if not contacts:
        print("No contacts in the book.")
        return

    print("\nContacts:")
    for i, contact in enumerate(contacts, start=1):
        print(f"{i}. {contact}")


def add_new_contact(contact_book: ContactBook) -> None:
    """Prompt the user to add a new contact."""
    name = input("Enter contact name: ").strip()
    phone = input("Enter contact phone number: ").strip()

    if not name or not phone:
        print("Name and phone number cannot be empty.")
        return

    new_contact = Contact(name, phone)
    if contact_book.add_contact(new_contact):
        contact_book.save_contacts(DATA_FILE)
        print(f"Contact '{name}' added successfully.")
    else:
        print(f"Contact '{name}' already exists.")


def search_contact(contact_book: ContactBook) -> None:
    """Prompt the user to search for a contact by name."""
    name = input("Enter the name of the contact to search: ").strip()
    if not name:
        print("Name cannot be empty.")
        return

    contact = contact_book.find_contact(name)
    if contact:
        print(f"Found contact: {contact}")
    else:
        print(f"No contact found with the name '{name}'.")


def main() -> None:
    """Run the contact book application."""
    contact_book = ContactBook()
    contact_book.load_contacts(DATA_FILE)

    while True:
        print("\nContact Book Menu:")
        print("1. Show all contacts")
        print("2. Add a new contact")
        print("3. Search for a contact")
        print("4. Exit")

        choice = input("Choose an option (1-4): ").strip()

        if choice == "1":
            show_contacts(contact_book)
        elif choice == "2":
            add_new_contact(contact_book)
        elif choice == "3":
            search_contact(contact_book)
        elif choice == "4":
            print("Exiting the contact book. Goodbye!")
            break
        else:
            print("Invalid option. Please choose a number between 1 and 4.")


if __name__ == "__main__":
    main()