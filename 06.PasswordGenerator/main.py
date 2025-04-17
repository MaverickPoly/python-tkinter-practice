import customtkinter as ctk
from tkinter import messagebox
import string
from pyperclip import copy
from random import choice


# Constants
TITLE = "Password Generator"
WIDTH, HEIGHT = 500, 500


class App:
    def __init__(self):
        self.window = ctk.CTk()
        self.window.title(TITLE)
        self.window.geometry(f"{WIDTH}x{HEIGHT}")

        # Variables
        self.password_generated = ctk.BooleanVar(value=False)
        self.number_var = ctk.StringVar(value="")

        self.include_numbers = ctk.BooleanVar(value=False)
        self.include_lowercase = ctk.BooleanVar(value=False)
        self.include_uppercase = ctk.BooleanVar(value=False)
        self.include_punctuation = ctk.BooleanVar(value=False)

        self.password = ctk.StringVar(value="")

        self.build_ui()
        self.window.mainloop()

    def on_checkbox_change(self, value):
        if value == "Numbers":
            self.include_numbers.set(not self.include_numbers.get())
        elif value == "Lowercase":
            self.include_lowercase.set(not self.include_lowercase.get())
        elif value == "Uppercase":
            self.include_uppercase.set(not self.include_uppercase.get())
        elif value == "Punctuation":
            self.include_punctuation.set(not self.include_punctuation.get())

    def generate_password(self):
        all_str = ""
        if self.include_numbers.get():
            all_str += string.digits
        if self.include_lowercase.get():
            all_str += string.ascii_lowercase
        if self.include_uppercase.get():
            all_str += string.ascii_uppercase
        if self.include_punctuation.get():
            all_str += string.punctuation

        if not all_str:
            messagebox.showwarning("No option selected", "Please select at least one component what password consists of!")
            return
        
        try:
            number = int(self.number_var.get())
        except:
            messagebox.showerror("Invalid number", "Please enter a valid number for the length of the password!")
            return
        
        all_str = list(all_str)
        password = "".join([choice(all_str) for _ in range(number)])
        self.password.set(password)
        self.password_label.configure(text=password)
        
    def copy_password(self):
        copy(self.password.get())
        messagebox.showinfo("Copied", "Password copied to clipboard!")

    def build_ui(self):
        ctk.CTkLabel(self.window, text="Password Generator", font=("Arial", 42)).pack(fill="x", pady=24)

        ctk.CTkLabel(self.window, text="Number of Digits:", font=("Arial", 24)).pack(fill="x", pady=10)
        self.number_input = ctk.CTkEntry(self.window, textvariable=self.number_var)
        self.number_input.pack(fill="x", pady=14, padx=20)

        frame = ctk.CTkFrame(self.window)
        self.number_chb = ctk.CTkCheckBox(frame, text="Numbers", command=lambda: self.on_checkbox_change("Numbers"), font=("Arial", 20))
        self.lowercase_chb = ctk.CTkCheckBox(frame, text="Lowercase", command=lambda: self.on_checkbox_change("Lowercase"), font=("Arial", 20))
        self.uppercase_chb = ctk.CTkCheckBox(frame, text="Uppercase", command=lambda: self.on_checkbox_change("Uppercase"), font=("Arial", 20))
        self.punctuation_chb = ctk.CTkCheckBox(frame, text="Punctuation", command=lambda: self.on_checkbox_change("Punctuation"), font=("Arial", 20))

        self.number_chb.pack(pady=5)
        self.lowercase_chb.pack(pady=5)
        self.uppercase_chb.pack(pady=5)
        self.punctuation_chb.pack(pady=5)

        frame.pack(fill="x", padx=12)

        self.generate_btn = ctk.CTkButton(self.window, text="Generate", command=self.generate_password)
        self.generate_btn.pack(fill="x", pady=14, padx=14)

        self.password_label = ctk.CTkLabel(self.window, text="", font=("Arial", 20))
        self.password_label.pack(fill="x", pady=10)

        self.copy_btn = ctk.CTkButton(self.window, text="Copy", command=self.copy_password)
        self.copy_btn.pack(padx=20, pady=10)


if __name__ == "__main__":
    App()
