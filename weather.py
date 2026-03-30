import os
import requests
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("API_KEY")

city = "Delhi"  # you can change or take input from user
url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}"

response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    print("Weather data fetched successfully!")
    print(data)
elif response.status_code == 404:
    print("City not found.")
elif response.status_code == 429:
    print("Rate limit exceeded, please wait before retrying.")
else:
    print(f"Error: {response.status_code} - {response.reason}")

