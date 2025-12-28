# Weather Dashboard Application

This is a command-line based Weather Dashboard Application built using Python.  
The application fetches real-time weather data and a 5-day forecast for any city in the world using the OpenWeatherMap API.

The main goal of this project is to understand API integration, data handling, caching, and clean project structuring in Python.

---

## Tech Stack

- Python 3.13  
- OpenWeatherMap API  
- requests  
- python-dotenv  
- colorama  

---

## Project Structure

Weather-Dashboard-Application/
│
├── weather_app/
│   ├── __init__.py
│   ├── config.py
│   ├── main.py
│   ├── weather_api.py
│   ├── weather_parser.py
│   ├── weather_display.py
│   │
│   ├── data/
│   │   └── cache/
│   │
│   └── tests/
│       └── __init__.py
│
├── venv/
├── .env
├── .gitignore
├── requirements.txt
└── README.md

---

## Features

- Fetches current weather for any city worldwide  
- Displays 5-day weather forecast  
- Shows temperature, feels-like temperature, humidity, wind speed, and pressure  
- Uses API response caching to reduce repeated API calls  
- Secure handling of API key using environment variables  
- Clean and modular Python code  

---

## Environment Setup

This project uses environment variables to store the API key securely.

Create a `.env` file in the root directory and add:

OPENWEATHER_API_KEY=your_openweathermap_api_key_here

Do not upload your `.env` file to GitHub.

---

## How to Run the Project

1. Clone the repository  
   git clone https://github.com/your-username/weather-dashboard-application.git

2. Navigate to the project folder  
   cd Weather-Dashboard-Application

3. Create and activate virtual environment  
   python -m venv venv  
   .\venv\Scripts\activate

4. Install dependencies  
   pip install -r requirements.txt

5. Run the application  
   python weather_app/main.py

6. Enter any city name when prompted.

---

## Sample Output

CURRENT WEATHER  
Location: London, GB  
Temperature: 7.25°C (Feels like 4.56°C)  
Condition: Overcast Clouds  
Humidity: 75%  
Wind Speed: 4.12 m/s  
Pressure: 1031 hPa  

5-DAY FORECAST  
Mon: 9°C / 5°C  
Tue: 10°C / 6°C  
Wed: 11°C / 7°C  
Thu: 12°C / 8°C  
Fri: 13°C / 9°C  

---

## What I Learned

- How to work with third-party APIs in Python  
- Making HTTP requests and handling API responses  
- Parsing and formatting JSON data  
- Implementing caching for better performance  
- Using environment variables for secure configuration  
- Structuring a Python project in a professional way  
- Working with virtual environments  

---

## Notes
- If a city is not found, users are advised to check spelling or include the country code (e.g., Visakhapatnam, IN).
- The application works for any city supported by OpenWeatherMap.
- Cached data is stored temporarily to avoid unnecessary API calls.
- This project is intended for learning and internship submission purposes.

---

## Author

Bhargav  
Python Developer Intern
