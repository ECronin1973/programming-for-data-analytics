# ✈️ Flight Punctuality Analysis at Dublin Airport

This README is for the **project** component of the repository. It focuses on the Dublin Airport punctuality analysis: aims, structure, setup, and how to run. Detailed methodology, visualisation rationale, and assessment alignment are documented in `docs/methodology.md` within this project folder. The project aligns with the Programming for Data Analytics module brief and final project guidance.

---

## 📖 Overview
The project investigates flight punctuality at Dublin Airport and its relationship to local weather conditions.  
It identifies patterns in delays and cancellations, analyses contributing factors (e.g., wind, rainfall, visibility), and forecasts potential disruption using Met Éireann data. The notebook and supporting modules emphasise modularity, reproducibility, and reviewer‑friendly documentation.

---

## Planned Objectives
1. **Data Acquisition**
   - Gather flight activity data (arrivals, departures, delays, cancellations) from Dublin Airport dashboards and APIs.
   - Download historical weather data from Met Éireann (wind, rain, temperature, pressure).
   - Collect forecast data for the Dublin region for the upcoming week.

2. **Data Cleaning & Normalisation**
   - Align flight events with nearest weather records.
   - Normalise units (wind speed, rainfall, temperature).
   - Create derived features such as heavy rain, strong wind, gusty conditions, and seasonal categories.

3. **Analysis**
   - Explore frequency and severity of delays by airline, time of day, and season.
   - Cross‑reference cancellations with weather conditions (wind speed/direction, rainfall, visibility proxies).
   - Identify trends and correlations between punctuality and adverse weather.

4. **Visualisation**
   - Generate Python plots (Matplotlib/Seaborn) for exploratory analysis.
   - Create interactive JavaScript charts (Plotly) for delay distributions and heat maps.
   - Produce probability timelines for forecasted delay risk.

5. **Forecasting**
   - Train baseline models (regression, gradient boosting) to predict delay minutes or cancellation probability.
   - Apply models to next‑week Met Éireann forecasts.
   - Present delay risk scenarios (optimistic/central/pessimistic).

---

## Repository Structure
- `notebooks/flight_punctuality_dub.ipynb` — main notebook with analysis and plots.
- `data/` — raw and processed datasets (flight events, weather).
- `src/` — modular Python scripts:
  - `data_loaders.py` — load and normalise datasets.
  - `features.py` — feature engineering (weather flags, time features).
  - `modeling.py` — training and evaluation of delay prediction models.
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
  - Dublin Airport flight activity dashboards/APIs

---

## How to Run
1. Clone the repository.
2. Install required packages:
   ```bash
   pip install -r requirements.txt
   ```
3. place raw data CSVs in the `data/` folder.
4. Open and run the `notebooks/flight_punctuality_dub.ipynb` notebook step‑by‑step.
---

## Assessment Alignment

- **Code (40%):** Modular, efficient, reusable functions; clear feature engineering; Python + JS plots.
- **Documentation (40%):** Succinct explanations, plots with captions, limitations noted.
- **Research (10%):** Sources cited inline (Met Éireann, flight dashboards).
- **Consistency (10%):** Clean repo, meaningful commits, notebook saved with outputs.

---

## Limitations & Notes

- Public flight dashboards may not expose all delay reasons; analysis relies on available status fields.
- Forecast uncertainty acknowledged; delay projections are indicative, not operational guarantees.
- Visibility data may require proxies (pressure + rain + time‑of‑day).

## Issues Encountered
- Generated .json files for dublin Airport were too large to include in the repository. Users must download these files directly from the Dublin Airport data portal.  I made five commits, but ran into issues each time in VSCode due to the large file upload attempt earlier. Unfortunately, I looked at solutions and ended up accidentally dropping the last five commits and reset everything using 'git reset --hard origin/main', which removed most of my work today. Thankfully, I had a backup and was able to restore everything.

```plain
🔎 Missing values per column:
delay            83248
delay_calc       81381
runway           36325
act              36325
season           19838
msl              19838
wdsp             19838
rain             19838
temp             19838
terminal          6239
est               5953
flight_iata       1309
airline           1203
status               0
sched                0
datetime_hour        0
datetime             0
is_cancelled         0
type                 0
dtype: int64

📊 Percentage of missing values per column:
flight_iata       0.49
airline           0.45
status            0.00
sched             0.00
est               2.21
act              13.49
delay            30.92
terminal          2.32
runway           13.49
delay_calc       30.22
datetime_hour     0.00
is_cancelled      0.00
type              0.00
datetime          0.00
temp              7.37
rain              7.37
wdsp              7.37
msl               7.37
season            7.37
dtype: float64

⚠️ Columns with missing values: ['delay', 'delay_calc', 'runway', 'act', 'season', 'msl', 'wdsp', 'rain', 'temp', 'terminal', 'est', 'flight_iata', 'airline']
```

20/11/2025 - After slicing the data to the overlapping date range between flight and weather datasets, the following counts were observed:

```plain
✈️ Flights in sliced range: 6771
🌦️ Weather observations in sliced range: 120
🔗 Matched flights with weather: 782
📈 Match rate: 11.55%

21/11/2025 - After refining the matching logic to ensure accurate datetime alignment, the following improved counts were observed:

```plain
✅ Step 23a Summary (5-Day Slice)
📆 Flight range:  2025-10-27 → 2025-10-31
📆 Weather range: 2025-10-27 → 2025-10-31
✈️ Flights in sliced range: 6771
🌦️ Weather observations in sliced range: 120
🔗 Matched flights with weather: 6771
📈 Match rate: 100.00%
🔎 Weather datetime match rate: 100.0%
🔎 Season assignment rate:     100.0%


## License

This project is for educational purposes as part of the Higher Diploma in Data Analytics coursework.