import requests
import time
import json
from pathlib import Path
from config import API_KEY, BASE_URL


class WeatherAPI:
    def __init__(self):
        self.cache_dir = Path("weather_app/data/cache")
        self.cache_dir.mkdir(parents=True, exist_ok=True)
        self.cache_duration = 600  # 10 minutes

    def _cache_path(self, city, endpoint):
        safe_city = city.replace(" ", "_").lower()
        return self.cache_dir / f"{safe_city}_{endpoint}.json"

    def _is_cache_valid(self, path):
        return path.exists() and (time.time() - path.stat().st_mtime) < self.cache_duration

    def _fetch(self, endpoint, params):
        params["appid"] = API_KEY
        params["units"] = "metric"

        try:
            response = requests.get(
                f"{BASE_URL}/{endpoint}",
                params=params,
                timeout=10
            )
            response.raise_for_status()
            return response.json()

        except requests.exceptions.Timeout:
            raise Exception("Request timed out")

        except requests.exceptions.ConnectionError:
            raise Exception("Network error")

        except requests.exceptions.HTTPError as e:
            raise Exception(f"API Error: {e}")

    def get_current_weather(self, city):
        cache = self._cache_path(city, "current")

        if self._is_cache_valid(cache):
            with open(cache, "r") as f:
                return json.load(f)

        data = self._fetch("weather", {"q": city})
        with open(cache, "w") as f:
            json.dump(data, f, indent=2)
        return data

    def get_forecast(self, city):
        cache = self._cache_path(city, "forecast")

        if self._is_cache_valid(cache):
            with open(cache, "r") as f:
                return json.load(f)

        data = self._fetch("forecast", {"q": city})
        with open(cache, "w") as f:
            json.dump(data, f, indent=2)
        return data
