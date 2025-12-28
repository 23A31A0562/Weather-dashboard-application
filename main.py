import requests
from weather_api import WeatherAPI
from weather_parser import parse_current_weather, parse_forecast
from weather_display import display_current, display_forecast

def main():
    city = input("Enter city name: ").strip()

    api = WeatherAPI()

    try:
        current = api.get_current_weather(city)
        forecast = api.get_forecast(city)

        display_current(parse_current_weather(current))
        display_forecast(parse_forecast(forecast))

    except requests.exceptions.HTTPError:
        print("❌ City not found. Please check the spelling or try adding country code (e.g., Visakhapatnam,IN)")

    except Exception as e:
        print("❌ Something went wrong:", e)


if __name__ == "__main__":
    main()
