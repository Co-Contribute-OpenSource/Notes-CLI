from notes_cli import storage

def add_note(note_text):
    notes_list = storage.load_notes()
    note_id = max([note['id'] for note in notes_list], default=0) + 1
    new_note = {"id": note_id, "note": note_text}
    notes_list.append(new_note)
    storage.save_notes(notes_list)
    print(f"✅ Note added successfully with ID {note_id}")


def list_notes():
    notes_list = storage.load_notes()
    if not notes_list:
        print("📭 No notes found.")
        return
    print("🗒️  Your Notes:")
    for note in notes_list:
        print(f"{note['id']}: {note['note']}")


def search_notes(keyword):
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
    notes_list = storage.load_notes()
    for note in notes_list:
        if note["id"] == note_id:
            notes_list.remove(note)
            storage.save_notes(notes_list)
            print(f"🗑️ Note with ID {note_id} deleted successfully.")
            return
    print("❌ Note not found.")


def export_notes(output_file="exported_notes.txt"):
    notes_list = storage.load_notes()
    if not notes_list:
        print("📭 No notes to export.")
        return
    with open(output_file, "w") as f:
        for note in notes_list:
            f.write(f"{note['id']}: {note['note']}\n")
    print(f"✅ Notes exported successfully to {output_file}")


def update_note(note_id, new_text):
    """
    Update an existing note by ID.
    """
    notes_list = storage.load_notes()
    for note in notes_list:
        if note["id"] == note_id:
            note["note"] = new_text
            storage.save_notes(notes_list)
            print(f"✏️ Note {note_id} updated successfully.")
            return
    print("❌ Note not found.")

def import_notes(input_file="imported_notes.txt"):
    """
    Import notes from a text file. Each line becomes a new note.
    """
    if not os.path.exists(input_file):
        print("❌ File not found.")
        return

    with open(input_file, "r") as f:
        lines = [line.strip() for line in f.readlines() if line.strip()]

    if not lines:
        print("⚠️ No notes found in file.")
        return

    notes_list = storage.load_notes()
    next_id = max([note["id"] for note in notes_list], default=0) + 1

    for line in lines:
        notes_list.append({"id": next_id, "note": line})
        next_id += 1

    storage.save_notes(notes_list)
    print(f"📥 Imported {len(lines)} notes successfully.")

