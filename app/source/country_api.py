import requests
from multiprocessing import cpu_count
from concurrent.futures import ThreadPoolExecutor, as_completed


def get_country_info(country: str) -> dict:
    try:
        response = requests.get(
            f"https://restcountries.com/v3.1/name/{country}?fields=name,population,continents"
        )
        response.raise_for_status()
        data = {}
        for value in response.json():
            data[country] = {
                "population": value["population"],
                "continents": value["continents"][0],
            }
    except Exception as e:
        # print(f"{country}: information not availale. Reason: {e}")
        data = {}
    return data


def parallel_get_country_info(countries: list):
    with ThreadPoolExecutor(max_workers=cpu_count() * 3) as executor:
        futures = [executor.submit(get_country_info, country) for country in countries]
        result = {}
        for future in as_completed(futures):
            result.update(future.result())
    return result
