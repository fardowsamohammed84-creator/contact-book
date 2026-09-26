# Contact Book

A simple command-line contact book in Python that lets you add, search, and list contacts. Contacts are persisted to a JSON file so they're available the next time you run the program.

## Features

- Add new contacts (name + phone number)
- Search for a contact by name (case-insensitive)
- List all contacts
- Persistent storage using a JSON file (`contacts.json`)
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
├── contacts.json      # Persisted contacts (created automatically)
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

Contacts are automatically saved to `contacts.json` whenever you add a new one and loaded when the program starts.

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

## Data Format (JSON)

Contacts are stored in `contacts.json` as a JSON array of objects:

```json
[
  {
    "name": "Aisha",
    "phone": "0712345678"
  },
  {
    "name": "Omar",
    "phone": "0722345678"
  }
]
```

On start, the app loads contacts from `contacts.json` (or starts empty if the file is missing or invalid). After adding a contact, the app saves all contacts back to `contacts.json`.

## Extending the Project

Possible next steps:

- Add delete and edit operations.
- Add more fields (email, address, notes).
- Sort contacts by name when listing.
- Add input validation (e.g., phone number format).
- Replace the JSON file with a database for larger-scale apps.

## License

This is a learning project. You can reuse and modify the code as you like.