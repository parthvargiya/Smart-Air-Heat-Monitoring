import pandas as pd
import matplotlib.pyplot as plt
import os

# ----------------------------------
# Step 1: Load the data
# ----------------------------------
input_path = os.path.join("..", "data", "weather_data_with_heat_index.csv")
df = pd.read_csv(input_path)

# ----------------------------------
# Step 2: Plot Heat Index Bar Chart
# ----------------------------------
plt.figure(figsize=(8, 6))
bars = plt.bar(df['city'], df['heat_index'], color='tomato')

# Annotate heat index values on top
for bar in bars:
    height = bar.get_height()
    plt.annotate(f"{height}°C", xy=(bar.get_x() + bar.get_width() / 2, height),
                 xytext=(0, 3), textcoords="offset points", ha='center', fontsize=10)

# Title and labels
plt.title("Heat Index Comparison Across Cities", fontsize=14)
plt.ylabel("Heat Index (°C)")
plt.xlabel("City")
plt.tight_layout()

# ----------------------------------
# Step 3: Save chart to reports/images/
# ----------------------------------
output_dir = os.path.join("..", "reports", "images")
os.makedirs(output_dir, exist_ok=True)
output_path = os.path.join(output_dir, "heat_index_bar_chart.png")
plt.savefig(output_path)

# ----------------------------------
# Done!
# ----------------------------------
print(" Chart saved to:", os.path.abspath(output_path))


output_dir = os.path.join("..", "reports", "images")
os.makedirs(output_dir, exist_ok=True)  # Creates folder if not present

output_path = os.path.join(output_dir, "heat_index_bar_chart.png")
plt.tight_layout()
plt.savefig(output_path)
plt.close()

plt.show()