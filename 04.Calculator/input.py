import customtkinter as ctk
from settings import *

class Input:
    def __init__(self, window):
        self.var = ctk.StringVar()

        self.window = window
        self.input = ctk.CTkEntry(self.window, height=INPUT_HEIGHT, textvariable=self.var, corner_radius=0, border_width=0, placeholder_text="Enter...", font=("Arial", 45), justify="right")

        self.input.pack(expand=True, fill="both")

    def append_text(self, text):
        self.var.set(self.var.get() + text)

    def calculate(self):
        try:
            res = eval(self.var.get())
            self.var.set(res)
        except ZeroDivisionError:
            self.var.set("Zero division!")
        except:
            self.var.set("Error")

    def clear_input(self):
        self.var.set("")

    def delete_char(self):
        self.var.set(self.var.get()[:-1])

    def percent(self):
        try:
            res = float(eval(self.var.get())) / 100
            self.var.set(str(res))
        except ZeroDivisionError:
            self.var.set("Zero division!")
        except:
            self.var.set("Error")
