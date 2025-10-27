from notes_cli import storage

def add_note(note_text):
    """
    Add a new note to the system.
    Generates a unique ID, saves to notes.json, and prints success message.
    """
    notes_list = storage.load_notes()
    note_id = max([note['id'] for note in notes_list], default=0) + 1
    new_note = {"id": note_id, "note": note_text}
    notes_list.append(new_note)
    storage.save_notes(notes_list)
    print(f"✅ Note added successfully with ID {note_id}")


def list_notes():
    """
    Display all saved notes in a formatted way.
    """
    notes_list = storage.load_notes()

    if not notes_list:
        print("📭 No notes found.")
        return

    print("🗒️  Your Notes:")
    for note in notes_list:
        print(f"{note['id']}: {note['note']}")


def search_notes(keyword):
    """
    Search for notes containing the keyword (case-insensitive).
    """
    notes_list = storage.load_notes()
    keyword = keyword.lower()
    matched = [note for note in notes_list if keyword in note['note'].lower()]

    if not matched:
        print("❌ No matching notes found.")
        return

    print(f"🔍 Search results for '{keyword}':")
    for note in matched:
        print(f"{note['id']}: {note['note']}")


def delete_note(note_id):
    """
    Delete a note by its ID.
    """
    notes_list = storage.load_notes()
    updated_list = [note for note in notes_list if note['id'] != note_id]

    if len(updated_list) == len(notes_list):
        print("❌ Note not found.")
        return

    storage.save_notes(updated_list)
    print(f"🗑️  Note with ID {note_id} deleted successfully.")
