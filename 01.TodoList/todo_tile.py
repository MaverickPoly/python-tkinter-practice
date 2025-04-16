import customtkinter as ctk
from todo import Todo
from settings import *
from database import Database


class TodoTile:

    def __init__(self, root, database: Database, update_todos, todo: Todo, row, col):
        self.root = root
        self.todo = todo
        self.database = database
        self.update_todos = update_todos

        color = "#9c1a00" if not self.todo.completed else "#008a05"
        self.frame = ctk.CTkFrame(self.root, fg_color=color)

        self.title = ctk.CTkLabel(self.frame, text=self.todo.title, font=("Arial", 20))
        self.created_at = ctk.CTkLabel(self.frame, text=self.todo.created_at.split(" ")[0])

        inner_frame = ctk.CTkFrame(self.frame)
        self.delete_btn = ctk.CTkButton(inner_frame, text="🗑️", command=self.delete, bg_color=color, width=30)
        self.update_btn = ctk.CTkButton(inner_frame, text="✅", command=self.update, bg_color=color, width=30)

        self.title.pack()
        self.created_at.pack()
        self.delete_btn.pack(side="left")
        self.update_btn.pack(side="left")
        inner_frame.pack()

        self.frame.grid(row=row, column=col, sticky="nsew", padx=4, pady=4)

    def delete(self):
        self.database.delete_todo(self.todo.id)
        self.update_todos()

    def update(self):
        self.todo.completed = not self.todo.completed
        self.database.update_todo(self.todo.id, self.todo)
        self.update_todos()