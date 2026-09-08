import json

from weather_service import WeatherServiceError, get_personalized_homepage


try:
    result = get_personalized_homepage("Davangere", "commuter")
    print(json.dumps(result, indent=2))
except WeatherServiceError as error:
    print(f"Weather error: {error}")