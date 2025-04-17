import customtkinter as ctk
import requests
from io import BytesIO
from PIL import Image

# Settings
TITLE = "Weather App"
WIDTH, HEIGHT = 800, 650
API_KEY = "ed2828e59ddf36874f1950c82bf3f254" # Put Your own OpenWeatherMap API KEY Here!


class WeatherData:
    def __init__(self, city, title, icon, temp, pressure, humidity):
        self.city = city
        self.title = title
        self.icon = icon
        self.temp = temp
        self.pressure = pressure
        self.humidity = humidity


class WeatherApp:
    def __init__(self):
        self.window = ctk.CTk()
        self.window.title(TITLE)
        self.window.geometry(f"{WIDTH}x{HEIGHT}")

        self.input_var = ctk.StringVar(value="")
        self.weather_data = None

        self.ui()
        self.window.mainloop()

    def fetch_weather(self):
        res = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={self.input_var.get()}&appid={API_KEY}&units=metric")
        if res.ok:
            data = res.json()
            city = data["name"]
            title = data["weather"][0]["main"]
            icon = data["weather"][0]["icon"]
            temp = data["main"]["temp"]
            pressure = data["main"]["pressure"]
            humidity = data["main"]["humidity"]
            self.weather_data = WeatherData(city, title, icon, temp, pressure, humidity)
            self.display_weather()

    def display_weather(self):
        frame = ctk.CTkFrame(self.window)
        # ctk.CTkLabel(frame, text=self.weather_data.city, font=("Arial", 20)).pack(fill="x")

        row1 = ctk.CTkFrame(frame)
        ctk.CTkLabel(row1, text=self.weather_data.city, font=("Arial", 28)).pack(expand=True, side="left", fill="x", pady=10)
        ctk.CTkLabel(row1, text=self.weather_data.title, font=("Arial", 24)).pack(expand=True, side="left", fill="x", pady=10)
        row1.pack(fill="x", padx=80)

        # Fetch and Show Icon
        icon_url = f"https://openweathermap.org/img/wn/{self.weather_data.icon}@2x.png"
        res = requests.get(icon_url)
        img_data = BytesIO(res.content)  
        image = Image.open(img_data)
        ctk_img = ctk.CTkImage(dark_image=image, light_image=image, size=(400, 400))
        img_widget = ctk.CTkLabel(frame, text="", image=ctk_img)
        img_widget.pack(expand=True, fill="both")
        
        ctk.CTkLabel(frame, text=f"{self.weather_data.temp}°C", font=("Sans-Serif", 40)).pack(fill="x", pady=10)

        row2 = ctk.CTkFrame(frame)
        ctk.CTkLabel(row2, text=f"Pressure: {self.weather_data.pressure}", font=("Arial", 24)).pack(expand=True, fill="x", side="left", pady=10)
        ctk.CTkLabel(row2, text=f"Humidity: {self.weather_data.humidity}", font=("Arial", 24)).pack(expand=True, fill="x", side="left", pady=10)
        row2.pack(fill="x", padx=80)

        frame.pack(expand=True, fill="both", padx=20)

    def ui(self):
        # Form
        form_frame = ctk.CTkFrame(self.window)
        self.input = ctk.CTkEntry(form_frame, justify="right", textvariable=self.input_var, font=("Arial", 24))
        self.fetch_btn = ctk.CTkButton(form_frame, text="Fetch", command=self.fetch_weather, font=("Arial", 20))

        self.input.pack(expand=True, fill="x", side="left", padx=7)
        self.fetch_btn.pack(fill="x", side="left")
        form_frame.pack(fill="x", padx=10, pady=8)
        
        # Weather Data Display
        # if self.weather_data:
        #     self.display_weather()
        


def main():
    app = WeatherApp()


if __name__ == "__main__":
    main()
