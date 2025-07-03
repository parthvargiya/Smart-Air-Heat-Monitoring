import pandas as pd
import matplotlib.pyplot as plt

# Load the cleaned dataset
df = pd.read_csv("../data/cleaned_aqicn_2025-07-02.csv")

# Extract values
pollutants = ['pm25', 'pm10', 'no2', 'so2', 'co', 'o3']
cities = df['city'].values
values = df[pollutants].values

# Plotting
plt.figure(figsize=(10, 6))
bar_width = 0.35
x = range(len(pollutants))

plt.bar(x, values[0], width=bar_width, label=cities[0], color='skyblue')
plt.bar([i + bar_width for i in x], values[1], width=bar_width, label=cities[1], color='salmon')

plt.xlabel("Pollutants")
plt.ylabel("Concentration")
plt.title("Pollutant Levels Comparison: Ahmedabad vs Vapi (2025-07-02 22:00)")
plt.xticks([i + bar_width / 2 for i in x], pollutants)
plt.legend()
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.savefig("../reports/images/pollutant_bar_chart.png")
plt.show()

