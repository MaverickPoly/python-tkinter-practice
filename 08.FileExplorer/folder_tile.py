import customtkinter as ctk
from PIL import Image
import os
from settings import *


class FolderTile:
    def __init__(self, name, path, command, master, row, col):
        self.master = master
        self.command = command

        self.frame = ctk.CTkFrame(self.master, width=FOLDER_IMG_W)
        
        img = Image.open(os.path.join(os.getcwd(), "08.FileExplorer", "images", "folder.png"))
        image = ctk.CTkImage(light_image=img, dark_image=img, size=(FOLDER_IMG_W, FOLDER_IMG_H))

        image_label = ctk.CTkLabel(self.frame, text="", image=image)
        image_label.pack(expand=True, fill="x")

        text = ctk.CTkLabel(self.frame, text=name[:18], font=("Arial", 20))
        text.pack(fill="x")

        self.frame.grid(row=row, column=col, sticky="nsew")

        image_label.bind("<Button-1>", lambda event: self.command(event, path, name))
        text.bind("<Button-1>", lambda event: self.command(event, path, name))
        self.frame.bind("<Button-1>", lambda event: self.command(event, path, name))
