# Project Daily Log – Smart Air & Heat Index Monitoring

## Day 1 – 2 July 2025

**Focus:**  
Project setup, data collection, and structure planning

**Tasks Completed:**
- Finalized project title and theme: Smart Air & Heat Index Monitoring for Urban Sustainability
- Identified key objectives aligned with UN SDGs 3, 11, and 13
- Collected AQI data from AQICN API for Ahmedabad (Maninagar) and Vapi (Phase-1 GIDC)
- Saved raw AQI data as CSV in `/data/` folder
- Created project folder structure:
  - `/data/`, `/notebooks/`, `/models/`, `/reports/`, `/utils/`, `/streamlit_app/`
- Created and cloned GitHub repository (initial setup only, no commits yet)

**Pending / Next Tasks:**
- Clean the collected data
- Handle missing values
- Begin exploratory data analysis

## Day 2 – 3 July 2025

**Focus:**  
Initial EDA – Air pollution level comparison (Ahmedabad vs Vapi)

**Tasks Completed:**
- Cleaned AQI dataset and handled missing CO value (imputed Vapi as 3.3)
- Saved cleaned file as `/data/cleaned_aqicn_2025-07-02.csv`
- Created `pollution_comparison.py` script in `/notebooks/`
- Generated side-by-side pollutant bar chart (6 parameters)
- Saved chart as `/reports/images/pollutant_bar_chart.png`
- Wrote insights in `/reports/pollution_comparison_insights.md`

**Pending / Next Tasks:**
- Analyze temperature and heat index from weather data (Day 3)
- Start integrating DL/ML-based insights into EDA
- Prepare for first Git commit

----------------------------------------
## Day 3 – Heat Index & Weather EDA
Date: 2025-07-03
----------------------------------------

Weather data fetched for 3 cities (Ahmedabad, Vapi, Bengaluru) using OpenWeatherMap API
Heat Index calculated using Rothfusz regression formula
Updated dataset saved to: data/weather_data_with_heat_index.csv
Heat Index bar chart created and saved: reports/images/heat_index_bar_chart.png

Insights:
- Ahmedabad recorded the highest Heat Index (34.3°C), mainly due to high humidity (71%)
- Vapi, despite lower temperature, had a high index (30.5°C) due to extreme humidity (94%)
- Bengaluru had the most comfortable index (28.3°C), showing why it's considered ideal weather-wise

Conclusion:
Humidity strongly influences urban heat discomfort. Cities like Ahmedabad and Vapi may require smart alert systems for humid heatwaves.

All code saved inside:
- notebooks/heat_index_analysis.py
- notebooks/heat_index_visualization.py

---

### Day 4 – 7th July 2025

-  Merged AQI and weather datasets for Ahmedabad and Vapi
-  Fixed city name mismatch to align datasets
-  Generated correlation matrix between pollutants and heat index
-  Created scatter plots (PM2.5, PM10, NO2, SO2, Temperature vs Heat Index)
-  Enhanced visual clarity using Seaborn (city color labels and legends)
-  Wrote analytical insights on pollutant-weather relationships
-  All charts saved in /reports/images/
-  Bengaluru excluded from this analysis due to missing pollutant data

