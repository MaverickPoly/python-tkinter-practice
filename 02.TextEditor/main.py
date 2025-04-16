import customtkinter as ctk
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog, messagebox
import os
import pyperclip


"""
Textly - Simple NotePad Clone App
"""


class App:
    def __init__(self):
        ctk.set_appearance_mode("Light")
        ctk.set_default_color_theme("blue")

        self.window = ctk.CTk()
        self.window.title("Textly")
        self.window.geometry("800x600")

        # Variables
        self.input_var = ctk.StringVar()
        self.file_name_var = ctk.StringVar()
        self.file_name_var.set("")

        self.build_widgets()

        self.window.mainloop()

    def open_file(self):
        res = filedialog.askopenfilename(title="Open file.")
        if not res:
            return
        self.file_name_var.set(res)
        self.update_filename_display()
        with open(res, "r") as file:
            self.input_var.set(file.read())
            self.text_field.delete("1.0", ctk.END)
            self.text_field.insert(ctk.END, self.input_var.get())

    def save_file(self):
        if self.file_name_var.get():
            with open(self.file_name_var.get(), "w") as file:
                file.write(self.input_var.get())
        else:
            file = filedialog.askopenfile("w", title="Choose a file to save text.")
            file.write(self.input_var.get())
            file.close()

    def close_file(self):
        if self.file_name_var.get():
            self.save_file() # Save file when closing
        self.file_name_var.set("")
        self.input_var.set("")
        self.update_filename_display()
        self.text_field.delete("1.0", ctk.END)

    def on_paste(self):
        text = pyperclip.paste()
        self.text_field.insert("insert", text)
        self.input_var.set(self.text_field.get("1.0", ctk.END))

    def on_cut(self):
        try:
            selection = self.text_field.get("sel.first", "sel.last")
            if selection:
                print(f"Selection: {selection}")
                pyperclip.copy(selection)
                self.text_field.delete("sel.first", "sel.last")
                self.input_var.set(self.text_field.get("1.0", ctk.END))
        except:
            pass

    def on_copy(self):
        pyperclip.copy(self.input_var.get())

    def on_help(self):
        messagebox.showinfo("Info", "Textly is a simple Notepad clone that was implemented in Tkinter library!")

    def build_menu(self):
        self.menu_bar = tk.Menu(self.window)
        self.window.config(menu=self.menu_bar)

        # File Menu
        file_menu = tk.Menu(self.menu_bar, tearoff=0)
        file_menu.add_command(label="Open", command=self.open_file)
        file_menu.add_command(label="Save", command=self.save_file)
        file_menu.add_command(label="Close", command=self.close_file)
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=self.window.destroy)
        self.menu_bar.add_cascade(label="File", menu=file_menu)
        
        # Edit Menu
        edit_menu = tk.Menu(self.menu_bar, tearoff=0)
        edit_menu.add_command(label="Paste", command=self.on_paste)
        edit_menu.add_command(label="Cut", command=self.on_cut)
        edit_menu.add_command(label="Copy", command=self.on_copy)
        self.menu_bar.add_cascade(label="File", menu=edit_menu)

        # Help Menu
        help_menu = tk.Menu(self.menu_bar, tearoff=0)
        help_menu.add_command(label="About", command=self.on_help)
        self.menu_bar.add_cascade(label="Help", menu=help_menu)

        self.filename_display_index = self.menu_bar.index("end") + 1
        self.menu_bar.add_command(label=" ")
        
    def create_text_field(self):
        self.text_field = ctk.CTkTextbox(self.window, font=("Arial", 18))
        self.text_field.bind("<KeyRelease>", self.on_text_change)
        self.text_field.pack(expand=True, fill="both")

    def on_text_change(self, event):
        current_text = self.text_field.get("1.0", "end-1c")
        self.input_var.set(current_text)

    def update_filename_display(self):
        if hasattr(self, 'menu_bar'):
            if self.file_name_var.get() and self.file_name_var.get() != "None":
                display_name = os.path.basename(self.file_name_var.get())
            else:
                display_name = " "
                
            try:
                print(self.file_name_var.get())
                self.menu_bar.entryconfig(self.filename_display_index, label=display_name)
            except:
                self.menu_bar.add_command(label=display_name, state="disabled", font=("Arial", 10, "italic"))

    def build_widgets(self):
        self.build_menu()
        self.create_text_field()


if __name__ == "__main__":
    App()
