import requests
import os
from typing import Union
from multiprocessing import cpu_count
from concurrent.futures import ThreadPoolExecutor, as_completed


def get_city_temp_c(city: str) -> Union[dict, None]:
    """
    Fetches air quality data for a given city using the WeatherAPI.
    Args:
        city (str): The name of the city to fetch air quality data for.
    Returns:
        dict: A dictionary containing the air quality data for the city.
    Raises:
        requests.RequestException: If there is an error while making the API request.
    """
    try:
        response = requests.get(
            f"http://api.weatherapi.com/v1/current.json?key={os.environ.get("WEATHER_KEY")}&q={city}"
        )
        response.raise_for_status()
        data = response.json()["current"]["temp_c"]
    except Exception as e:
        # print(f"Error fetchin air quality data: data not found for city: {city}")
        return None
    return data


def _paralle_get_city_temp_c(city: str) -> tuple:
    return city, get_city_temp_c(city)


def paralle_get_city_temp_c(cities: Union[list, set]) -> dict:
    result = {}
    with ThreadPoolExecutor(max_workers=cpu_count() * 3) as executor:
        futures = [executor.submit(_paralle_get_city_temp_c, city) for city in cities]
        for future in as_completed(futures):
            city, temp = future.result()
            result[city] = temp
    return result
