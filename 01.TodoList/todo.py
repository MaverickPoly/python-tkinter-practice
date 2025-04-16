class Todo:
    def __init__(self, title: str, completed: bool, created_at, id=None):
        self.title = title
        self.completed = completed
        self.id = id
        self.created_at = created_at

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "completed": int(self.completed),
            "created_at": str(self.created_at)
        }

    @classmethod
    def from_dict(cls, d):
        print("D:")
        print(d)
        return Todo(
            title=d[1], 
            completed=bool(d[2]), 
            created_at=d[3],
            id=d[0]
        )
