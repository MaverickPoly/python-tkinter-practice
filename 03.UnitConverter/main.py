import customtkinter as ctk
from settings import *


class App:
    def __init__(self):
        self.window = ctk.CTk()
        self.window.title(TITLE)
        self.window.geometry(f"{WIDTH}x{HEIGHT}")
        self.window.resizable(False, False)

        # Variables
        self.input_var = ctk.StringVar()
        self.temp_var = ctk.StringVar(value="fah")

        self.init_ui()
        self.window.mainloop()

    def select_checkbox(self, value):
        self.temp_var.set(value)
        if value == "fah":
            self.far_checkbox.select()
            self.cel_checkbox.deselect()
        else:
            self.cel_checkbox.select()
            self.far_checkbox.deselect()

    def convert(self):
        value = self.input_var.get()
        try:
            value = float(value)
        except:
            self.res_text.configure(text="Error")
            return

        if self.temp_var.get() == "fah":
            cel_res = round((value - 32) * 5 / 9, 2)
            self.res_text.configure(text=f"{value}F = {cel_res}C")
        else:
            fah_res = round(value * 9 / 5 + 32, 2)
            self.res_text.configure(text=f"{value}C = {fah_res}F")

    def init_ui(self):
        self.input = ctk.CTkEntry(self.window, textvariable=self.input_var, justify="right", font=ctk.CTkFont(family="Sans-Serif", size=24))
        self.input.pack(fill="x")
        ctk.CTkLabel(self.window, text="From:", font=("Arial", 24)).pack(fill="x")

        self.frame = ctk.CTkFrame(self.window)
        self.far_checkbox = ctk.CTkCheckBox(
            self.frame, 
            text="Fahrenheit", 
            command=lambda: self.select_checkbox("fah")
        )
        self.cel_checkbox = ctk.CTkCheckBox(
            self.frame, 
            text="Celsius", 
            command=lambda: self.select_checkbox("cel")
        )
        self.far_checkbox.select()

        self.far_checkbox.pack(expand=True, fill="x", side="left")
        self.cel_checkbox.pack(expand=True, fill="x", side="left")

        self.frame.pack(fill="x")

        self.button = ctk.CTkButton(self.window, text="Convert", command=self.convert)
        self.button.pack(fill="x")

        self.res_text = ctk.CTkLabel(self.window, text="", font=("Arial", 64))
        self.res_text.pack(expand=True, fill="both")


if __name__ == "__main__":
    App()
