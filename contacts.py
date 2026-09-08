class Contact:
    """Represent a single contact with a name and phone number."""

    def __init__(self, name: str, phone: str):
        self.name = name.strip()
        self.phone = phone.strip()

    def __str__(self) -> str:
        return f"{self.name} - {self.phone}"

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Contact):
            return NotImplemented
        return self.name.lower() == other.name.lower()


class ContactBook:
    """Manage a collection of contacts with basic CRUD operations."""

    def __init__(self) -> None:
        self.contacts: list[Contact] = []

    def add_contact(self, contact: Contact) -> bool:
        """
        Add a contact if no contact with the same name (case-insensitive) exists.

        Returns:
            True if the contact was added, False if a duplicate name was found.
        """
        for existing in self.contacts:
            if existing.name.lower() == contact.name.lower():
                return False
        self.contacts.append(contact)
        return True

    def find_contact(self, name: str) -> Contact | None:
        """
        Find a contact by name (case-insensitive).

        Returns:
            The matching Contact, or None if not found.
        """
        cleaned = name.strip().lower()
        for contact in self.contacts:
            if contact.name.lower() == cleaned:
                return contact
        return None

    def list_contacts(self) -> list[Contact]:
        """Return a list of all contacts."""
        return list(self.contacts)

    # ---------- Persistence ----------

    def save_contacts(self, filename: str) -> None:
        """
        Save contacts to a text file.

        Format: one contact per line as 'Name|Phone'.
        """
        with open(filename, "w", encoding="utf-8") as f:
            for contact in self.contacts:
                f.write(f"{contact.name}|{contact.phone}\n")

    def load_contacts(self, filename: str) -> None:
        """
        Load contacts from a text file.

        Format: one contact per line as 'Name|Phone'.
        Silently ignores a missing file or invalid lines.
        """
        try:
            with open(filename, "r", encoding="utf-8") as f:
                for line in f:
                    line = line.strip()
                    if not line:
                        continue  # skip empty lines
                    if "|" not in line:
                        continue  # skip malformed lines
                    name, phone = line.split("|", 1)
                    if not name or not phone:
                        continue  # skip lines with empty name/phone
                    contact = Contact(name, phone)
                    self.add_contact(contact)
        except FileNotFoundError:
            # No file yet; start with an empty book
            pass