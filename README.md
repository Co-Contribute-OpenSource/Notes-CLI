

# Notes CLI

A simple command-line interface (CLI) tool to manage your notes.
This project is beginner-friendly and perfect for learning Python, open source, and contributing during Hacktoberfest.

---

## Features

- Add new notes
- List all notes
- Search notes by keyword
- Delete notes by ID
- Persistent storage using JSON

---

## Project Structure

```

notes-cli/
├── notes\_cli/
│   ├── **init**.py
│   ├── main.py           \# CLI entry point
│   ├── notes.py          \# Core notes functions
│   ├── storage.py        \# Handles reading/writing JSON
│   └── utils.py          \# Helper functions
├── data/
│   └── notes.json        \# Stores notes persistently
├── tests/
│   ├── test\_notes.py     \# Unit tests for notes.py
│   └── test\_storage.py   \# Unit tests for storage.py
├── requirements.txt      \# Dependencies (if any)
└── README.md

````

---

## Installation

1.  Clone the repository:

```bash
git clone [https://github.com/your-username/notes-cli.git](https://github.com/your-username/notes-cli.git)
cd notes-cli
````

2.  (Optional) Create a virtual environment:

<!-- end list -->

```bash
python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows
```

3.  Install dependencies (if any):

<!-- end list -->

```bash
pip install -r requirements.txt
```

## Usage

Run the CLI using Python:

```bash
python -m notes_cli.main <command> [options]
```

### Commands

**Add a note**

```bash
python -m notes_cli.main add "Buy groceries"
```

**List all notes**

```bash
python -m notes_cli.main list
```

**Search notes**

```bash
python -m notes_cli.main search "groceries"
```

**Delete a note**

```bash
python -m notes_cli.main delete 1
```

-----

## Contributing

We welcome contributions\! Here’s how to get started:

1.  **Fork** the repository
2.  Create a new branch: `git checkout -b feature/your-feature-name`
3.  Make your changes
4.  Commit your changes: `git commit -m "Add your descriptive message"`
5.  Push to the branch: `git push origin feature/your-feature-name`
6.  Create a **pull request**

Check out our [issues] for **good first issues**.

## License

This project is licensed under the **MIT License**. See the `LICENSE` file for details.

## Acknowledgements

  - Inspired by beginner-friendly Python projects
  - Perfect for Hacktoberfest contributions


```
