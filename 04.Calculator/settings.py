class ButtonData:
    def __init__(self, text, text_color, bg_color, span, row, col, hover_color):
        self.text = text
        self.text_color = text_color
        self.bg_color = bg_color
        self.span = span
        self.row = row
        self.col = col
        self.hover_color = hover_color

# Window
WIDTH, HEIGHT = 400, 620
TITLE = "Calcly"

# Colors
WHITE = "#fff"
DARK_GRAY = "#333"
GRAY = "#555"
RED = "#d00"
ORANGE = "#fa0"

DARK_GRAY_HOVER = "#444"
GRAY_HOVER = "#666"
LIGHT_RED = "#f00"
LIGHT_ORANGE = "#fb1"

# Sizes
BTN_WIDTH, BTN_HEIGHT = 100, 100
INPUT_HEIGHT = 120

# Buttons Data
BUTTONS = [
    ButtonData(text="C", text_color=WHITE, bg_color=RED, span=1, row=0, col=0, hover_color=LIGHT_RED),
    ButtonData(text="D", text_color=WHITE, bg_color=GRAY, span=1, row=0, col=1, hover_color=GRAY_HOVER),
    ButtonData(text="%", text_color=WHITE, bg_color=GRAY, span=1, row=0, col=2, hover_color=GRAY_HOVER),
    ButtonData(text="✕", text_color=WHITE, bg_color=GRAY, span=1, row=0, col=3, hover_color=GRAY_HOVER),
    
    ButtonData(text="7", text_color=WHITE, bg_color=DARK_GRAY, span=1, row=1, col=0, hover_color=DARK_GRAY_HOVER),
    ButtonData(text="8", text_color=WHITE, bg_color=DARK_GRAY, span=1, row=1, col=1, hover_color=DARK_GRAY_HOVER),
    ButtonData(text="9", text_color=WHITE, bg_color=DARK_GRAY, span=1, row=1, col=2, hover_color=DARK_GRAY_HOVER),
    ButtonData(text="÷", text_color=WHITE, bg_color=GRAY, span=1, row=1, col=3, hover_color=GRAY_HOVER),
    
    ButtonData(text="4", text_color=WHITE, bg_color=DARK_GRAY, span=1, row=2, col=0, hover_color=DARK_GRAY_HOVER),
    ButtonData(text="5", text_color=WHITE, bg_color=DARK_GRAY, span=1, row=2, col=1, hover_color=DARK_GRAY_HOVER),
    ButtonData(text="6", text_color=WHITE, bg_color=DARK_GRAY, span=1, row=2, col=2, hover_color=DARK_GRAY_HOVER),
    ButtonData(text="+", text_color=WHITE, bg_color=GRAY, span=1, row=2, col=3, hover_color=GRAY_HOVER),
    
    ButtonData(text="1", text_color=WHITE, bg_color=DARK_GRAY, span=1, row=3, col=0, hover_color=DARK_GRAY_HOVER),
    ButtonData(text="2", text_color=WHITE, bg_color=DARK_GRAY, span=1, row=3, col=1, hover_color=DARK_GRAY_HOVER),
    ButtonData(text="3", text_color=WHITE, bg_color=DARK_GRAY, span=1, row=3, col=2, hover_color=DARK_GRAY_HOVER),
    ButtonData(text="-", text_color=WHITE, bg_color=GRAY, span=1, row=3, col=3, hover_color=GRAY_HOVER),
    
    ButtonData(text="0", text_color=WHITE, bg_color=DARK_GRAY, span=2, row=4, col=0, hover_color=DARK_GRAY_HOVER),
    ButtonData(text=".", text_color=WHITE, bg_color=GRAY, span=1, row=4, col=2, hover_color=GRAY_HOVER),
    ButtonData(text="=", text_color=WHITE, bg_color=ORANGE, span=1, row=4, col=3, hover_color=LIGHT_ORANGE),
]
