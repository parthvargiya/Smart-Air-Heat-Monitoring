# streamlit_app/app.py

import streamlit as st
import pandas as pd
import joblib
import os
import matplotlib.pyplot as plt
import seaborn as sns

# Set page configuration
st.set_page_config(page_title="Smart Air & Heat Index Monitoring", layout="wide")

# Load data and model
DATA_PATH = os.path.join("data", "merged_aqi_weather_with_heat_index_2025-07-09.csv")
MODEL_PATH = os.path.join("models", "heat_index_predictor.pkl")

@st.cache_data
def load_data():
    return pd.read_csv(DATA_PATH)

@st.cache_resource
def load_model():
    return joblib.load(MODEL_PATH)

# Load resources
df = load_data()
model = load_model()

# Title
st.title("Smart Air & Heat Index Monitoring Dashboard")

# Sidebar
cities = df["city"].unique().tolist()
selected_city = st.sidebar.selectbox("Select City", cities)

# Filter city data
city_df = df[df["city"] == selected_city]

# Display basic info
st.subheader(f"Current Conditions in {selected_city}")
st.dataframe(city_df)

# Section placeholders (will be updated next)
st.markdown("---")
st.header("Charts and Analysis")

# 1. Pollution Bar Chart
st.subheader("1. Pollution Level Comparison – Ahmedabad vs Vapi")
st.image("reports/images/pollutant_bar_chart.png", use_container_width=True)

# 2. Heat Index Bar Chart
st.subheader("2. Heat Index – Citywise Comparison")
st.image("reports/images/heat_index_bar_chart.png", use_container_width=True)

# 3. Correlation Scatter Plots
st.subheader("3. Correlation: Pollutants & Weather vs Heat Index")

st.markdown("**PM2.5 vs Heat Index**")
st.image("reports/images/pm25_vs_heat_index.png", use_container_width=True)

st.markdown("**PM10 vs Heat Index**")
st.image("reports/images/pm10_vs_heat_index.png", use_container_width=True)

st.markdown("**NO2 vs Heat Index**")
st.image("reports/images/no2_vs_heat_index.png", use_container_width=True)

st.markdown("**SO2 vs Heat Index**")
st.image("reports/images/so2_vs_heat_index.png", use_container_width=True)

st.markdown("**Temperature vs Heat Index**")
st.image("reports/images/temperature_vs_heat_index.png", use_container_width=True)

# 4. Prediction Results
st.subheader("4. Machine Learning – Heat Index Prediction (Actual vs Predicted)")
st.image("reports/images/heat_index_prediction_plot.png", use_container_width=True)