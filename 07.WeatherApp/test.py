import requests
from main import API_KEY


res = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q=Tashkent&appid={API_KEY}&units=metric")

if res.ok:
    print(res.json())
