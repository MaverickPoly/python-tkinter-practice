import sqlite3
import os
from todo import Todo

"""
- Structure:
Title, Completed, Id, Created At
"""


class Database:
    def __init__(self):
        self.conn = sqlite3.connect(os.path.join("01.TodoList", "todo.db"))
        self.cur = self.conn.cursor()
        self.cur.execute("""
            CREATE TABLE IF NOT EXISTS todo(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                completed INTEGER,
                created_at TEXT
            )
        """)

    def add_todo(self, todo: Todo):
        self.cur.execute("""
            INSERT INTO todo (title, completed, created_at) VALUES (?, ?, ?)
        """, (todo.title, int(todo.completed), str(todo.created_at)))
        self.conn.commit()

    def fetch_todos(self) -> list[Todo]:
        self.cur.execute("SELECT * FROM todo")
        todos = self.cur.fetchall()
        model_todos: list[Todo] = []
        for todo in todos:
            model_todos.append(Todo.from_dict(todo))
        return model_todos

    def delete_todo(self, id):
        self.cur.execute("DELETE FROM todo WHERE id=?", (id,))
        self.conn.commit()

    def update_todo(self, id, todo: Todo):
        self.cur.execute("""
            UPDATE todo SET title=?, completed=? WHERE id=?
        """, (todo.title, todo.completed, todo.id))

    def __del__(self):
        print("Deleting")
