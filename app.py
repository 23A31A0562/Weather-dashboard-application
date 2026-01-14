import streamlit as st
from weather_api import WeatherAPI
from weather_parser import parse_current_weather, parse_forecast

st.set_page_config(page_title="Weather Dashboard", page_icon="🌦️")

st.title("🌤️ Weather Dashboard")
st.write("Get current weather and 5-day forecast for any city worldwide")

city = st.text_input("Enter city name", placeholder="e.g. Visakhapatnam, IN")

if st.button("Get Weather"):
    if not city.strip():
        st.error("Please enter a city name")
    else:
        api = WeatherAPI()
        try:
            current = api.get_current_weather(city)
            forecast = api.get_forecast(city)

            current_data = parse_current_weather(current)
            forecast_data = parse_forecast(forecast)

            st.subheader(f"📍 {current_data['city']}, {current_data['country']}")
            st.metric("🌡️ Temperature", f"{current_data['temperature']} °C")
            st.write(f"**Condition:** {current_data['condition']}")
            st.write(f"**Humidity:** {current_data['humidity']}%")
            st.write(f"**Wind Speed:** {current_data['wind_speed']} m/s")
            st.write(f"**Pressure:** {current_data['pressure']} hPa")

            st.subheader("📅 5-Day Forecast")
            for day in forecast_data:
                st.write(
                    f"📆 {day['date']} | {day['condition']} | {day['min']}°C - {day['max']}°C"
                )

        except Exception as e:
            st.error(str(e))
