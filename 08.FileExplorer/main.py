import customtkinter as ctk
import os
from file_tile import FileTile
from folder_tile import FolderTile
from settings import *
from pyperclip import copy

"""
Simple File Explorer App Made Using Tkinter
"""


class App:
    def __init__(self):
        self.window = ctk.CTk()
        self.window.title(TITLE)
        self.window.geometry(f"{WIDTH}x{HEIGHT}")
        self.window.resizable(False, False)

        # Variables
        self.current_dir = ctk.StringVar(value=r"D:\\")
        # self.current_dir = ctk.StringVar(value=os.getcwd())
        self.items = os.listdir(self.current_dir.get())

        self.build_ui()
        self.window.mainloop()

    def move_to_disk(self, disk_name):
        if disk_name == "C":
            self.current_dir.set("C:\\")
        else:
            self.current_dir.set("D:\\")
        self.items = os.listdir(self.current_dir.get())
        self.list.pack_forget()
        self._build_top()
        self._build_list()

    def open_file(self, event, path, name):
        self.toplevel = ctk.CTkToplevel()
        self.toplevel.title(name)
        filename = os.path.join(path, name)

        size_label = ctk.CTkLabel(self.toplevel, text=f"{round(os.path.getsize(filename) / 1024, 1)}KB", font=("Arial", 32))
        size_label.pack()

        path_label = ctk.CTkLabel(self.toplevel, text=filename, font=("Arial", 18))
        path_label.pack(pady=10)

        copy_path_btn = ctk.CTkButton(self.toplevel, text="Copy Path", command=lambda: copy(filename))
        copy_path_btn.pack(fill="x")

    def open_folder(self, event, path, name):
        self.current_dir.set(os.path.join(path, name))
        self.items = os.listdir(self.current_dir.get())
        self.list.pack_forget()
        self._build_top()
        self._build_list()

    def go_back(self):
        self.current_dir.set(os.path.join("\\".join(self.current_dir.get().split("\\")[:-1])))
        self.items = os.listdir(self.current_dir.get())
        self.list.pack_forget()
        self._build_top()
        self._build_list()

    def _build_top(self):
        if hasattr(self, "top_frame"):
            self.top_frame.pack_forget()
        self.top_frame = ctk.CTkFrame(self.window)

        prev_btn = ctk.CTkButton(self.top_frame, text="Up", command=self.go_back)
        prev_btn.pack(side="left")

        path_label = ctk.CTkLabel(self.top_frame, text=self.current_dir.get())
        path_label.pack(side="left", padx=10)

        c_btn = ctk.CTkButton(self.top_frame, text="C Drive", command=lambda: self.move_to_disk("C"))
        c_btn.pack(side="right")

        d_btn = ctk.CTkButton(self.top_frame, text="D Drive", command=lambda: self.move_to_disk("D"))
        d_btn.pack(side="right")

        self.top_frame.pack(fill="x", pady=10, padx=10)

    def _build_list(self):
        self.list = ctk.CTkScrollableFrame(self.window)

        for i in range(COLUMNS):
            self.list.columnconfigure(i, weight=1)

        for i, item in enumerate(self.items):
            row = i // COLUMNS
            col = i % COLUMNS

            item_path = os.path.join(self.current_dir.get(), item)
            if os.path.isfile(item_path):
                FileTile(item, self.current_dir.get(), self.open_file, self.list, row, col)
            elif os.path.isdir(item_path):
                FolderTile(item, self.current_dir.get(), self.open_folder, self.list, row, col)

        self.list.pack(expand=True, fill="both")

    def build_ui(self):
        self._build_top()    
        self._build_list()    


if __name__ == "__main__":
    App()
