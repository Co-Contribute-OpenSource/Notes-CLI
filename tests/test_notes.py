import json
import os
import pytest
from notes_cli import notes, storage

TEST_FILE = "test_notes.json"

@pytest.fixture(autouse=True)
def setup_tmp_json(monkeypatch):
    """Use a temp file for tests."""
    monkeypatch.setattr(storage, "DATA_FILE", TEST_FILE)
    if os.path.exists(TEST_FILE):
        os.remove(TEST_FILE)
    yield
    if os.path.exists(TEST_FILE):
        os.remove(TEST_FILE)


def test_add_and_list_notes(capsys):
    notes.add_note("Write tests")
    notes.list_notes()
    output = capsys.readouterr().out
    assert "Write tests" in output


def test_search_notes(capsys):
    notes.add_note("Learn pytest")
    notes.search_notes("pytest")
    output = capsys.readouterr().out
    assert "Learn pytest" in output


def test_delete_note_success(capsys):
    notes.add_note("Temp note")
    notes.delete_note(1)
    output = capsys.readouterr().out
    assert "deleted successfully" in output


def test_delete_note_invalid_id(capsys):
    notes.delete_note(999)
    output = capsys.readouterr().out
    assert "Note not found" in output
