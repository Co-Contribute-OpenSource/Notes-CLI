from notes_cli import storage

def add_note(note_text):
    """
    Add a new note to the system.
    Generates a unique ID, saves to notes.json, and prints success message.
    """
    notes_list = storage.load_notes()  # Load existing notes
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
