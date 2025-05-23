import requests
from requests.exceptions import HTTPError
import os
from time import sleep


def get_air_quality(city: str, district: str, country: str, wait: int = 10) -> dict:
    data = {}
    try:
        url = "http://api.airvisual.com/v2/city?"
        params = {
            "city": city,
            "state": district,
            "country": country,
            "key": os.environ.get("AIRVISUAL_KEY"),
        }
        response = requests.get(url=url, params=params)
        response.raise_for_status()
        data = response.json()
    except HTTPError as e:
        if e.response.status_code == 429:
            if wait <= 60:
                print(f"Waiting... {wait} seconds")
                sleep(wait)
                get_air_quality(
                    city=city, district=district, country=country, wait=wait + 10
                )
            return data
        else:
            pass
            # print(e.response.status_code)
    except Exception as e:
        print(f"Data not found: {e}")
    return data
