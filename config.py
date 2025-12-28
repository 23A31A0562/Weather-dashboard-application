import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("OPENWEATHER_API_KEY")
BASE_URL = "https://api.openweathermap.org/data/2.5"

if not API_KEY:
    raise ValueError("OPENWEATHER_API_KEY not found in .env file")
