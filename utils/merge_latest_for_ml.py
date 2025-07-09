import pandas as pd
import numpy as np

# File paths for today's fresh data
aqi_path = "data/aqicn_2025-07-09_15-01.csv"
weather_path = "data/weather_data_2025-07-09.csv"
output_path = "data/merged_aqi_weather_with_heat_index_2025-07-09.csv"

# Load AQI data
aqi_df = pd.read_csv(aqi_path)

# Normalize city names in AQI data
city_map = {
    "india/ahmedabad/maninagar": "Ahmedabad,IN",
    "india/vapi/phase-1-gidc": "Vapi,IN"
}
aqi_df["city"] = aqi_df["city"].map(city_map)
aqi_df = aqi_df.dropna(subset=["city"])

# Fill missing CO value for Vapi (known gap)
aqi_df["co"] = aqi_df["co"].fillna(3.3)

# Load weather data
weather_df = pd.read_csv(weather_path)
weather_df = weather_df[weather_df["city"].isin(["Ahmedabad,IN", "Vapi,IN"])]

# --- Compute Heat Index if missing ---
if "heat_index" not in weather_df.columns:
    T_c = weather_df["temperature"]
    R = weather_df["humidity"]

    # Convert temperature from Celsius to Fahrenheit
    T_f = (T_c * 9/5) + 32

    # Rothfusz regression formula in Fahrenheit
    HI_f = (
        -42.379 + 2.04901523 * T_f + 10.14333127 * R
        - 0.22475541 * T_f * R - 0.00683783 * T_f**2
        - 0.05481717 * R**2 + 0.00122874 * T_f**2 * R
        + 0.00085282 * T_f * R**2 - 0.00000199 * T_f**2 * R**2
    )

    # Convert Heat Index back to Celsius
    HI_c = (HI_f - 32) * 5/9
    weather_df["heat_index"] = HI_c.round(2)


# Merge datasets
merged_df = pd.merge(weather_df, aqi_df, on="city", how="inner")

# Show preview
print("Merged Data:")
print(merged_df[["city", "temperature", "humidity", "heat_index", "pm25", "pm10", "no2", "so2", "co", "o3"]])

# Save result
merged_df.to_csv(output_path, index=False)
print(f"\nMerged dataset saved to: {output_path}")
