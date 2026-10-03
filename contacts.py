import json
from pathlib import Path


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

    def save_contacts(self, filename: str = "contacts.json") -> None:
        """
        Save contacts to a JSON file.

        Format: list of {"name": "...", "phone": "..."} objects.
        """
        data = [
            {"name": contact.name, "phone": contact.phone}
            for contact in self.contacts
        ]
        try:
            with open(filename, "w", encoding="utf-8") as f:
                json.dump(data, f, indent=2, ensure_ascii=False)
        except OSError:
            # If we can't write, just don't crash the whole program
            pass

    def load_contacts(self, filename: str = "contacts.json") -> None:
        """
        Load contacts from a JSON file.

        Format: list of {"name": "...", "phone": "..."} objects.
        Silently ignores a missing file or invalid lines.
        """
        try:
            with open(filename, "r", encoding="utf-8") as f:
                data = json.load(f)
        except FileNotFoundError:
            # No file yet; start with an empty book
            return
        except (json.JSONDecodeError, OSError):
            # Corrupt or unreadable file; start fresh
            return

        if not isinstance(data, list):
            return

        for item in data:
            if not isinstance(item, dict):
                continue
            name = item.get("name")
            phone = item.get("phone")
            #Require both fields to exist
            if not name or not phone:
                continue

            #Require both fields to be strings
            if not isinstance(name, str) or not isinstance(phone, str):
                continue  

            name = str(name).strip()
            phone = str(phone).strip()

            #Require both fields to be non-empty after stripping
            if not name or not phone:
                continue
            contact = Contact(name, phone)
            self.add_contact(contact)