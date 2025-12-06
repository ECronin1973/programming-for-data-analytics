# Methodology: Flight Punctuality Analysis at Dublin Airport

## 1. Project Overview
This project examines how local weather conditions affect flight punctuality at Dublin Airport.  
The analysis integrates flight activity data (arrivals, departures, delays, cancellations) with hourly weather data from Met Éireann.  
The workflow emphasises **schema enforcement, database integration, exploratory analysis, correlation, and modelling**, producing a transparent and reproducible foundation for assessing weather impacts on delays.

---

## 2. Data Sources
- **Flight Activity Data**
  - Acquired via the Aviation Edge API (scheduled vs actual times, delay minutes, flight status).  
  - Monthly batching ensured GitHub compatibility and reproducibility.  

- **Weather Data**
  - Historical hourly weather from Met Éireann (temperature, humidity, visibility, rainfall, wind speed/direction).  
  - Forecast data for Dublin region (short‑term outlook).  

- **Database Schema (`dublin_airport.db`)**
  - `flights`: flight_number, scheduled_arrival, actual_arrival, delay_minutes, status (landed, cancelled, diverted).  
  - `weather_hourly`: timestamp, temp_c, humidity_pct, visibility_m, rain_mm, wind_speed_knots, wind_dir_deg.  
  - Joined tables aligned on hourly flooring for deterministic merges.  

---

## 3. Data Cleaning & Normalisation
- **Schema Enforcement:** Flight and weather tables validated against authoritative schemas; missingness audits exported.  
- **Time Alignment:** Flooring to hourly bins ensured reproducible joins, though short‑lived events were dampened.  
- **Unit Conversion:** Standardised wind speed (knots → km/h), rainfall (mm), temperature (°C).  
- **Derived Features:** Flags for heavy rain, strong wind, low visibility, seasonal categories.  
- **Missing Data:** Explicit NaN handling; imputation flags (`imputed_flag`) documented in schema exports.  

---

## 4. Analysis Techniques
- **Exploratory Data Analysis (EDA):**
  - Weather distributions (temperature, rainfall, wind speed, humidity, visibility).  
  - Scatterplots (humidity vs visibility, temperature vs humidity).  
  - Correlation heatmaps (arrivals + weather, departures + weather).  
  - Operational context plots (wind roses, WMO weather codes, risk score distributions).  

- **Delay Analysis (Post‑Merge):**
  - Daily arrivals vs departures volumes.  
  - Hourly delay patterns.  
  - Airline‑level delay comparisons.  
  - Boxplots of delays under different weather categories.  

- **Modelling:**
  - Benchmarked Linear Regression, Random Forest, and CatBoost.  
  - Metrics: R² and RMSE for arrivals and departures.  
  - Random Forest consistently outperformed, with arrivals R² ≈0.11 and departures ≈0.06.  
  - Feature importance highlighted **temperature and humidity** as dominant drivers, with visibility and rainfall contributing less.  

---

## 5. Visualisation
- **Python (Matplotlib/Seaborn):** Histograms, scatterplots, boxplots, correlation heatmaps.  
- **Auto‑generated PNGs:** Saved systematically to `plots/` (`sXX_<descriptor>.png`) for reproducibility.  
- **Database Queries:** SQL used to aggregate delays, compute risk exceedances, and validate joins.  

---

## 6. Insights & Deliverables
- Visibility and humidity emerged as the strongest correlates of delays; rainfall and temperature weaker.  
- Departures showed lower weather sensitivity, reflecting missing operational drivers.  
- Hourly flooring reduced temporal granularity, dampening short‑term disruption signals.  
- Deliverables included: cleaned datasets, database (`dublin_airport.db`), EDA plots, correlation matrices, feature importance charts, and documented limitations.  

---

## 7. Repository Layout
- `project.ipynb` — main notebook with full workflow (acquire → clean → integrate → database → model → conclude).  
- `README.md` — summary, assessment alignment, quick start instructions.  
- `data/` — cleaned CSVs, batched flight JSONs, risk tables.  
- `plots/` — auto‑generated PNG artefacts (EDA, correlations, modelling).  
- `docs/methodology.md` — extended methodological narrative (this file).  
- `dublin_airport.db` — root‑level SQLite database with merged weather + flight tables, enforced schemas, and query outputs.  
- `requirements.txt` — Python dependencies pinned for reproducibility.  

---

## 8. Further Angles
- Incorporating airline schedules, traffic density, and ATC interventions.  
- Gust vs sustained wind impact on delays.  
- Visibility proxies (pressure + rain + time‑of‑day).  
- Scenario bands for forecast uncertainty (optimistic/central/pessimistic).  

---

## 9. Assessment Alignment
- **Code (40%)**: Structured notebook, schema enforcement, reproducible plots, database queries.  
- **Documentation (40%)**: Clear explanations, plots with captions, limitations noted, reviewer takeaways.  
- **Research (10%)**: Sources cited inline (Met Éireann, Aviation Edge API, WMO codes).  
- **Consistency (10%)**: Clean repo, meaningful commits, notebook saved with outputs, reproducible database.  

---

## 10. Limitations
- Weather‑only predictors explain limited variance (≤11% arrivals, ≤6% departures).  
- Hourly flooring obscures sub‑hour disruptions.  
- Forecast integration exploratory only; no back‑testing against actual delay outcomes.  
- Operational drivers (airline schedules, traffic density, ATC constraints) absent, limiting predictive capacity.  

---
