import requests
import pandas as pd
from datetime import datetime

API_TOKEN = "f4117ba106d46f5c0d853c8e39e5f6443684fa2f"

# Base URL for AQICN API
BASE_URL = "https://api.waqi.info/feed/{city}/?token={token}"

def fetch_city_data(city_name):
    """Fetch PM2.5 and other pollutants for a given city from AQICN."""
    url = BASE_URL.format(city=city_name, token=API_TOKEN)
    response = requests.get(url)
    data = response.json()

    if data["status"] != "ok":
        print(f" Error fetching data for {city_name}: {data.get('data', '')}")
        return None

    iaqi = data["data"]["iaqi"]
    time = data["data"]["time"]["s"]

    result = {
        "city": city_name,
        "time": time,
        "pm25": iaqi.get("pm25", {}).get("v", None),
        "pm10": iaqi.get("pm10", {}).get("v", None),
        "no2": iaqi.get("no2", {}).get("v", None),
        "so2": iaqi.get("so2", {}).get("v", None),
        "co": iaqi.get("co", {}).get("v", None),
        "o3": iaqi.get("o3", {}).get("v", None),
    }

    return result

def save_to_csv(data_list, filename):
    df = pd.DataFrame(data_list)
    df.to_csv(filename, index=False)
    print(f" Data saved to {filename}")

if __name__ == "__main__":
    cities = ["india/ahmedabad/maninagar", "india/vapi/phase-1-gidc"]

    all_data = []
    for city in cities:
        print(f" Fetching data for {city}...")
        data = fetch_city_data(city)
        if data:
            all_data.append(data)

    if all_data:
        now = datetime.now().strftime("%Y-%m-%d_%H-%M")
        output_file = f"data/aqicn_{now}.csv"
        save_to_csv(all_data, output_file)
