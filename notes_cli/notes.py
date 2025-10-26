# def

from notes_cli import storage

def add_note(note_text):
    """
    Add a new note to the system.
    Generates a unique ID, saves to notes.json, and prints success message.
    """
    notes_list = storage.load_notes()  # Load existing notes

    # Generate unique ID
    note_id = max([note['id'] for note in notes_list], default=0) + 1

    # Create and add note
    new_note = {"id": note_id, "note": note_text}
    notes_list.append(new_note)

    # Save to storage
    storage.save_notes(notes_list)

    print(f"✅ Note added successfully with ID {note_id}")
