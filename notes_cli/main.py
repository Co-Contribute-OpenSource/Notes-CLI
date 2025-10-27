#!/usr/bin/env python

# Placeholder for main execution logic
import argparse
from notes_cli import notes

def main():
    parser = argparse.ArgumentParser(
        description="🗒️ Notes CLI — Manage your notes from the command line"
    )

    subparsers = parser.add_subparsers(dest="command", help="Available commands")

    # add
    parser_add = subparsers.add_parser("add", help="Add a new note")
    parser_add.add_argument("note", type=str, help="The note text")

    # list
    subparsers.add_parser("list", help="List all notes")

    # search
    parser_search = subparsers.add_parser("search", help="Search notes by keyword")
    parser_search.add_argument("keyword", type=str, help="Keyword to search for")

    # delete
    parser_delete = subparsers.add_parser("delete", help="Delete a note by ID")
    parser_delete.add_argument("id", type=int, help="The ID of the note to delete")
    # export
    subparsers.add_parser("export", help="Export all notes to a text file")


    args = parser.parse_args()

    if args.command == "add":
        notes.add_note(args.note)
    elif args.command == "list":
        notes.list_notes()
    elif args.command == "search":
        notes.search_notes(args.keyword)
    elif args.command == "delete":
        notes.delete_note(args.id)
    elif args.command == "export":
        notes.export_notes()
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
