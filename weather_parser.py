from datetime import datetime

def parse_current_weather(data):
    return {
        "city": data["name"],
        "country": data["sys"]["country"],
        "temperature": data["main"]["temp"],
        "feels_like": data["main"]["feels_like"],
        "humidity": data["main"]["humidity"],
        "pressure": data["main"]["pressure"],
        "condition": data["weather"][0]["description"].title(),
        "wind_speed": data["wind"]["speed"]
    }

def parse_forecast(data):
    forecast = []
    seen_dates = set()

    for item in data["list"]:
        date = item["dt_txt"].split(" ")[0]
        if date not in seen_dates:
            seen_dates.add(date)
            forecast.append({
                "date": date,
                "min": item["main"]["temp_min"],
                "max": item["main"]["temp_max"],
                "condition": item["weather"][0]["description"].title()
            })

        if len(forecast) == 5:
            break

    return forecast
