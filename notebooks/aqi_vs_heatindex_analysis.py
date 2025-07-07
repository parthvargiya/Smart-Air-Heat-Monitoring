import pandas as pd

# Load cleaned AQI data
aqi_df = pd.read_csv("data/cleaned_aqicn_2025-07-02.csv")

# Load weather + heat index data
weather_df = pd.read_csv("data/weather_data_with_heat_index.csv")

print("AQI Data:")
print(aqi_df.head())

print("\nWeather Data:")
print(weather_df.head())

# Replace complex AQI city paths with simplified city names to match weather data
aqi_df['city'] = aqi_df['city'].replace({
    "india/ahmedabad/maninagar": "Ahmedabad,IN",
    "india/vapi/phase-1-gidc": "Vapi,IN"
})

merged_df = pd.merge(aqi_df, weather_df, on='city')
print("Merged DataFrame:")
print(merged_df)

# List of features to analyze
features = ['pm25', 'pm10', 'co', 'no2', 'so2', 'temperature', 'humidity', 'heat_index']

# Compute correlation matrix
correlation_matrix = merged_df[features].corr()

# Print correlation matrix
print("Final Correlation Matrix:")
print(correlation_matrix)

import os
import matplotlib.pyplot as plt
import seaborn as sns

# Ensure the save directory exists
os.makedirs("reports/images", exist_ok=True)

# Features to compare with heat index
features_to_plot = ['pm25', 'pm10', 'no2', 'so2', 'temperature']

# Create scatter plots
for col in features_to_plot:
    plt.figure(figsize=(6, 4))
    sns.scatterplot(data=merged_df, x=col, y='heat_index', hue='city', s=120)
    plt.title(f"{col.upper()} vs Heat Index")
    plt.xlabel(col.upper())
    plt.ylabel("Heat Index")
    plt.legend(title="City")
    plt.grid(True)
    plt.tight_layout()
    plt.savefig(f"reports/images/{col}_vs_heat_index.png")
    plt.close()

print("Scatter plots saved in /reports/images with city labels.")
