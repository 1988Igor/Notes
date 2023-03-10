from datetime import datetime
class Note:
  def __init__(self, id, title, body, created_time=None, updated_time=None):
    self.id = id
    self.title = title
    self.body = body
    self.created_time = created_time if created_time else datetime.now()
    self.updated_time = updated_time if updated_time else datetime.now()

  def to_dict(self):
    return {
      "id": self.id,
      "title": self.title,
      "body": self.body,
      "created_time": self.created_time.isoformat(),
      "updated_time": self.updated_time.isoformat(),
    }

  @staticmethod
  def from_dict(note_dict):
    return Note(
        id=note_dict["id"],
        title=note_dict["title"],
        body=note_dict["body"],
        created_time=datetime.fromisoformat(note_dict["created_time"]),
        updated_time=datetime.fromisoformat(note_dict["updated_time"]),
    )

