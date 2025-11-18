# Flight Rerouting Analysis at Dublin Airport

## Overview
This project investigates flight rerouting events at Dublin Airport and their relationship to local weather conditions. The aim is to identify patterns in rerouting decisions, analyse contributing factors such as wind and rainfall, and forecast potential rerouting events using Met Éireann weather data.

The notebook demonstrates data acquisition, cleaning, exploratory analysis, visualisation, and forecasting techniques. It is designed to be modular, well‑documented, and reviewer‑friendly.

---

## Planned Objectives
1. **Data Acquisition**
   - Gather flight activity data from Dublin Airport dashboards and trackers.
   - Download historical weather data from Met Éireann (wind, rain, temperature).
   - Collect forecast data for Dublin region for the upcoming week.

2. **Data Cleaning & Normalization**
   - Align flight events with nearest weather records.
   - Normalise units (wind speed, rainfall, temperature).
   - Standardise reroute reasons into categories (crosswind, tailwind, rain/wet, low visibility, ATC/traffic, other).

3. **Analysis**
   - Explore frequency of reroutes by reason, runway, and time of day.
   - Cross‑reference reroutes with weather conditions (wind speed/direction, rainfall).
   - Derive crosswind/headwind components relative to runway orientation.
   - Identify trends and correlations between rerouting and weather.

4. **Visualisation**
   - Generate Python plots (Matplotlib/Seaborn) for exploratory analysis.
   - Create interactive JavaScript charts (Plotly) for reroute reasons and heat maps.
   - Produce probability timelines for forecasted reroute risk.

5. **Forecasting**
   - Train baseline models (logistic regression, gradient boosting) to predict rerouting.
   - Apply models to next‑week Met Éireann forecasts.
   - Present reroute risk scenarios (optimistic/central/pessimistic).

---

## Repository Structure
- `notebooks/flight_reroute_dub.ipynb` — main notebook with analysis and plots.
- `data/` — raw and processed datasets (flight events, weather).
- `src/` — modular Python scripts:
  - `data_loaders.py` — load and normalise datasets.
  - `features.py` — feature engineering (crosswind, headwind).
  - `modeling.py` — training and evaluation of reroute prediction models.
  - `viz_js.py` — JavaScript/Plotly visualisation snippets.
- `docs/` — supporting documentation:
  - `methodology.md` — detailed methodology.
- `README.md` — project overview and instructions.

---

## Requirements
- Python 3.9+
- Packages: pandas, numpy, matplotlib, seaborn, scikit‑learn, plotly
- Data sources:
  - Met Éireann historical and forecast datasets
  - Dublin Airport flight activity dashboards

---

## How to Run
1. Clone the repository.
2. Install required packages:
   ```bash
   pip install -r requirements.txt
   ```
3. place raw data CSVs in the `data/` folder.
4. Open and run the `notebooks/flight_reroute_dub.ipynb` notebook step‑by‑step.

---

## Assessment Alignment

- **Code (40%):** Modular, efficient, reusable functions; clear feature engineering; Python + JS plots.
- **Documentation (40%):** Succinct explanations, plots with captions, limitations noted.
- **Research (10%):** Sources cited inline (Met Éireann, flight dashboards).
- **Consistency (10%):** Clean repo, meaningful commits, notebook saved with outputs.

---

## Limitations & Notes

- Public flight dashboards may not expose all reroute reasons; annotated CSVs supplement.
- Forecast uncertainty acknowledged; reroute projections are indicative, not operational guarantees.
- Visibility data may require proxies (pressure + rain + time‑of‑day).

## License

This project is for educational purposes as part of the Higher Diploma in Data Analytics coursework.