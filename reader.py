from contacts import ContactBook

DATA_FILE = "contacts.txt"


def main() -> None:
    book = ContactBook()
    book.load_contacts(DATA_FILE)

    contacts = book.list_contacts()
    if not contacts:
        print("No contacts in the book.")
        return

    print("Contacts:")
    for i, contact in enumerate(contacts, start=1):
        print(f"{i}. {contact}")


if __name__ == "__main__":
    main()