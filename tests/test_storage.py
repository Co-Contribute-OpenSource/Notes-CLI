import os
from notes_cli import storage

TEST_FILE = "test_storage.json"


def test_save_and_load_notes(monkeypatch):
    monkeypatch.setattr(storage, "DATA_FILE", TEST_FILE)
    notes_data = [{"id": 1, "note": "Test storage"}]
    storage.save_notes(notes_data)
    loaded = storage.load_notes()
    assert loaded == notes_data
    os.remove(TEST_FILE)


def test_load_empty_file(monkeypatch):
    monkeypatch.setattr(storage, "DATA_FILE", "nonexistent.json")
    notes = storage.load_notes()
    assert notes == []
