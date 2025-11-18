# Methodology: Flight Rerouting Analysis at Dublin Airport

## 1. Project Overview
This project investigates flight rerouting events at Dublin Airport and their relationship to local weather conditions. The analysis combines flight activity data with historical and forecast weather data from Met Éireann to identify trends, visualise reroute reasons, and project future rerouting probabilities.

---

## 2. Data Sources
- **Flight Activity Data**
  - Dublin Airport dashboards and flight trackers (arrivals, departures, runway usage).
  - Annotated CSV of reroute events (date, time, flight, runway change, reason).
- **Weather Data**
  - Historical hourly/daily weather from Met Éireann (wind, rain, temperature, pressure).
  - Forecast data for Dublin region (next week outlook).
- **Schema**
  - `flights`: flight_number, scheduled_arrival, actual_arrival, runway_planned, runway_used, rerouted_flag, reroute_reason.
  - `weather_hourly`: timestamp, wind_speed_kmh, wind_dir_deg, gust_kmh, rain_mm, temp_c, pressure_hpa.

---

## 3. Data Cleaning & Normalisation
- **Time Alignment:** Join flights with nearest weather record within ±60 minutes.
- **Unit Conversion:** Normalize wind speed (knots → km/h), rainfall (mm), temperature (°C).
- **Derived Features:** Compute headwind and crosswind components relative to runway orientation.
- **Reason Taxonomy:** Standardise reroute reasons into categories (crosswind, tailwind, rain/wet, low visibility, ATC/traffic, other).
- **Missing Data:** Explicit NaN handling; “unknown” category for missing reroute reasons.

---

## 4. Analysis Techniques
- **Exploratory Data Analysis (EDA):**
  - Frequency of reroutes by reason, time of day, and runway.
  - Scatter plots of wind speed vs reroute events.
  - Box plots of rainfall and visibility split by reroute flag.
- **Heat Maps:**
  - Hour-of-day × wind-direction reroute rates.
  - Runway × wind-speed band reroute counts.
- **Forecasting:**
  - Logistic regression and gradient-boosted trees predicting reroute probability.
  - Features: wind speed, crosswind, rain, gusts, hour, day of week.
  - Apply trained model to next-week Met Éireann forecasts.

---

## 5. Visualisation
- **Python (Matplotlib/Seaborn):** Quick EDA plots, density plots, box plots.
- **JavaScript (Plotly):**
  - Interactive bar charts of reroute reasons.
  - Heat maps of reroute rates by wind direction and time.
  - Probability timelines for forecasted reroute risk.

---

## 6. Insights & Deliverables
- Identify weather conditions most associated with rerouting (e.g., crosswinds > 30 km/h).
- Highlight temporal patterns (peak reroutes during evening arrivals).
- Forecast reroute risk windows for the next week based on Met Éireann data.
- Provide interactive charts and concise explanations in the notebook.

---

## 7. Repository Layout
- `notebooks/flight_reroute_dub.ipynb` — main notebook with analysis and plots.
- `data/` — raw and processed CSVs (flight events, weather).
- `src/` — modular Python scripts (data loaders, feature engineering, modeling, JS viz).
- `README.md` — overview, setup instructions, imports required.
- `docs/methodology.md` — this document.

---

## 8. Further Angles
- Gust vs sustained wind impact on reroutes.
- Traffic density and ATC-related reroutes.
- Visibility proxies (pressure + rain + time-of-day).
- Scenario bands for forecast uncertainty (optimistic/central/pessimistic).

---

## 9. Assessment Alignment
- **Code (40%)**: Modular, efficient, reusable functions; clear feature engineering; JS + Python plots.
- **Documentation (40%)**: Succinct explanations, plots with captions, limitations noted.
- **Research (10%)**: Sources cited inline (Met Éireann, flight dashboards).
- **Consistency (10%)**: Clean repo, meaningful commits, notebook saved with outputs.

---

## 10. Limitations
- Public flight dashboards may not expose all reroute reasons; annotated CSVs supplement.
- Forecast uncertainty acknowledged; reroute projections are indicative, not operational guarantees.
- Visibility data may require proxies; documented clearly.

---
