from colorama import Fore, Style, init

init(autoreset=True)

def display_current(weather):
    print(Fore.CYAN + "\n🌤️  CURRENT WEATHER")
    print("────────────────────")
    print(f"📍 Location: {weather['city']}, {weather['country']}")
    print(f"🌡️ Temperature: {weather['temperature']}°C (Feels like {weather['feels_like']}°C)")
    print(f"☁ Condition: {weather['condition']}")
    print(f"💧 Humidity: {weather['humidity']}%")
    print(f"🌬️ Wind Speed: {weather['wind_speed']} m/s")
    print(f"🔽 Pressure: {weather['pressure']} hPa")

def display_forecast(forecast):
    print(Fore.YELLOW + "\n📅 5-DAY FORECAST")
    print("────────────────────")
    for day in forecast:
        print(f"{day['date']} | {day['condition']} | {day['min']}°C - {day['max']}°C")
