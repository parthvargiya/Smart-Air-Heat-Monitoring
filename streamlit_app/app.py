# streamlit_app/app.py

import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from utils.fetch_live_data import fetch_all_live_data

st.set_page_config(page_title="Smart Air & Heat Index Monitoring", layout="wide")
st.title("🌍 Smart Air & Heat Index Monitoring Dashboard")

# --- Step 1: Fetch live data ---
@st.cache_data(show_spinner=True)
def load_live_data():
    return fetch_all_live_data()

df = load_live_data()

if df is None or df.empty:
    st.error("No live data available. Please check API or connectivity.")
    st.stop()

# --- Step 2: City Selection ---
cities = df["city"].unique()
selected_city = st.selectbox("Select City", cities)

city_df = df[df["city"] == selected_city]

# --- Step 3: Show City Snapshot ---
st.subheader(f"Live Snapshot – {selected_city}")
st.dataframe(city_df, use_container_width=True)

# --- Step 4: Show Key Metrics ---
st.subheader(f"🔹 Key Metrics for {selected_city}")
col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Temperature (°C)", city_df["temperature"].values[0])
with col2:
    st.metric("Humidity (%)", city_df["humidity"].values[0])
with col3:
    st.metric("Heat Index (°C)", city_df["heat_index"].values[0])

# --- Step 5: Heat Index Bar Chart ---
st.subheader("Heat Index Comparison Across Cities")
fig, ax = plt.subplots(figsize=(10, 5))
sns.barplot(data=df, x="city", y="heat_index", palette="coolwarm", ax=ax)
ax.set_ylabel("Heat Index (°C)")
ax.set_title("City-wise Heat Index")
ax.set_xticklabels(ax.get_xticklabels(), rotation=45, ha='right')  # Rotation fix
plt.tight_layout()
st.pyplot(fig)


# --- Step 6: Pollutant Comparison Chart ---
st.subheader(f"Pollutant Levels in {selected_city}")
pollutants = ["pm25", "pm10", "no2", "so2", "co"]
pollutant_values = {
    p: city_df[p].values[0] if p in city_df.columns else "N/A"
    for p in pollutants
}

pollution_df = pd.DataFrame({
    "Pollutant": list(pollutant_values.keys()),
    "Value": list(pollutant_values.values())
})

st.bar_chart(pollution_df.set_index("Pollutant"))
st.write("Cities available in live data:", df["city"].unique())


# Footer
st.markdown("---")
st.markdown("Project: Smart Air & Heat Index Monitoring | Author: Parth Varagiya")

