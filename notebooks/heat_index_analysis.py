import pandas as pd
import os

# ----------------------------------
# Step 1: Load weather data
# ----------------------------------
input_path = os.path.join("..", "data", "weather_data_2025-07-03.csv")
df = pd.read_csv(input_path)

# ----------------------------------
# Step 2: Define Heat Index function
# ----------------------------------
def compute_heat_index(temp_celsius, humidity):
    # Convert Celsius to Fahrenheit
    T = temp_celsius * 9/5 + 32
    R = humidity

    # Rothfusz regression formula
    HI = (
        -42.379 + 2.04901523*T + 10.14333127*R
        - 0.22475541*T*R - 0.00683783*T*T
        - 0.05481717*R*R + 0.00122874*T*T*R
        + 0.00085282*T*R*R - 0.00000199*T*T*R*R
    )

    # Convert back to Celsius
    HI_C = (HI - 32) * 5/9
    return round(HI_C, 2)

# ----------------------------------
# Step 3: Apply function to DataFrame
# ----------------------------------
df['heat_index'] = df.apply(lambda row: compute_heat_index(row['temperature'], row['humidity']), axis=1)

# ----------------------------------
# Step 4: Save updated data
# ----------------------------------
output_path = os.path.join("..", "data", "weather_data_with_heat_index.csv")
df.to_csv(output_path, index=False)

# ----------------------------------
# Done!
# ----------------------------------
print("Heat Index calculated and saved to:")
print(os.path.abspath(output_path))
print("\nFinal DataFrame:")
print(df)
