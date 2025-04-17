import customtkinter as ctk
from tkinter.colorchooser import askcolor


"""
A simple Drawing App
"""

class DrawingApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Drawing App")
        self.root.geometry("900x700")

        self.brush_size = 3 
        self.color = "black"

        self.last_x, self.last_y = None, None

        self.build_ui()

    def build_ui(self):
        top_frame = ctk.CTkFrame(self.root)
        top_frame.pack(fill="x", padx=10, pady=5)

        clear_btn = ctk.CTkButton(top_frame, text="Clear", command=self.clear_canvas)
        clear_btn.pack(side="left", padx=16)

        brush_label = ctk.CTkLabel(top_frame, text="Brush Size", font=("Arial", 18))
        brush_label.pack(side="left", padx=6)

        self.brush_slider = ctk.CTkSlider(top_frame, from_=1, to=30, number_of_steps=19, command=self.change_brush_size, width=300)
        self.brush_slider.pack(side="left", padx=10)
        self.brush_slider.set(self.brush_size)

        color_btn = ctk.CTkButton(top_frame, text="Choose color", command=self.choose_color)
        color_btn.pack(side="left", padx=16)

        self.canvas = ctk.CTkCanvas(self.root, bg="white", bd=0, highlightthickness=0)
        self.canvas.pack(expand=True, fill="both")

        self.canvas.bind("<Button-1>", self.start_drawing)
        self.canvas.bind("<B1-Motion>", self.draw)

    def start_drawing(self, event):
        self.last_x, self.last_y = event.x, event.y 

    def draw(self, event):
        x, y = event.x, event.y
        if self.last_x and self.last_y:
            self.canvas.create_line(self.last_x, self.last_y, x, y, fill=self.color, width=self.brush_size, capstyle="round", smooth=True)
        self.last_x, self.last_y = x, y

    def clear_canvas(self):
        self.canvas.delete("all")

    def choose_color(self):
        color = askcolor()[1]
        if color:
            self.color = color

    def change_brush_size(self, value):
        self.brush_size = int(float(value))


if __name__ == "__main__":
    root = ctk.CTk()
    ctk.set_appearance_mode("Light")
    ctk.set_default_color_theme("green")
    app = DrawingApp(root)

    root.mainloop()
