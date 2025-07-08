import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
import joblib
import os

# Paths
merged_path = os.path.join('data', 'merged_aqi_weather_with_heat_index.csv')
model_path = os.path.join('models', 'heat_index_predictor.pkl')
scatter_plot_path = os.path.join('reports', 'images', 'heat_index_prediction_plot.png')
bar_plot_path = os.path.join('reports', 'images', 'heat_index_bar_plot.png')

# Read merged dataset
df = pd.read_csv(merged_path)
print("Merged Data:\n", df)

# Select features and target
features = ['pm25', 'pm10', 'no2', 'so2', 'co', 'temperature', 'humidity']
target = 'heat_index'

X = df[features]
y = df[target]

# Train model on full data (small dataset)
model = LinearRegression()
model.fit(X, y)
y_pred = model.predict(X)

# Evaluation
mae = mean_absolute_error(y, y_pred)
mse = mean_squared_error(y, y_pred)
rmse = mse ** 0.5
r2 = r2_score(y, y_pred)

print("\nModel Evaluation (on full dataset):")
print(f"MAE: {mae:.2f}")
print(f"RMSE: {rmse:.2f}")
print(f"R² Score: {r2:.2f}")

print("X used for prediction:\n", X)
print("Predicted Heat Index:\n", y_pred)
print("Actual Heat Index:\n", list(y))

# Save model
joblib.dump(model, model_path)
print(f"\nModel saved to: {model_path}")

# Plot 1: Scatter Plot (Predicted vs Actual)
plt.figure(figsize=(6, 6))
plt.scatter(y, y_pred, color='blue', label='Predicted')
plt.plot([min(y), max(y)], [min(y), max(y)], color='red', linestyle='--', label='Ideal Fit')
plt.xlabel('Actual Heat Index')
plt.ylabel('Predicted Heat Index')
plt.title('Predicted vs Actual Heat Index')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig(scatter_plot_path)
plt.close()
print(f"Plot saved to: {scatter_plot_path}")

# Plot 2: Bar Plot (City-wise Actual vs Predicted)
cities = df['city'].values
x = np.arange(len(cities))

plt.figure(figsize=(8, 5))
plt.bar(x - 0.2, y, width=0.4, label='Actual', color='skyblue')
plt.bar(x + 0.2, y_pred, width=0.4, label='Predicted', color='orange')
plt.xticks(x, cities, rotation=15)
plt.ylabel('Heat Index')
plt.title('Actual vs Predicted Heat Index per City')
plt.legend()
plt.grid(axis='y')
plt.tight_layout()
plt.savefig(bar_plot_path)
plt.close()
print(f"Bar plot saved to: {bar_plot_path}")
