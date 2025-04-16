import customtkinter as ctk
from settings import *
from database import Database
from datetime import datetime
from todo import Todo
from tkinter import messagebox
from todo_tile import TodoTile


class App:
    def __init__(self):
        self.window = ctk.CTk()
        self.window.title(TITLE)
        self.window.geometry(f"{WIDTH}x{HEIGHT}")

        self.database = Database()

        # Variables
        self.input_var = ctk.StringVar()

        self.init_ui()

        self.window.mainloop()

    def add_todo(self):
        if self.input_var.get():
            todo = Todo(title=self.input_var.get(), completed=False, created_at=str(datetime.now()))
            self.database.add_todo(todo)
            self.input_var.set("")
            self._build_list()
        else:
            messagebox.showwarning("Invalid input!", "The title of the todo cannot be empty!")

    def _build_form(self):
        frame = ctk.CTkFrame(self.window)
        self.input = ctk.CTkEntry(frame, textvariable=self.input_var)
        self.add_button = ctk.CTkButton(frame, text="Add", command=self.add_todo, font=("Arial", 22))

        self.input.pack(expand=True, fill="both", side="left")
        self.add_button.pack(fill="both", padx=10)
        frame.pack(fill="x", padx=20, pady=10)

    def _build_list(self):
        if hasattr(self, "todo_frame"):
            self.todo_frame.pack_forget()

        self.todo_frame = ctk.CTkScrollableFrame(self.window)

        # Grid will have 4 rows
        todos = self.database.fetch_todos()
        for i in range(4):
            self.todo_frame.columnconfigure(i, weight=1)

        row_count = (len(todos) // 4) + (1 if len(todos) % 4 > 0 else 0)
        for i in range(row_count):
            self.todo_frame.rowconfigure(i, weight=1)

        for i, todo in enumerate(todos):
            row = i // 4
            col = i % 4
            TodoTile(self.todo_frame, self.database, self._build_list, todo, row, col)

        self.todo_frame.pack(expand=True, fill="both")

    def init_ui(self):
        self._build_form()
        self._build_list()


if __name__ == "__main__":
    App()
