import requests
import pandas as pd
import os
import time

API_KEY = "15fa9875a90fc02095355d8df176dc12"  
cities = ["Ahmedabad,IN", "Vapi,IN", "Bengaluru,IN"]
weather_data = []

for city in cities:
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    response = requests.get(url)
    data = response.json()

    if "main" in data:
        temp = data["main"]["temp"]
        humidity = data["main"]["humidity"]
        weather_data.append({"city": city, "temperature": temp, "humidity": humidity})
    else:
        print(f" Failed to fetch for {city}: {data.get('message', 'Unknown error')}")
    
    time.sleep(1)  # Pause 1 second between requests (optional for API limit)

# Convert and save to ../data/
df = pd.DataFrame(weather_data)
output_path = os.path.join("data", "weather_data_2025-07-09.csv")
df.to_csv(output_path, index=False)
print(" Weather data saved:", os.path.abspath(output_path))
