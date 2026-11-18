from django.shortcuts import render
from django.http import JsonResponse
import requests


def home(request):
    return render(request, 'weather/index.html')


def get_weather(request):

    url = "https://api.open-meteo.com/v1/forecast"

    params = {
        "latitude": 28.6139,
        "longitude": 77.2090,
        "current": "temperature_2m,relative_humidity_2m,precipitation,rain,weather_code,wind_speed_10m",
        "timezone": "Asia/Kolkata"
    }

    try:
        response = requests.get(url, params=params, timeout=10)
        response.raise_for_status()
        data = response.json()

        return JsonResponse(data)

    except requests.RequestException:
        return JsonResponse(
            {"error": "Unable to fetch weather data. Please try again."},
            status=502
        )