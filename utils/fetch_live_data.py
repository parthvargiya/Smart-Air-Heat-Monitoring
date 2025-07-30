# utils/fetch_live_data.py

import requests
import pandas as pd

# --- API Keys (replace with your actual keys) ---
AQICN_TOKEN = "f4117ba106d46f5c0d853c8e39e5f6443684fa2f"
OPENWEATHERMAP_KEY = "15fa9875a90fc02095355d8df176dc12"

# --- City and Station Mappings ---
CITIES = {
    "Vapi (Phase-1 GIDC)": {
        "aqicn_path": "india/vapi/phase-1-gidc",
        "weather_city": "Vapi,IN"
    },
    "Ahmedabad (Maninagar)": {
        "aqicn_path": "india/ahmedabad/maninagar",
        "weather_city": "Ahmedabad,IN"
    },
    "Noida (Sector - 62)": {
        "aqicn_path": "india/noida/sector-62",
        "weather_city": "Noida,IN"
    },
    "Mumbai (Kurla)": {
        "aqicn_path": "india/mumbai/kurla",
        "weather_city": "Mumbai,IN"
    },
    "Coimbatore (Sidco Kurichi)": {
        "aqicn_path": "india/coimbatore/sidco-kurichi",
        "weather_city": "Coimbatore,IN"
    },
    "Kolkata (Bidhannagar)": {
        "aqicn_path": "india/kolkata/bidhannagar",
        "weather_city": "Kolkata,IN"
    },
    "Jaipur (Adarsh Nagar)": {
        "aqicn_path": "india/jaipur/adarsh-nagar",
        "weather_city": "Jaipur,IN"
    },
    "Hyderabad (Somajiguda)": {
        "aqicn_path": "india/hyderabad/somajiguda",
        "weather_city": "Hyderabad,IN"
    },
    "Bengaluru (Silk Board)": {
        "aqicn_path": "india/bengaluru/silk-board",
        "weather_city": "Bengaluru,IN"
    },
    "Chandigarh (Sector-25)": {
        "aqicn_path": "india/chandigarh/sector-25",
        "weather_city": "Chandigarh,IN"
    },
    "Lucknow (Talkatora)": {
        "aqicn_path": "india/lucknow/talkatora",
        "weather_city": "Lucknow,IN"
    },
    "Shillong (lumpyngngad)": {
        "aqicn_path": "india/shillong/lumpyngngad",
        "weather_city": "Surat,IN"
    }

}

# --- Helper: Fetch AQICN pollutant data ---
def fetch_aqicn_data(station_path):
    try:
        url = f"https://api.waqi.info/feed/{station_path}/?token={AQICN_TOKEN}"
        response = requests.get(url)
        data = response.json()

        if data.get("status") != "ok":
            print(f"[AQICN] Status not OK for {station_path} → status: {data.get('status')}")
            print(f"[AQICN] Full response: {data}")
            return None

        iaqi = data.get("data", {}).get("iaqi", {})
        return {
            "pm25": iaqi.get("pm25", {}).get("v"),
            "pm10": iaqi.get("pm10", {}).get("v"),
            "no2": iaqi.get("no2", {}).get("v"),
            "so2": iaqi.get("so2", {}).get("v"),
            "co": iaqi.get("co", {}).get("v"),
        }

    except Exception as e:
        print(f"[AQICN] Error fetching data for {station_path}: {e}")
        return None


# --- Helper: Fetch OpenWeatherMap data ---
def fetch_openweather_data(city_name):
    try:
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={OPENWEATHERMAP_KEY}&units=metric"
        response = requests.get(url)
        data = response.json()

        if data.get("cod") != 200:
            print(f"[Weather] Invalid response code for {city_name} → code: {data.get('cod')}")
            print(f"[Weather] Full response: {data}")
            return None

        return {
            "temperature": data["main"]["temp"],
            "humidity": data["main"]["humidity"]
        }

    except Exception as e:
        print(f"[Weather] Error fetching weather data for {city_name}: {e}")
        return None


# --- Heat Index Calculation (Rothfusz formula, °C version) ---
def calculate_heat_index(temp_c, humidity):
    # Convert Celsius to Fahrenheit for calculation
    T = temp_c * 9/5 + 32
    R = humidity

    HI_f = (
        -42.379 + 2.04901523 * T + 10.14333127 * R
        - 0.22475541 * T * R - 0.00683783 * T**2
        - 0.05481717 * R**2 + 0.00122874 * T**2 * R
        + 0.00085282 * T * R**2 - 0.00000199 * T**2 * R**2
    )

    # Convert back to Celsius
    return round((HI_f - 32) * 5/9, 2)

# --- Main: Fetch all city data ---
def fetch_all_live_data():
    records = []

    for city, info in CITIES.items():
        print(f"Fetching data for: {city}")

        aqicn = fetch_aqicn_data(info["aqicn_path"])
        weather = fetch_openweather_data(info["weather_city"])

        print(f"[DEBUG] AQICN for {city}: {aqicn}")
        print(f"[DEBUG] Weather for {city}: {weather}")

        if aqicn is None or weather is None:
            print(f"[EXCEPTION] Skipping {city}: Missing data")
            continue

        heat_index = calculate_heat_index(weather["temperature"], weather["humidity"])

        record = {
            "city": city,
            "temperature": weather["temperature"],
            "humidity": weather["humidity"],
            "heat_index": heat_index,
            **aqicn
        }

        records.append(record)

    df = pd.DataFrame(records)

    if not df.empty and "city" in df.columns:
        print("Cities in final live dataset:", df["city"].tolist())
    else:
        print("No valid city data fetched. DataFrame is empty.")

    return df
