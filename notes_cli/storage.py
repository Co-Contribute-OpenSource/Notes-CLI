import json
import os

DATA_FILE = "data/notes.json"

def load_notes():
    """
    Load notes from notes.json.
    Returns an empty list if file is missing or invalid.
    """
    if not os.path.exists(DATA_FILE):
        return []

    with open(DATA_FILE, "r") as f:
        try:
            return json.load(f)
        except json.JSONDecodeError:
            return []


def save_notes(notes_list):
    """
    Save all notes into notes.json.
    Creates the data directory if it doesn't exist.
    """
    os.makedirs(os.path.dirname(DATA_FILE), exist_ok=True)
    with open(DATA_FILE, "w") as f:
        json.dump(notes_list, f, indent=4)
