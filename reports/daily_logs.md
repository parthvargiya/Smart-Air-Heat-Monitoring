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
