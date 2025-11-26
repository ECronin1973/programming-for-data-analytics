# Methodology: Flight Punctuality Analysis at Dublin Airport

## 1. Project Overview
This project examines how local weather conditions affect flight punctuality at Dublin Airport.  
The analysis integrates flight activity data (arrivals, departures, delays, cancellations) with historical and forecast weather data from Met Éireann to identify trends, quantify impacts, and project future delay probabilities.

---

## 2. Data Sources
- **Flight Activity Data**
  - Dublin Airport dashboards and flight trackers (arrivals, departures, delay and cancellation logs).
  - API‑based datasets (scheduled vs actual times, delay minutes, flight status).
- **Weather Data**
  - Historical hourly/daily weather from Met Éireann (wind, rain, temperature, pressure).
  - Forecast data for the Dublin region (short‑term outlook).
- **Schema**
  - `flights`: flight_number, scheduled_arrival, actual_arrival, delay_minutes, status (landed, cancelled, diverted).
  - `weather_hourly`: timestamp, wind_speed_kmh, wind_dir_deg, gust_kmh, rain_mm, temp_c, pressure_hpa.

---

## 3. Data Cleaning & Normalisation
- **Time Alignment:** Join flights with the nearest weather record within ±60 minutes.  
- **Unit Conversion:** Standardise wind speed (knots → km/h), rainfall (mm), temperature (°C).  
- **Derived Features:** Create flags for heavy rain, strong wind, gusty conditions, and seasonal categories.  
- **Missing Data:** Explicit NaN handling; “unknown” status for incomplete flight records.  

---

## 4. Analysis Techniques
- **Exploratory Data Analysis (EDA):**
  - Distribution of delays by time of day, airline, and season.  
  - Scatter plots of wind speed vs delay minutes.  
  - Box plots of rainfall and visibility split by cancellation status.  
- **Heat Maps:**
  - Hour‑of‑day × wind‑direction delay rates.  
  - Delay severity across wind‑speed bands.  
- **Forecasting:**
  - Regression and gradient‑boosted models predicting delay minutes or cancellation probability.  
  - Features: wind speed, gusts, rainfall, hour, day of week.  
  - Apply trained model to next‑week Met Éireann forecasts.

---

## 5. Visualisation
- **Python (Matplotlib/Seaborn):** Quick EDA plots, density plots, box plots.  
- **JavaScript (Plotly):**
  - Interactive bar charts of delay distributions.  
  - Heat maps of delay rates by wind direction and time.  
  - Probability timelines for forecasted delay risk.  

---

## 6. Insights & Deliverables
- Identify weather conditions most associated with delays and cancellations (e.g., strong crosswinds, heavy rain).  
- Highlight temporal patterns (peak delays during evening arrivals).  
- Forecast delay risk windows for the next week based on Met Éireann data.  
- Provide interactive charts and concise explanations in the notebook.  

---

## 7. Repository Layout
- `notebooks/flight_punctuality_dub.ipynb` — main notebook with analysis and plots.  
- `data/` — raw and processed CSVs (flight events, weather).  
- `src/` — modular Python scripts (data loaders, feature engineering, modeling, JS viz).  
- `README.md` — overview, setup instructions, imports required.  
- `docs/methodology.md` — this document.  

---

## 8. Further Angles
- Gust vs sustained wind impact on delays.  
- Traffic density and ATC‑related cancellations.  
- Visibility proxies (pressure + rain + time‑of‑day).  
- Scenario bands for forecast uncertainty (optimistic/central/pessimistic).  

---

## 9. Assessment Alignment
- **Code (40%)**: Modular, efficient, reusable functions; clear feature engineering; JS + Python plots.  
- **Documentation (40%)**: Succinct explanations, plots with captions, limitations noted.  
- **Research (10%)**: Sources cited inline (Met Éireann, flight dashboards).  
- **Consistency (10%)**: Clean repo, meaningful commits, notebook saved with outputs.  

---

## 10. Limitations
- Public flight dashboards may not expose all delay reasons; analysis relies on available status fields.  
- Forecast uncertainty acknowledged; delay projections are indicative, not operational guarantees.  
- Visibility data may require proxies; documented clearly.  

---
