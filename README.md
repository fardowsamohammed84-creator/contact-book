# Contact Book

A simple command-line contact book in Python that lets you add, search, and list contacts. Contacts are persisted to a text file so they’re available the next time you run the program.

## Features

- Add new contacts (name + phone number)
- Search for a contact by name (case-insensitive)
- List all contacts
- Persistent storage using a text file (`contacts.txt`)
- Basic unit tests for core logic and persistence

## Requirements

- Python 3.10+ (works with 3.11, 3.12, etc.)

No external dependencies are required.

## Project Structure

```text
Contact-book/
├── contacts.py        # Contact and ContactBook classes
├── main.py            # CLI application (menu-driven)
├── reader.py          # Optional: simple reader that just lists contacts
├── test_contacts.py   # Unit tests
├── contacts.txt       # Persisted contacts (created automatically)
└── README.md          # This file
```

## Setup

1. Clone or copy the project to your machine.
2. Open a terminal in the `Contact-book` directory.
3. (Optional) Create and activate a virtual environment:

   ```bash
   python -m venv .venv
   # Windows PowerShell
   .venv\Scripts\Activate.ps1
   ```

No additional packages need to be installed.

## Usage

### Run the full application

```bash
python main.py
```

Menu options:

1. **Show all contacts** – list every contact in the book.  
2. **Add a new contact** – enter a name and phone number.  
3. **Search for a contact** – enter a name to find a contact.  
4. **Exit** – close the application.

Contacts are automatically saved to `contacts.txt` whenever you add a new one and loaded when the program starts.

### Run the reader only

To just view all stored contacts without the menu:

```bash
python reader.py
```

### Run the tests

From the `Contact-book` directory:

```bash
python -m unittest test_contacts.py -v
```

You should see all tests passing.

## Data Format

Contacts are stored in `contacts.txt`, one per line:

```text
Name|Phone
```

Example:

```text
Aisha - 0712345678
Omar - 0722345678
```

(Implementation uses `Name|Phone` internally; the display format is `Name - Phone`.)

## Extending the Project

Possible next steps:

- Add delete and edit operations.
- Add more fields (email, address, notes).
- Sort contacts by name when listing.
- Add input validation (e.g., phone number format).
- Replace the text file with JSON or a database.

## License

This is a learning project. You can reuse and modify the code as you like.