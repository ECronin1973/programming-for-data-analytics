# ✈️ Flight Delay Prediction Using Weather Data

## Table of Contents

1. [Objective](#1-objective)  
2. [Assessment Criteria Mapping](#2-assessment-criteria-mapping)  
3. [Workflow Outline](#3-workflow-outline)  
   - [Weather Acquisition and Cleaning](#1-weather-acquisition-and-cleaning-steps-2-to-10i)  
   - [Flight Data Acquisition](#2-flight-data-acquisition-step-11)  
   - [Flight Batching](#3-flight-batching-steps-12-to-13)  
   - [Arrivals Workflow](#4-arrivals-workflow-steps-14-to-17)  
   - [Departures Workflow](#5-departures-workflow-steps-18-to-23)  
   - [Integration](#6-integration-steps-24-to-29)  
   - [Weather Impact Plots](#7-weather-impact-plots-steps-30a-to-30d)  
   - [Correlation Analysis](#8-correlation-analysis-steps-31a-to-31c)  
   - [Modelling](#9-modelling-steps-32-to-39)  
   - [Conclusion](#10-conclusion)  
4. [Data Sources](#4-data-sources)  
5. [Key Functions / Components](#5-key-functions--components)  
6. [Cleaning & Auditing Highlights](#6-cleaning--auditing-highlights)  
7. [Exploratory Analysis](#7-exploratory-analysis)  
8. [Integrated Risk Scoring](#8-integrated-risk-scoring)  
9. [Modelling & Metrics](#9-modelling--metrics)  
10. [Findings](#10-findings)  
11. [Limitations](#11-limitations)  
12. [Future Enhancements](#12-future-enhancements)  
13. [How to Run](#13-how-to-run)  
14. [Repository Structure](#14-repository-structure-project-segment)  
15. [Reproducibility & Consistency](#15-reproducibility--consistency)  
    - [Large Batch File Handling](#large-batch-file-handling)  
    - [GitHub File Size Considerations](#-github-file-size-considerations)  
16. [Research & Attribution (Inline Usage)](#16-research--attribution-inline-usage)  
17. [Conclusion](#17-conclusion)  
18. [Quick Start Summary](#18-quick-start-summary)

---

## 1. Objective
Integrate hourly Dublin Airport weather data with arrivals & departures delay data (May–Oct 2025) to:
- Acquire, clean, audit, merge multi‑source datasets.
- Perform exploratory, correlation, and predictive modelling (Linear Regression, Random Forest, CatBoost).
- Benchmark models, interpret feature importance, and apply tuned models to forecast scenarios.
- Present concise, reproducible analysis aligned to assessment criteria.

## 2. Assessment Criteria Mapping
| Criterion | Implementation Summary |
|-----------|------------------------|
| 40% Code | Modular steps (Sectioned workflow), robust cleaning (`clean_data` for weather, arrivals, departures; missing audits; hourly flooring; risk scoring), feature engineering, modelling (baseline + ensembles + tuning). |
| 40% Documentation | Structured workflow mirrors notebook sections with succinct rationale, inline pros/cons, statistical interpretation, plots saved to `plots/`. |
| 10% Research | Each major step cites specific sources with contextual use (data acquisition, cleaning, time series, modelling, tuning, interpretation). |
| 10% Consistency | Hourly binning audit, dry‑run toggles (`RUN_DOWNLOAD`, `RUN_BATCHING`), reproducible parameter grids, saved artefacts, consistent naming, transparent logging, version‑friendly batching strategy. |

## 3. Workflow Outline

### 1. Weather Acquisition and Cleaning (Steps 2 to 10i)
- Imported hourly weather data from Met Éireann.  
- Detected headers, parsed datetime fields, and coerced numeric values for consistency.  
- Dropped redundant indicator columns and audited missing values.  
- Conducted exploratory data analysis (EDA) with distributions, boxplots, rolling averages, wind roses, and categorical WMO codes.  
- Built an integrated **risk scoring system** to flag adverse conditions (e.g., low visibility, strong winds, heavy rainfall).

### 2. Flight Data Acquisition (Step 11)
- Queried Aviation Edge API for arrivals and departures at Dublin Airport.  
- Implemented a **dry‑run option** to avoid unnecessary API calls during testing.  
- Logged cumulative JSON responses to ensure reproducibility and transparency.

### 3. Flight Batching (Steps 12 to 13)
- Extracted schema from raw flight data.  
- Split large JSON files into monthly batches for GitHub compatibility.  
- Audited file sizes to maintain reproducibility and prevent oversized commits.

### 4. Arrivals Workflow (Steps 14 to 17)
- Inspected and cleaned arrival delay data.  
- Reconstructed delay fields, applied hourly flooring, and converted categorical variables.  
- Combined monthly batches into a unified arrivals dataset.  
- Audited results to ensure schema consistency and reproducibility.

### 5. Departures Workflow (Steps 18 to 23)
- Mirrored the arrivals workflow for departures to maintain **schema parity**.  
- Cleaned, reconstructed, and combined departure delay data.  
- Ensured consistency across both arrivals and departures datasets.

### 6. Integration (Steps 24 to 29)
- Aligned arrivals, departures, and weather data on an **hourly basis**.  
- Verified flooring accuracy and merged datasets into a single unified table.  
- Produced the final dataset for modelling and analysis.

### 7. Weather Impact Plots (Steps 30a to 30d)
- Generated scatterplots and regression lines to show how individual weather variables (e.g., visibility, humidity) impact delays.  
- Reported $R^2$ values to quantify explanatory power.  
- Provided reviewer‑friendly visual context before correlation analysis.

### 8. Correlation Analysis (Steps 31a to 31c)
- Created heatmaps to show correlations between weather features and delays.  
- Compared arrivals vs departures to highlight differences in sensitivity.  
- Identified visibility and humidity as dominant predictors.

### 9. Modelling (Steps 32 to 39)
- Conducted readiness audit and feature selection.  
- Split data into training and testing sets.  
- Built baseline **Linear Regression** models (transparent but weak explanatory power).  
- Applied **Random Forest** (stronger non‑linear performance, feature importance analysis).  
- Introduced **CatBoost** (advanced gradient boosting, modest gains for arrivals).  
- Visualised feature importance and benchmarked models side‑by‑side.  
- Tuned hyperparameters using GridSearchCV (Random Forest) and a safe manual loop (CatBoost).  
- Summarised metrics (R², RMSE) for arrivals and departures.

### 10. Conclusion
- Synthesised findings across weather, flight, and merged datasets.  
- Highlighted limitations (weather‑only scope, aggregation sensitivity).  
- Outlined practical value (transparent workflow, reproducible modelling, operationalisation with forecasts).  
- Proposed future enhancements (adding operational features, richer weather data, ensemble stacking, dashboard deployment).

---

## 4. Data Sources

| Source | Purpose | Role in Workflow |
|--------|---------|------------------|
| **Met Éireann hourly (hly532.csv)** | Provides environmental predictors including temperature, rainfall, visibility, relative humidity, wind speed/direction, and cloud height. | Formed the backbone of the weather dataset. Cleaned and audited in Steps 2–10, then used for exploratory plots (distributions, boxplots, rolling averages, wind roses) and integrated into the merged dataset for modelling. Visibility and humidity from this source emerged as the strongest predictors of delays. |
| **Aviation Edge API (DUB)** | Supplies raw arrivals and departures data for Dublin Airport, including scheduled vs actual times and delay context. | Queried in Step 11 with dry‑run logging for reproducibility. Batched into monthly JSON files (Steps 12–13) to ensure GitHub compatibility. Cleaned and reconstructed in the arrivals (Steps 14–17) and departures workflows (Steps 18–23), then merged with weather data for predictive modelling. |
| **WMO Code Tables** | Standardised categorisation of weather events (present and past codes). | Applied during weather cleaning (Step 10i) to classify conditions such as fog, mist, or precipitation. Enabled categorical analysis and risk scoring, ensuring consistency across weather records and providing operational context for delay analysis. |
| **Risk Scoring Framework (derived)** | Composite index built from thresholds (e.g., visibility < 2000 m, wind ≥ 25 knots, heavy rain ≥ 25 mm). | Developed in Step 10h to quantify adverse conditions. Produced histograms and exceedance tables that summarised combined weather hazards, later used to contextualise modelling results. |
| **Schema & Audit Exports (derived)** | Text exports of schema and missingness audits from raw JSON flight data. | Ensured reproducibility and transparency in Steps 12–13. Allowed reviewers to verify data integrity and understand how large raw files were structured before batching. |

### 📑 Reviewer Takeaway
The project integrates **multiple complementary sources**:  
- **Met Éireann** provided the environmental context.  
- **Aviation Edge API** supplied operational flight delay data.  
- **WMO Code Tables** standardised weather event categorisation.  
- Derived **risk scores and schema audits** strengthened transparency and reproducibility.  

Together, these sources enabled a **merged dataset** that supported exploratory analysis, correlation studies, and predictive modelling of flight delays.

---

## 5. Key Functions / Components

The notebook defines several core functions and reusable components that structure the workflow. Each plays a specific role in ensuring data quality, reproducibility, and reviewer‑friendly outputs.

- **[`clean_data`](project/project.ipynb)**  
  *Variants for weather and arrivals data.*  
  - Parses datetime fields and applies seasonal filters.  
  - Coerces numeric values and drops noisy indicator columns.  
  - Provides a consistent, reproducible cleaning pipeline for both weather and arrivals datasets.  
  - Ensures transparency by handling missingness and schema consistency early in the workflow.

- **[`clean_departures`](project/project.ipynb)**  
  - Tailored cleaning function for departure data.  
  - Reconstructs delay fields, applies hourly flooring, and converts categorical variables.  
  - Mirrors the arrivals workflow to maintain schema parity across datasets.  
  - Critical for ensuring departures can be integrated seamlessly with arrivals and weather data.

- **[`plot_monthly_wind_roses`](project/project.ipynb)**  
  - Generates polar plots of wind regimes for each month.  
  - Highlights operationally relevant thresholds (≥20/25 knots).  
  - Provides reviewer‑friendly visualisations of directional wind patterns.  
  - Supports operational context by linking weather conditions to airport runway usage and planning.

- **[`tune_catboost`](project/project.ipynb)**  
  - Implements a safe manual loop for CatBoost hyperparameter tuning.  
  - Avoids integration issues with `GridSearchCV` while ensuring reproducibility.  
  - Selects best models based on R² scores, with safeguards against invalid runs.  
  - Demonstrates transparency in advanced modelling by documenting parameter choices and runtime trade‑offs.

- **Risk Scoring Block (Step 10h)**  
  - Composite index built from adverse‑condition thresholds (e.g., visibility < 2000 m, wind ≥ 25 knots, heavy rain ≥ 25 mm).  
  - Produces histograms and exceedance tables summarising combined weather hazards.  
  - Provides operational insight into how multiple adverse conditions interact.  
  - Strengthens transparency by quantifying risk in a reproducible, reviewer‑friendly format.

### 📑 Reviewer Takeaway
These functions and components form the **technical backbone of the project**. They ensure that cleaning, visualisation, modelling, and risk scoring are **modular, reproducible, and transparent**. By centralising definitions inside [project/project.ipynb](project/project.ipynb), the workflow remains easy to audit, extend, and adapt for future enhancements.

---

## 6. Cleaning & Auditing Highlights

### Forms of Missing Data
Across the literature, missing data is consistently classified into three main types:  
- [**MCAR (Missing Completely at Random):**](https://www.researchgate.net/publication/392514236_Understanding_and_Managing_Missing_Data_A_Practical_Guide_to_MCAR_MAR_and_MNAR_Mechanisms) the absence is unrelated to any variable, often due to random technical errors.  
- [**MAR (Missing at Random):**](https://www.researchgate.net/publication/392514236_Understanding_and_Managing_Missing_Data_A_Practical_Guide_to_MCAR_MAR_and_MNAR_Mechanisms) missingness depends on observed variables, such as survey responses skipped by certain groups.  
- [**MNAR (Missing Not at Random):**](https://www.researchgate.net/publication/392514236_Understanding_and_Managing_Missing_Data_A_Practical_Guide_to_MCAR_MAR_and_MNAR_Mechanisms) the missingness is tied to the unobserved value itself, e.g., exam scores missing because students didn’t attend.  

### Published Strategies from Leading Authorities
- **DataCamp** [Top Techniques to Handle Missing Values Every Data Scientist Should Know](https://www.datacamp.com/tutorial/techniques-to-handle-missing-data-values) outline that missingness can appear as blanks, coded placeholders, or systemic gaps.  
- **Quora** [Effective strategies for handling missing data in data science](https://www.quora.com/What-are-some-effective-strategies-for-handling-missing-data-in-a-dataset-within-the-field-of-data-science) state that survey non‑responses and operational errors are common; MAR is most frequent, MNAR most problematic.  
- **GeeksforGeeks** [Handling Missing Values in Machine Learning](https://www.geeksforgeeks.org/machine-learning/handling-missing-values-machine-learning/) state that technical flags like NaN, NULL, or “UNKNOWN” require classification before using `dropna` or `fillna`.  
- **Python Data Science Handbook** [Handling Missing Data](https://jakevdp.github.io/PythonDataScienceHandbook/03.04-missing-values.html) states that Pandas uses sentinel values (NaN, None), simplifying handling but limiting representable ranges.  
- **MachineLearningPlus** [Missing Data Imputation Approaches](https://www.machinelearningplus.com/machine-learning/missing-data-imputation-how-to-handle-missing-values-in-python/)state NMAR cases (e.g., avoided responses) are hardest to handle and require mechanism awareness.  
- **Towards Data Science** [Handling Missing Data](https://towardsdatascience.com/handling-missing-data-f998715fb73f/) state entry errors and omissions are frequent; dropping rows assumes MCAR, which is rarely true.  
- **Analytics Vidhya** [5 Effective Strategies to Handle Missing Values in Data Analysis](https://www.analyticsvidhya.com/blog/2021/10/handling-missing-value/) state that corrupted data and human error are added factors; sometimes missingness itself can be treated as a feature.  
- **Kaggle** [A Guide to Handling Missing Values in Python](https://www.kaggle.com/code/parulpandey/a-guide-to-handling-missing-values-in-python) state that detection can be numeric or visual (e.g., Missingno), stressing diagnosis before handling.  

### Handling Strategies & Limitations
Common strategies include:  
- **Deletion** (listwise/pairwise) – simple but risks bias unless MCAR.  
- **Simple imputation** (mean, median, mode) – preserves dataset size but distorts variance.  
- **Advanced imputation** (regression, k‑NN, MICE) – more robust but computationally heavy.  
- **Algorithmic handling** (e.g., XGBoost) – model‑specific, not universally applicable.  
- **Sentinel substitution** (NaN/None) – practical but constrains values.  
- **Treating missingness as a feature** – can capture signal but risks overfitting.  

Limitations are consistent across sources: deletion discards information, naive imputation introduces bias, and advanced methods demand careful validation. The consensus is that the choice of strategy must balance dataset integrity, statistical power, and model requirements, with explicit documentation of trade‑offs for reviewer transparency.

---

### Cleaning Approach Taken in This Project

In this project, the cleaning strategy was deliberately conservative and transparent, prioritising reproducibility and reviewer clarity over complex imputation. The focus was on ensuring datasets were consistent, auditable, and compatible with weather data aggregated at hourly intervals.

### Dataset Missingness Classification and Handling

| Dataset        | Missingness Type(s) | Handling Strategy Applied                          | Limitation / Trade‑off                                      |
|----------------|----------------------|---------------------------------------------------|-------------------------------------------------------------|
| **Weather Data** | Mostly **MCAR** (random technical errors, mixed‑type numeric fields, malformed datetime formats) | Robust datetime parsing with fallbacks, safe numeric coercion, dropping redundant indicator columns | Random gaps treated as noise; excluded records reduced sample size slightly |
| **Flight Arrivals** | Primarily **MAR** (missing actual times linked to flight status or airline reporting) + some **MNAR** (systematic absence of actual times) | Imputed missing actual times from scheduled values; reconstructed delays; removed “unknown” status flights | Imputation skewed delays by underestimating true values; exclusion reduced dataset size |
| **Flight Departures** | Primarily **MAR** (missing actual times tied to operational metadata) + some **MNAR** (systematic gaps in reporting) | Same approach as arrivals: imputation from scheduled times, delay reconstruction, categorical conversion | Bias introduced by imputation; flooring times reduced real‑time granularity |
| **Integrated Dataset (Flights + Weather)** | Combination of **MCAR** (random weather gaps) and **MAR/MNAR** (flight reporting issues) | Hourly flooring of all times to align with weather totals; schema parity across arrivals/departures | Reduced temporal precision; sub‑hour disruptions masked for compatibility with weather data |


---

**Weather Data Cleaning**  
- **Datetime parsing with fallbacks:** Supported multiple formats (`YYYY-MM-DD HH:MM:SS` and `DD-MMM-YYYY HH:MM`) to avoid silent failures.  
- **Seasonal filtering:** Retained only May–October data for the latest year to match the study period.  
- **Dropping redundant indicator columns:** Removed noisy fields (`ind`, `ind.1`, etc.) to reduce clutter.  
- **Safe numeric coercion:** Converted mixed‑type columns (visibility, rainfall, temperature) using `pd.to_numeric(errors="coerce")`.  
- **Special handling of wind speed (`wdsp`):** Explicit conversion due to frequent mixed types.  
- **Auditing:** Produced missingness tables and schema exports to document gaps transparently.  

---

**Flight Arrivals Data Cleaning**  
- **Drop unused technical columns:** Removed codeshared identifiers, airline codes, gate/runway/baggage details, and other metadata not required for analysis.  
- **Parse datetime columns:** Converted scheduled and actual arrival times into proper datetime objects, with fallback parsing for alternative formats.  
- **Remove flights with unknown status:** Excluded records marked as “unknown” to avoid unreliable entries.  
- **Convert categorical fields:** Standardised fields such as flight type, status, and airline name into categorical variables.  
- **Impute missing actual arrival times:** Where actual times were missing, they were filled with scheduled times. This ensured continuity but introduced bias, as delays computed afterwards were artificially reduced.  
- **Reconstruct missing delays:** Calculated delays in minutes by subtracting scheduled from actual times. Because actual times were sometimes imputed from scheduled values, this skewed potential results by underestimating true delays.  
- **Round times to hourly bins:** Floored both scheduled and actual arrival times to hourly intervals. This reduced real‑time granularity but was necessary to align flights with weather hourly totals.  
- **Audit imputation:** Added flags to indicate where times or delays were imputed, ensuring transparency for reviewers.  

---

**Flight Departures Data Cleaning**  
- **Drop unused technical columns:** Removed codeshared identifiers, airline codes, gate/runway/baggage details, and other metadata not required for analysis.  
- **Parse datetime columns:** Converted scheduled and actual departure times into proper datetime objects with robust error handling.  
- **Remove flights with unknown status:** Excluded unreliable records marked as “unknown.”  
- **Convert categorical fields:** Standardised fields such as flight type, status, and airline name into categorical variables.  
- **Impute missing actual departure times:** Where actual times were missing, they were filled with scheduled times. As with arrivals, this introduced bias by reducing observed delays.  
- **Reconstruct missing delays:** Computed delays in minutes from scheduled vs actual times, filling gaps where official delay values were missing.  
- **Round times to hourly bins:** Floored both scheduled and actual departure times to hourly intervals, reducing real‑time detail but ensuring compatibility with weather data.  
- **Drop intermediate audit flags:** Removed temporary imputation markers for reviewer‑friendly outputs.  
- **Enforce final dtypes:** Ensured `computed_delay` was stored as `float64` (fractional minutes) and `departure.delay` as `int64` (whole minutes).  

---

### Cleaning Steps, Purpose, and Limitations

| Step                          | Purpose                                                                 | Limitation / Trade‑off                                                                 |
|-------------------------------|-------------------------------------------------------------------------|----------------------------------------------------------------------------------------|
| **Drop unused technical columns** | Remove irrelevant metadata (codeshared IDs, gates, baggage, etc.)        | No major limitation; reduces clutter but discards potentially useful operational detail |
| **Parse datetime columns**    | Standardise scheduled/actual times into consistent datetime objects      | Parsing errors coerced to NaT; some records excluded                                    |
| **Remove flights with unknown status** | Ensure dataset reliability by excluding uncertain records              | May reduce sample size; excludes potentially valid but incomplete flights               |
| **Convert categorical fields**| Improve efficiency and consistency in analysis                          | None significant; simplifies storage and processing                                     |
| **Impute missing actual times** | Fill NaN actual times with scheduled times to maintain continuity       | Skews delay calculations by underestimating true delays                                 |
| **Reconstruct delays**        | Compute delays in minutes from scheduled vs actual times                 | Dependent on imputed actual times; introduces bias if actual data was missing           |
| **Round times to hourly bins**| Align flights with weather hourly totals for integration                 | Reduces real‑time granularity; masks sub‑hour disruptions                               |
| **Audit imputation flags**    | Document where values were imputed for reviewer transparency             | Adds intermediate columns; later dropped for cleaner outputs                            |
| **Enforce final dtypes**      | Ensure delays stored as integers and computed_delay as floats            | None significant; improves reproducibility and clarity                                  |


📑 **Reviewer Takeaway:**  
Published methods often rely on deletion, imputation, or complex modelling. In this project, the focus was on **clear parsing, safe conversions, and transparent auditing**. Filling missing actual times with scheduled values kept the dataset complete but reduced the accuracy of delay calculations. Rounding times to hourly bins lowered real‑time detail, yet was necessary to match flight records with weather data.

---

## 7. Exploratory Analysis

This section uses a series of diagnostic plots to explore the **distribution, variability, and relationships** within the weather dataset before merging with flight delays. Visualisations serve as both a quality check and a narrative tool, ensuring transparency for reviewers and guiding later modelling choices.

The plots include:
- **Distributions (combined + individual histograms):** Document the spread of key weather variables and highlight skewness or outliers.  
- **Boxplots:** Surface outliers and show variability across core features.  
- **Daily min/mean/max temperature profiles:** Capture thermal cycles and extremes.  
- **Rolling 7‑day smoothing:** Clarify medium‑term weather trends.  
- **Wind histogram + monthly wind roses:** Reveal operationally relevant wind regimes, with thresholds at 20/25 knots.  
- **Humidity–Visibility scatterplots:** Demonstrate the strong inverse relationship between humidity and visibility.  
- **Weather code counts (present vs past):** Separate and quantify WMO code categories for operational context.  

All plots are saved to `project/plots/` with systematic naming conventions (`sXX_<descriptor>.png`) to ensure reproducibility and easy reference throughout the notebook.

---

### 📊 Distribution of Key Weather Variables (Including Wind Speed)
![Distribution of Key Weather Variables (Including Wind Speed)](plots/s6b_distributions_combined.png)

**Plot Purpose**  
Illustrates the distribution of core weather variables, including wind speed.  
Serves as a diagnostic step before correlation analysis (Step 7), confirming variables are suitable for statistical comparison.  
Provides transparency by documenting distributional properties and highlighting skewness or outliers that may influence modelling.

---

### 🌡️ Temperature Distribution
![Temperature Distribution](plots/s6b_temp.png)

**Plot Purpose**  
Shows the distribution of temperature values.  
Highlights skewness and potential outliers that could affect regression models.  
Establishes baseline variability for later correlation and predictive analysis.

---

### 💧 Relative Humidity Distribution
![Relative Humidity Distribution](plots/s6b_rhum.png)

**Plot Purpose**  
Displays the range and central tendency of humidity values.  
Helps reviewers understand the spread and typical conditions.  
Supports later analysis of humidity’s strong correlation with visibility and delays.

---

### 💨 Vapour Pressure Distribution
![Vapour Pressure Distribution](plots/s6b_vappr.png)

**Plot Purpose**  
Illustrates variability in vapour pressure.  
Provides thermodynamic context for temperature and humidity relationships.  
Ensures consistency checks before modelling.

---

### 🌧️ Rainfall Distribution
![Rainfall Distribution](plots/s6b_rain.png)

**Plot Purpose**  
Shows precipitation frequency and intensity.  
Highlights skewed distribution typical of rainfall data.  
Provides context for evaluating rainfall’s limited but important role in delays.

---

### 🌬️ Wind Speed Distribution
![Wind Speed Distribution](plots/s6b_wdsp.png)

**Plot Purpose**  
Reveals typical wind regimes and distribution tails.  
Supports later wind rose plots and operational context.  
Highlights variability relevant to airport operations.

---

### 🔗 Weather Variable Correlation Heatmap
![Weather Correlation Heatmap](plots/s7_corr_heatmap.png)

**Plot Purpose**  
Displays pairwise correlations among weather features.  
Highlights strong inverse relationship between humidity and visibility.  
Provides diagnostic insight before merging with flight delay data.

---

### 🌡️ Temp vs Relative Humidity (Scatter/Regression)
![Temp vs RH](plots/s8_temp_vs_rhum.png)

**Plot Purpose**  
Explores non‑linear relationship between temperature and humidity.  
Confirms expected thermodynamic patterns.  
Supports feature engineering decisions.

---

### 👁️ Visibility vs Relative Humidity (Scatter/Regression)
![Visibility vs RH](plots/s8_vis_vs_rhum.png)

**Plot Purpose**  
Demonstrates inverse relationship between visibility and humidity.  
Provides operational context for weather‑driven delays.  
Highlights humidity as a dominant predictor.

---

### 📈 Weather Trends (Time Series Overview)
![Weather Trends](plots/s9_weather_trends.png)

**Plot Purpose**  
Provides a multi‑variable overview across the study period.  
Highlights seasonal cycles and anomalies.  
Supports narrative synthesis of weather impacts.

---

### 📦 Boxplots of Core Weather Variables
![Boxplots](plots/s10a_boxplots.png)

**Plot Purpose**  
Highlights outliers and spread across weather variables.  
Provides transparency in data quality.  
Supports reviewer understanding of variability.

---

### 🌡️ Daily Temperature Range (Min/Mean/Max)
![Daily Temp Range](plots/s10b_daily_temp_range.png)

**Plot Purpose**  
Shows daily thermal variability.  
Highlights seasonal cycles and extremes.  
Provides operational context for flight scheduling.

---

### 🌧️ Daily Rainfall Totals
![Daily Rainfall](plots/s10c_daily_rainfall.png)

**Plot Purpose**  
Summarises precipitation per day.  
Highlights wet vs dry periods.  
Supports correlation with delay patterns.

---

### 💧 Humidity vs Visibility (Scatter)
![Humidity vs Visibility](plots/s10d_humidity_vs_visibility.png)

**Plot Purpose**  
Quantifies visibility degradation with increased humidity.  
Provides operational insight into fog and mist conditions.  
Supports predictive modelling of arrival delays.

---

### 📈 Temperature Rolling Average (7‑day)
![Temp Rolling Avg](plots/s10e_temp_rolling_avg.png)

**Plot Purpose**  
Smooths temperature trends to reveal medium‑term signals.  
Highlights seasonal transitions.  
Provides context for delay seasonality.

---

### 💧 Relative Humidity vs Visibility (Alt Scatter)
![RH vs Visibility](plots/s10f_rhum_vs_vis.png)

**Plot Purpose**  
Alternate scaling and filters for RH–visibility relationship.  
Confirms robustness of correlation.  
Provides reviewer transparency.

---

### 🌡️ Temperature vs Relative Humidity (Scatter)
![Temp vs RH](plots/s10f_temp_vs_rhum.png)

**Plot Purpose**  
Cross‑checks temperature–humidity gradients.  
Validates consistency across different visualisations.  
Supports thermodynamic context.

---

### 🌡️ Temperature vs Vapour Pressure (Scatter)
![Temp vs Vapour Pressure](plots/s10f_temp_vs_vappr.png)

**Plot Purpose**  
Validates thermodynamic consistency between temperature and vapour pressure.  
Provides reviewer confidence in dataset integrity.  

---

### 🌬️ Wind Speed Histogram
![Wind Speed Histogram](plots/s10g_wdsp_histogram.png)

**Plot Purpose**  
Shows frequency distribution of wind speeds.  
Highlights operationally relevant regimes.  
Supports wind rose analysis.

---

### 🌬️ Monthly Wind Roses (May–October)
![Wind Rose May](plots/s10g_windrose_2025-05-01.png)  
![Wind Rose June](plots/s10g_windrose_2025-06-01.png)  
![Wind Rose July](plots/s10g_windrose_2025-07-01.png)  
![Wind Rose August](plots/s10g_windrose_2025-08-01.png)  
![Wind Rose September](plots/s10g_windrose_2025-09-01.png)  
![Wind Rose October](plots/s10g_windrose_2025-10-01.png)

**Plot Purpose**  
Illustrates directional wind regimes for each month.  
Provides operational context for runway usage and flight planning.  
Highlights seasonal shifts in prevailing winds.

---

### ⚠️ Risk Score Distribution
![Risk Score Distribution](plots/s10h_risk_score_distribution.png)

**Plot Purpose**  
Histogram of composite adverse‑condition risk.  
Summarises combined weather hazards.  
Supports operational risk assessment.

---

### 🌍 Weather Codes Counts (Present vs Past)
![Weather Codes Counts](plots/s10i_weather_codes_counts_full_separate.png)

**Plot Purpose**  
Shows frequency of WMO code categories.  
Highlights prevalence of adverse conditions.  
Provides operational context for delay analysis.

---

### ✈️ Daily Arrivals vs Departures (Counts)
![Daily Arrivals vs Departures](plots/s26a_daily_arrivals_vs_departures.png)

**Plot Purpose**  
Displays operational volume trends by day.  
Provides baseline context for delay analysis.  
Highlights traffic variability.

---

### ⏱️ Average Hourly Delay (All Flights)
![Average Hourly Delay](plots/s26b_average_hourly_delay.png)

**Plot Purpose**  
Shows typical delay profile by hour.  
Highlights peak congestion periods.  
Supports operational context for modelling.

---

### 🛫 Top Airlines by Flight Volume
![Top Airlines Volume](plots/s26c_top_airlines_flight_volume.png)

**Plot Purpose**  
Identifies carriers with highest activity.  
Provides operational context for delay benchmarking.  

---

### 🛫 Top Airlines by Average Delay
![Top Airlines Avg Delay](plots/s26d_top_airlines_average_delay.png)

**Plot Purpose**  
Compares delay performance by carrier.  
Highlights variability across airlines.  
Supports operational feature expansion.

---

### 🌡️ Arrival Delay vs Temperature
![Arrival Delay vs Temp](plots/s30a_arrival_delay_vs_temperature.png)

**Plot Purpose**  
Assesses temperature impact on arrival delays.  
Provides reviewer transparency on weak correlations.  

---

### 🌧️ Departure Delay vs Rainfall
![Departure Delay vs Rain](plots/s30b_departure_delay_vs_rainfall.png)

**Plot Purpose**  
Evaluates rainfall influence on departure delays.  
Highlights limited predictive power of precipitation.  

---

### 👁️ Arrival Delay vs Visibility
![Arrival Delay vs Visibility](plots/s30c_arrival_delay_vs_visibility.png)

**Plot Purpose**  
Quantifies visibility effect on arrivals.  
Confirms visibility as a dominant predictor.  

---

### 💧 Departure Delay vs Relative Humidity
![Departure Delay vs RH](plots/s30d_departure_delay_vs_relative_humidity.png)

**Plot Purpose**  
Tests humidity sensitivity for departures.  
Highlights weak explanatory power.  

---

### 🔗 Correlation Matrix: Arrivals + Weather
![Arrivals Corr Matrix](plots/s31a_correlation_matrix_arrivals_weather.png)

**Plot Purpose**  
Shows correlations between arrival delays and weather features.  
Highlights visibility and humidity as strongest drivers.  

---

### 🔗 Correlation Matrix: Departures + Weather
![Departures Corr Matrix](plots/s31b_correlation_matrix_departures_weather.png)

**Plot Purpose**  
Shows correlations between departure delays and weather features.  
Highlights weaker associations compared to arrivals.  

---

### 🌲 Feature Importance (Random Forest – Arrivals & Departures)
![Feature Importance](plots/s37_feature_importance_arrivals_departures.png)

**Plot Purpose**  
Ranks the relative influence of weather features on delay predictions.  
Highlights visibility and humidity as dominant drivers.  
Provides interpretability for Random Forest outputs.

---

## 8. Integrated Risk Scoring
Flags: wind (≥20, ≥25), extreme temp (≤0/≥30), visibility (≤5000, ≤2000), heavy rain (≥25 mm), low cloud (≤500 m). Aggregate score = sum of binary flags; histogram + exceedance % table persisted.

## 9. Modelling & Metrics
| Model | Arrivals $R^2$ | Arrivals RMSE | Departures $R^2$ | Departures RMSE | Notes |
|-------|----------------|---------------|------------------|-----------------|-------|
| Linear Regression | ~0.0025 | ~32 min | ~0.0033 | ~25.8 min | Baseline, negligible variance explained. |
| Random Forest (default) | ~0.113 | ~30.1 min | ~0.038 | ~25.3 min | Nonlinear gains (visibility & humidity). |
| CatBoost (default) | ~0.060 | ~31.0 min | <0 | ~25.9 min | Limited signal with weather-only. |
| Random Forest (tuned) | ~0.114 | ~30.1 min | ~0.062 | ~25.0 min | Marginal improvement departures. |
| CatBoost (tuned) | ~0.076 | ~30.7 min | ~0.003 | ~25.8 min | Still weaker than RF. |

Feature Importance (Random Forest):
- Arrivals: Visibility ≈51%, Humidity ≈41%, Temp ≈4%, Rain ≈3%.
- Departures: Visibility ≈60%, Humidity ≈29%, Temp ≈7%, Rain ≈4%.

## 10. Findings
- Weather-only predictors yield modest explanatory power (ceiling ≈11% $R^2$ arrivals).
- Visibility + humidity dominate; temperature & rainfall minor additive variance.
- Departures less weather-sensitive; operational factors missing.
- Hourly aggregation reduces temporal granularity (dampens micro disruptions).

## 11. Limitations
- No airline schedule, traffic density, ATC constraints, maintenance states (major delay drivers absent).
- Hourly flooring obscures sub-hour patterns.
- Simplified thresholds (generic, not airport-specific SOP).
- CatBoost underperforms due to limited feature set.

## 12. Future Enhancements
| Enhancement | Impact |
|-------------|--------|
| Add operational features (airline, turnaround time, seasonal demand) | Increase predictive signal beyond weather. |
| Integrate ATC / capacity metrics | Capture systemic congestion effects. |
| Sub-hour timestamp precision | Recover fine-grained delay triggers. |
| Advanced ensemble stacking (RF + CatBoost) | Robust variance capture. |
| Database layer (PostgreSQL / SQLite) | Queryable reproducibility & scaling. |
| Dashboard (interactive forecast + risk ledger) | Operationalisation & usability. |

## 13. How to Run
```bash
# (from repo root)
pip install -r requirements.txt
jupyter notebook project/project.ipynb
```
Optional environment:
```bash
set AVIATION_EDGE_API_KEY=YOUR_KEY   # Windows
export AVIATION_EDGE_API_KEY=YOUR_KEY # macOS/Linux
```
Inside notebook:
- Set RUN_DOWNLOAD / RUN_BATCHING flags.
- Execute cells sequentially; outputs & plots saved to `project/plots/`.

---

## 14. Repository Structure (Project Segment)
| Path | Purpose |
|------|---------|
| `project/project.ipynb` | Full workflow (acquire → clean → integrate → model → conclude). |
| `project/README.md` | Summary & assessment alignment (this file). |
| `project/data/` | Cleaned CSVs, batched flight JSONs, risk tables. |
| `project/plots/` | Generated PNG artefacts (EDA, correlations, modelling). |
| `project/docs/methodology.md` | Extended methodological narrative (see linked path). |

---

## 15. Reproducibility & Consistency
- Dry‑run toggles prevent forced API dependency.
- Monthly batching reduces large‑file friction.
- Explicit header detection & schema exports.
- Hourly bin audits guarantee deterministic merges.
- Parameter grids documented; tuned models reproducible.
- Plots named systematically: `sXX_<descriptor>.png`.

### Large Batch File Handling
Raw JSON files from the Aviation Edge API are very large and exceed typical GitHub file size limits.  
To prevent oversized commits and repeated processing of inaccessible files, the workflow includes a batching mechanism that splits data into monthly segments.  

#### 📂 GitHub File Size Considerations
[GitHub](https://docs.github.com/en/repositories/working-with-files/managing-large-files/about-large-files-on-github) imposes practical limits on repository file sizes:
- **Individual file limit:** ~100 MB (hard limit for pushes).  
- **Recommended repository size:** <1 GB for smooth cloning and usage.  
- **Large files:** Can cause slow downloads, version control friction, and may be rejected by GitHub.

https://docs.github.com/en/repositories/working-with-files/managing-large-files/about-large-files-on-github

### Project Strategy
To remain compatible with GitHub and ensure reproducibility:
- **Monthly Batching:** Raw flight JSON files from the Aviation Edge API were split into monthly segments (Steps 12–13). This keeps each file well below the 100 MB threshold.  
- **Schema & Audit Exports:** Instead of storing oversized raw files, schema text exports and missingness audits were saved. This allows reviewers to verify structure without needing full raw data.  
- **Toggle Control:**  
  - `RUN_BATCHING = False` by default, preventing re‑batching of already large or inaccessible files.  
  - **Re‑running batching is not available in this repository** — batching has already been performed, and the resulting monthly files are included for analysis.  
  - `RUN_BATCHING = True` only if you have your own downloaded dataset and need to split it into monthly batches locally.  

### 📑 Reviewer Takeaway
This design ensures the repository remains lightweight, reproducible, and version‑friendly:
- Reviewers can run the notebook directly using the **batched files already provided** without hitting GitHub file size limits.  
- Users with their own datasets can enable batching to reproduce the full pipeline.  
- The workflow balances **transparency** (schema exports, risk tables) with **practical usability** (manageable file sizes).

---

## 16. Research & Attribution (Inline Usage)

The following resources were consulted and applied directly within the notebook. Each citation is tied to a specific workflow step, ensuring transparency and reproducibility for reviewers.

| Resource | Applied In | Role in Workflow |
|----------|------------|------------------|
| [**Project Specification Document**](https://vlegalwaymayo.atu.ie/pluginfile.php/1804303/mod_resource/content/2/Project%20Description.pdf) | Entire workflow | Provided the foundational requirements and assessment criteria. Guided the overall structure, deliverables, and evaluation metrics for the project. |
| **Pandas IO / Missing Data Documentation** | Weather & flight cleaning (Steps 2–6, 14–19) | Guided handling of missing values, schema consistency, and robust data import/export operations. Ensured reproducible cleaning pipelines for both weather and flight datasets. |
| **NumPy Documentation** | Weather cleaning and transformations (Steps 2–6) | Supported numerical coercion, array handling, and efficient calculations across weather variables. |
| **Python Standard Library (os, json)** | Flight batching and API handling (Steps 11–13) | `os` managed file paths and reproducibility for saving plots and batched JSON files; `json` parsed raw API responses into structured formats for cleaning and batching. |
| **Seaborn (heatmap, scatter, lineplot)** | Correlations, regression visuals (Steps 7, 8, 30) | Provided statistical visualisations for correlation matrices, scatterplots, and regression lines. Enhanced interpretability of relationships between weather variables and delays. |
| **Matplotlib (polar plots, histograms, general plotting)** | Distributions, boxplots, scatterplots, wind roses (Steps 7–10, 30) | Backbone for most static plots saved to `project/plots/`. Enabled polar wind rose plots, histograms, and regression visualisations. |
| **WMO Code Tables** | Weather code mapping (Step 10i) | Standardised classification of present and past weather events. Allowed categorical analysis of conditions such as fog, mist, and precipitation. |
| **Scikit‑Learn Documentation (LinearRegression, RandomForest, GridSearchCV)** | Baseline, ensemble modelling, tuning (Steps 34–39) | Provided implementation details for regression models, ensemble methods, and systematic hyperparameter tuning. Ensured reproducibility and fairness in model benchmarking. |
| **Scikit‑Learn Metrics Documentation** | Model evaluation (Steps 34–39) | Supplied formulas and functions for R² and RMSE, ensuring transparent evaluation of model performance. |
| **CatBoost Quickstart Guide** | Boosting model integration (Steps 35, 38, 39) | Supported integration of CatBoost into the modelling pipeline. Guided parameter selection and explained default handling of categorical features. |
| **Time Series & Rolling Guides** | Daily aggregation + smoothing (Steps 10b, 10e) | Informed rolling averages and daily aggregation methods. Helped clarify medium‑term weather trends and seasonal cycles. |
| **Aviation Edge API Documentation** | Raw flight acquisition (Step 11) | Provided schema and query details for retrieving arrivals and departures data. Supported reproducible API calls and dry‑run logging. |
| **GitHub Large‑Files Guidance** | Batching strategy justification (Steps 12–13) | Informed the decision to split raw JSON flight data into monthly batches. Ensured repository compatibility and reproducibility for large datasets. |

### 📑 Reviewer Takeaway
This section demonstrates that every major step in the workflow was **grounded in authoritative resources**. By citing documentation inline and explaining its use, the project maintains transparency, reproducibility, and reviewer confidence. Each resource directly shaped the cleaning, visualisation, modelling, or operationalisation stages of the notebook.

---

## 17. Conclusion

This project delivered a transparent, reproducible workflow for integrating Dublin Airport flight delays with hourly weather data. Each stage produced clear insights:

- **Weather Cleaning & Exploration:**  
  Weather data was successfully parsed, cleaned, and audited. Plots revealed skewed rainfall distributions, seasonal temperature cycles, directional wind regimes, and strong inverse relationships between humidity and visibility. Risk scoring quantified adverse conditions such as low visibility, strong winds, and heavy rainfall.

- **Flight Data Acquisition & Batching:**  
  Raw arrivals and departures data were acquired via the Aviation Edge API and split into monthly batches to remain GitHub‑compatible. Plots highlighted daily traffic variability, hourly delay peaks, and airline‑level differences in delay performance.

- **Integration & Flooring:**  
  Weather and flight datasets were aligned on an hourly basis using flooring. While this ensured deterministic merges and schema parity, it had an **adverse effect on results**: sub‑hour delays were collapsed into hourly bins, reducing variance, weakening correlations, and constraining predictive ceilings. Short‑lived weather events (fog patches, sudden rainfall) were dampened, limiting explanatory power.

- **Correlation Analysis:**  
  Heatmaps and scatterplots confirmed visibility and humidity as the strongest predictors of arrival delays, while temperature and rainfall played minor roles. Departures showed weaker associations, underscoring the influence of non‑weather operational factors.

- **Modelling:**  
  Linear Regression provided a transparent baseline but explained negligible variance. Random Forest captured non‑linear effects, improving explanatory power and ranking visibility and humidity as dominant drivers (≈50–60% combined importance). CatBoost offered modest gains for arrivals but underperformed for departures. Hyperparameter tuning delivered incremental improvements, yet predictive ceilings remained low without operational features.

- **External Factors:**  
  The limited explanatory power (≤11% arrivals, ≤6% departures) reflects the absence of critical operational drivers such as airline schedules, traffic density, ATC constraints, and turnaround times. These factors must be integrated in future work to achieve richer predictive capacity.

### 📑 Overall Takeaway
Weather‑only modelling sets a clear upper bound on predictive accuracy. Visibility and humidity dominate delay variance, departures are less weather‑sensitive, and flooring reduced temporal granularity, further constraining results. Despite these limitations, the project delivered a **transparent, reproducible foundation** that met all assessment requirements: structured acquisition, cleaning, exploratory analysis, correlation, modelling, and benchmarking. It provides a solid platform for future integration of operational datasets, finer temporal precision, and advanced ensemble approaches.

---

## 18. Quick Start Summary
1. Install dependencies.
2. Open notebook.
3. (Optional) Set API key & enable downloads.
4. Run sequentially; verify audits (minutes arrays = `[0]`).
5. Review plots, metrics, risk tables.
6. Extend feature set for improved predictive capacity.

---
# END