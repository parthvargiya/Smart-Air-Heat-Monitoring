import pandas as pd
import os

# Define file paths
aqi_path = os.path.join("data", "cleaned_aqicn_2025-07-02.csv")
weather_path = os.path.join("data", "weather_data_with_heat_index.csv")
merged_path = os.path.join("data", "merged_aqi_weather_with_heat_index.csv")

# Load datasets
aqi_df = pd.read_csv(aqi_path)
weather_df = pd.read_csv(weather_path)

# Print original city names for debugging
print("Original AQI Cities:", aqi_df["city"].unique())
print("Original Weather Cities:", weather_df["city"].unique())

# Standardize AQI city names to match weather dataset
city_mapping = {
    "india/ahmedabad/maninagar": "Ahmedabad,IN",
    "india/vapi/phase-1-gidc": "Vapi,IN"
}
aqi_df["city"] = aqi_df["city"].map(city_mapping)

# Merge on standardized city names
merged_df = pd.merge(aqi_df, weather_df, on="city", how="inner")

# Drop any rows with missing values (optional but safe)
merged_df = merged_df.dropna()

# Print merged result
print("Merged Data:\n", merged_df)

# Save merged dataset
merged_df.to_csv(merged_path, index=False)
print(f"Merged dataset saved to: {merged_path}")
