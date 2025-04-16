import customtkinter as ctk
from settings import *
from tkinter import filedialog
from PIL import Image, ImageTk


class App:
    def __init__(self):
        self.window = ctk.CTk()
        self.window.title(TITLE)
        self.window.geometry(f"{WIDTH}x{HEIGHT}")

        # Variables
        self.image_open = ctk.BooleanVar(value=False)

        self.build_ui()

        self.window.mainloop()

    def open_image(self):
        filepath = filedialog.askopenfilename(title="Select an Image File", filetypes=[("Image Files", "*.jpg *.png *.jpeg *.bmp *.gif")])
        if not filepath:
            return
        print(filepath)
        self.image = Image.open(filepath)
        # self.image.resize()

        self.open_button.pack_forget()
        self._build_image()

        self.image_open.set(True)

    def close_image(self):
        self.image_widget.pack_forget()
        self.close_button.place_forget()
        self._build_handles()
        self.image_open.set(False)

    def _build_image(self):
        img = ctk.CTkImage(dark_image=self.image, light_image=self.image, size=(self.window.winfo_width(), self.window.winfo_height()))
        self.image_widget = ctk.CTkLabel(self.window, text="", image=img, width=self.window.winfo_width(), height=self.window.winfo_height())
        self.image_widget.pack(expand=True, fill="both")

        self.close_button = ctk.CTkButton(self.window, text="Close", bg_color="transparent", command=self.close_image, width=100)
        print(self.window.winfo_width())
        self.close_button.place(rely=0, relx=0)

    def _build_handles(self):
        self.open_button = ctk.CTkButton(self.window, text="Open Image", command=self.open_image)
        self.open_button.pack(expand=True)

    def build_ui(self):
        if self.image_open.get():
            self._build_image()
        else:
            self._build_handles()


if __name__ == "__main__":
    App()
