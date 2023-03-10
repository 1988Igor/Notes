import json
import random
from datetime import datetime
from note import Note

class NotesManager:
  def __init__(self, file_path):
    super().__init__()
    self.file_path = file_path
    self.notes = self.load_notes()

  def load_notes(self):
    try:
      with open(self.file_path, "r") as f:
        notes_data = json.load(f)
    except FileNotFoundError:
      return []
    else:
      notes = [Note.from_dict(note_dict) for note_dict in notes_data]
      print(f"Loaded {len(notes)} notes from file {self.file_path}")
      return notes

  def save_notes(self):
    notes_data = [note.to_dict() for note in self.notes]
    with open(self.file_path, "w") as f:
      json.dump(notes_data, f, indent=4, separators=(';', ':'))

  def add_note(self, title, body):
    if not title or not body:
      print("Title and body are required.")
      return
    id = random.randint(1, 101);
    note = Note(id, title, body)
    self.notes.append(note)
    self.save_notes()
    print("Note added successfully.")

  def view_notes(self, created_date=None):
    if created_date:
      notes = [note for note in self.notes if
               note.created_time.date() == created_date]
    else:
      notes = self.notes
    for note in notes:
      print(
          f"Id: {note.id}\nTitle: {note.title}\nContent: {note.body}\nDate: ({note.created_time})")
      print()

  def edit_note(self, note_id, title=None, body=None):
    note = self.get_note_by_id(note_id)
    if note:
      if title is not None and title != "":
        note.title = title
      if body is not None and body != "":
        note.body = body
      note.updated_time = datetime.now()
      self.save_notes()
      print("Note updated successfully.")
    else:
      print(f"Note with id {note_id} not found.")

  def delete_note(self, note_id):
    note = self.get_note_by_id(note_id)
    if note:
      self.notes.remove(note)
      self.save_notes()
      print("Note deleted successfully.")
    else:
      print(f"Note with id {note_id} not found.")

  def get_note_by_id(self, note_id):
    for note in self.notes:
      if note.id == note_id:
        return note
    return None