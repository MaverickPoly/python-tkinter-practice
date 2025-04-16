import customtkinter as ctk
from settings import *
from input import Input
import os


class App:
    def __init__(self):
        self.window = ctk.CTk()
        self.window.geometry(f"{WIDTH}x{HEIGHT}")
        self.window.title(TITLE)
        self.window.wm_iconbitmap(os.path.join("04.Calculator", "image1.ico"))
        self.window.resizable(False, False)

        self.init_ui()

        self.window.mainloop()

    def handle_click(self, btn_data: ButtonData):
        if btn_data.text == "C":
            self.input.clear_input()
        elif btn_data.text == "D":
            self.input.delete_char()
        elif btn_data.text == "%":
            self.input.percent()
        elif btn_data.text == "✕":
            self.input.append_text("*")
        elif btn_data.text == "÷":
            self.input.append_text("/")
        elif btn_data.text == "=":
            self.input.calculate()
        else:
            self.input.append_text(btn_data.text)

    def _build_input(self):
        self.input = Input(self.window)

    def _build_buttons(self):
        self.frame = ctk.CTkFrame(self.window)
        for btn_data in BUTTONS:
            button = ctk.CTkButton(self.frame, text=btn_data.text, width=BTN_WIDTH, height=BTN_HEIGHT, fg_color=btn_data.bg_color, text_color=btn_data.text_color, corner_radius=0, font=("Arial", 28), hover_color=btn_data.hover_color, command=lambda btn_data=btn_data: self.handle_click(btn_data))
            button.grid(row=btn_data.row, column=btn_data.col, columnspan=btn_data.span, sticky="nsew")

        self.frame.pack(expand=True, fill="both")

    def init_ui(self):
        self._build_input()
        self._build_buttons()


if __name__ == "__main__":
    App()
