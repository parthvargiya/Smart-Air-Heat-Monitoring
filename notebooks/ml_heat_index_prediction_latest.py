# ml_heat_index_prediction_latest.py

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
import joblib
import os

# Load latest merged dataset (9 July)
data_path = "data/merged_aqi_weather_with_heat_index_2025-07-09.csv"
df = pd.read_csv(data_path)

# Drop any rows with missing values
df.dropna(inplace=True)

# Ensure heat_index is float
df["heat_index"] = df["heat_index"].astype(float)

# Select features and target
X = df[["pm25", "pm10", "no2", "so2", "co", "temperature", "humidity"]]
y = df["heat_index"]

# Train model on full dataset
model = LinearRegression()
model.fit(X, y)

# Predict on same data (due to low sample size)
y_pred = model.predict(X)

# Evaluation
mae = mean_absolute_error(y, y_pred)
rmse = mean_squared_error(y, y_pred) ** 0.5
r2 = r2_score(y, y_pred)

print("\nModel Evaluation (on full dataset):")
print(f"MAE: {mae:.2f}")
print(f"RMSE: {rmse:.2f}")
print(f"R² Score: {r2:.2f}")

print("X used for prediction:")
print(X)
print("\nPredicted Heat Index:")
print(y_pred)
print("\nActual Heat Index:")
print(list(y))

# Save model
os.makedirs("models", exist_ok=True)
joblib.dump(model, "models/heat_index_predictor_latest.pkl")

# Plot actual vs predicted with city labels
plt.figure(figsize=(8, 6))
sns.scatterplot(x=y, y=y_pred, hue=df['city'], s=100)
plt.plot([y.min(), y.max()], [y.min(), y.max()], 'k--', lw=2)
plt.xlabel("Actual Heat Index")
plt.ylabel("Predicted Heat Index")
plt.title("Heat Index Prediction (Latest Data)")
plt.legend(title="City")
plt.grid(True)

# Save plot
os.makedirs("reports/images", exist_ok=True)
plt.savefig("reports/images/heat_index_prediction_plot_latest.png")
plt.show()

print("\nModel and plot saved successfully.")
