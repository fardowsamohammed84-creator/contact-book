import unittest
import os
from contacts import Contact, ContactBook


class TestContactBook(unittest.TestCase):
    def setUp(self) -> None:
        """Create a fresh ContactBook for each test."""
        self.book = ContactBook()

    # --- Core functionality ---

    def test_add_contact_success(self) -> None:
        contact = Contact("Alice", "1234567890")
        result = self.book.add_contact(contact)
        self.assertTrue(result)
        self.assertIn(contact, self.book.list_contacts())

    def test_add_contact_duplicate(self) -> None:
        c1 = Contact("Bob", "0987654321")
        c2 = Contact("bob", "1112223333")  # same name, different case
        self.book.add_contact(c1)
        result = self.book.add_contact(c2)
        self.assertFalse(result)
        self.assertEqual(len(self.book.list_contacts()), 1)

    def test_find_contact_exists(self) -> None:
        c = Contact("Charlie", "5555555555")
        self.book.add_contact(c)
        found = self.book.find_contact("charlie")
        self.assertIsNotNone(found)
        self.assertEqual(found.name, "Charlie")

    def test_find_contact_not_exists(self) -> None:
        found = self.book.find_contact("NonExistent")
        self.assertIsNone(found)

    def test_list_contacts_empty(self) -> None:
        self.assertEqual(self.book.list_contacts(), [])

    def test_list_contacts_non_empty(self) -> None:
        c1 = Contact("David", "4444444444")
        c2 = Contact("Eve", "3333333333")
        self.book.add_contact(c1)
        self.book.add_contact(c2)
        contacts = self.book.list_contacts()
        self.assertIn(c1, contacts)
        self.assertIn(c2, contacts)

    # --- Persistence ---

    def test_save_and_load_contacts(self) -> None:
        test_file = "test_contacts_temp.txt"

        c1 = Contact("Aisha", "0712345678")
        c2 = Contact("Omar", "0722345678")
        self.book.add_contact(c1)
        self.book.add_contact(c2)

        self.book.save_contacts(test_file)

        new_book = ContactBook()
        new_book.load_contacts(test_file)

        loaded = new_book.list_contacts()
        self.assertEqual(len(loaded), 2)

        names = {c.name for c in loaded}
        self.assertIn("Aisha", names)
        self.assertIn("Omar", names)

        if os.path.exists(test_file):
            os.remove(test_file)

    def test_load_contacts_missing_file(self) -> None:
        self.book.load_contacts("nonexistent_file.txt")
        self.assertEqual(self.book.list_contacts(), [])


if __name__ == "__main__":
    unittest.main()