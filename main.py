from datetime import datetime
from notes_manager import NotesManager
if __name__ == "__main__":
  manager = NotesManager('notes.json')

  while True:
    command = input("Введите команду (add, view, edit, delete, exit): ")

    if command == "add":
      title = input("Введите название заметки: ")
      body = input("Введите текст заметки: ")
      manager.add_note(title, body)

    elif command == "view":
      created_date = input(
          "Введите дату создания заметок в формате YYYY-MM-DD (опционально): ")
      if created_date:
        try:
          created_date = datetime.strptime(created_date, '%Y-%m-%d').date()
        except ValueError:
          print("Неверный формат даты.")
          continue
      manager.view_notes(created_date)

    elif command == "edit":
      note_id = int(input("Введите id заметки: "))
      title = input("Введите новое название заметки (опционально): ")
      body = input("Введите новый текст заметки (опционально): ")
      manager.edit_note(note_id, title, body)

    elif command == "delete":
      note_id = int(input("Введите id заметки: "))
      manager.delete_note(note_id)

    elif command == "exit":
      print("До свидания!")
      break

    else:
      print("Неверная команда.")