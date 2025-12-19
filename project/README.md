# ✈️ Flight Delay Prediction Using Weather Data

## Repository Overview
This repository offers a complete workflow for predicting flight delays at Dublin Airport, using hourly weather data from May to October 2025.
- Jupyter notebook (project/project.ipynb) containing the full pipeline: data acquisition, cleaning, integration, analysis, modelling, and conclusions.
- Supporting data files in project/data/: cleaned CSVs, batched flight JSONs, and risk tables.
- Generated plots in project/plots/: exploratory, correlation, and modelling results.
- Documentation in project/docs/methodology.md: detailed methodology and workflow notes.
- Environment specification files (requirements.txt and environment.yml) listing all Python dependencies required to reproduce the workflow.

The project prioritises transparency, reproducibility, and accessibility through modular functions, systematic plots, and clear documentation of trade-offs.

---

### ▶️ How to run the project (single-file environment.yml)

1. Clone the repository and navigate to the `project` folder:
   ```bash
   git clone https://github.com/EdwardCronin1973/programming-for-data-analytics.git
   cd project
    ```

*This sets the working directory to the repository’s project folder, which contains the main Jupyter notebook and supporting files.*  

2. Create the conda environment
This project uses a single environment.yml file to install all required packages. Run the following from the project folder:
```bash
conda env create -f ../environment.yml -n project
```

#### or update if it already exists
```bash
# If the env already exists and you want to recreate it cleanly:
conda env remove -n project
conda env create -f ../environment.yml -n project
```

3. Activate the environment and register the kernel 
After creation, activate the environment and ensure the Jupyter kernel is available in VS Code or Jupyter:
```bash
conda activate project
python -m pip install --upgrade pip
python -m pip install ipykernel
python -m ipykernel install --user --name=pda_project_env --display-name "Python (project)"
```

**Tip:** If conda env create fails because of strict pins, remove exact '=version' pins for problematic packages (for example matplotlib=3.9.0) or use mamba with -c conda-forge for faster, more reliable solving.

4. (Optional) Set the API key for Aviation Edge:

```bash
set AVIATION_EDGE_API_KEY=YOUR_KEY   # Windows
export AVIATION_EDGE_API_KEY=YOUR_KEY # macOS/Linux
```

- Open project/project.ipynb.
- Open project/project.ipynb in Jupyter Notebook or JupyterLab.

**Inside the notebook:**
- Execute the cells in order; outputs and plots are saved automatically to project/plots/.
- The notebook includes all executed code cells, so plots and outputs can be viewed without rerunning.

Required packages: pandas, numpy, matplotlib, seaborn, scikit-learn, catboost, and requests. Standard library packages such as json and os are included with Python and do not require installation.

---
## Repository Structure

| Path                          | Purpose                                                                 |
|-------------------------------|-------------------------------------------------------------------------|
| `project.ipynb`               | Full workflow (acquire → clean → integrate → database → model → conclude). |
| `README.md`                   | Summary & assessment alignment (this file).                            |
| `data/`                       | Cleaned CSVs, batched flight JSONs, risk tables (already included).     |
| `plots/`                      | Auto‑generated PNG artefacts (EDA, correlations, modelling).            |
| `docs/methodology.md`         | Extended methodological narrative.                                     |
| `dublin_airport.db`           | Root‑level SQLite database containing merged weather + flight tables, enforced schemas, and query outputs. |
| `requirements.txt`            | Pip dependencies pinned for reproducibility.                        |
| `environment.yml`             | Conda environment file for Python 3.11 with pinned dependencies.       |

---

### Table of Contents

1. [Objective and Approach](#1-objective-and-approach)  
2. [Assessment Criteria Mapping](#2-assessment-criteria-mapping)  
3. [Workflow Overview](#3-workflow-overview)  
4. [Database Integration](#4-database-integration)  
   - [4b. Database Example Queries & Plots](#4b-database-example-queries--plots)
5. [Data Sources & Roles in Workflow](#5-data-sources--roles-in-workflow)  
6. [Environment and Dependencies](#6-environment-and-dependencies)  
7. [Initial Visual Inspection](#7-initial-visual-inspection)  
8. [Dataset Missingness Classification and Handling](#8-dataset-missingness-classification-and-handling)  
9. [Cleaning Approach Taken in This Project](#9-cleaning-approach-taken-in-this-project)  
   - [Table showing Cleaning Steps, Purpose, and Limitations](#table-showing-cleaning-steps-purpose-and-limitations)  
   - [Importance of Data Types (dtypes)](#9b-importance-of-data-types-dtypes-in-this-project)  
10. [Schema and Audit Exports](#10-schema-and-audit-exports)  
11. [Core Functions and Components](#11-core-functions-and-components)  
12. [Exploratory Data Analysis (EDA)](#12-exploratory-data-analysis-eda)  
13. [Integrated Risk Scoring Framework](#13-integrated-risk-scoring-framework)  
14. [Modelling Results and Metrics](#14-modelling-results-and-metrics)  
15. [Key Findings](#15-key-findings)  
16. [Project Limitations](#16-project-limitations)  
17. [Proposed Future Enhancements](#17-proposed-future-enhancements)  
18. [Reproducibility and Consistency Strategy](#18-reproducibility-and-consistency-strategy)  
    - [Large Batch File Handling](#large-batch-file-handling)  
    - [GitHub File Size Considerations](#github-file-size-considerations)  
19. [Research and Attribution](#19-research-and-attribution)  
20. [Difficulties Experienced and Lessons Learned](#20-difficulties-experienced-and-lessons-learned)  
21. [Conclusion and Overall Takeaway](#21-conclusion-and-overall-takeaway)  
22. [Quick Start Summary](#22-quick-start-summary)  
23. [References](#23-references)  
24. [Ethical & Transparency Considerations](#24-ethical--transparency-considerations)  

---

### 1. Objective and Approach
This notebook forms part of the **Programming for Data Analytics Big Project 2025/2026**.

The objective is to demonstrate data acquisition, data cleaning, and analysis, to apply module techniques, and to present meaningful insights supported by clear visualisations.

### Approach
- Two complementary datasets were acquired and integrated: historic weather records and flight delay data.
- Both datasets were cleaned and normalised, then merged into a unified framework.
- Correlation analysis was conducted to explore relationships between weather conditions and flight delays.
- Machine learning models (Linear Regression, Random Forest, CatBoost) were used to benchmark predictive performance.
- Visualisations and summary tables were produced at each stage to ensure clarity and reproducibility.

### Goals
- Identify the weather variables that most strongly influence flight delays.
- Demonstrate how predictive models can extend correlation analysis, even when predictive accuracy is modest.
- Provide a transparent and reproducible workflow with clear documentation and outputs accessible to reviewers.

### Reviewer Takeaway
This project integrates weather and flight delay data into a transparent and reproducible workflow. It demonstrates data acquisition, cleaning, correlation analysis, and predictive modelling, aligning with module requirements and assessment criteria: 40% code, 40% documentation, 10% research, and 10% consistency.

---

## 2. Assessment Criteria Mapping
The following table presents the mapping of project outputs to the corresponding assessment criteria:

| Criterion | Implementation Summary |
|-----------|------------------------|
| **40% Code** | Modular workflow steps, robust cleaning (`clean_data` for weather, arrivals, departures), missing audits, hourly flooring, risk scoring, feature engineering, modelling (baseline + ensembles + tuning). |
| **40% Documentation** | Structured workflow mirrors notebook sections with succinct rationale, inline pros/cons, statistical interpretation, plots saved to `plots/`. |
| **10% Research** | Each major step cites specific sources with contextual use (data acquisition, cleaning, time series, modelling, tuning, interpretation). |
| **10% Consistency** | Hourly flooring for weather/flight alignment, schema parity across arrivals/departures, reproducible batching, pinned dependencies, CI/CD checks. |

### Reviewer Takeaway
The assessment criteria are explicitly mapped to workflow outputs, thereby ensuring transparency and alignment with the expectations of the module.

---

## 3. Workflow Overview

This section presents the complete workflow, from raw data acquisition through modelling and conclusions. Each stage is structured to ensure reproducibility, transparency, and alignment with module requirements.

| Step | Title | Key Actions | Reviewer Takeaway |
|:-----|:------|:------------|:------------------|
| 🔍 1 | Initial Visual Inspection | - Inspected raw flight JSON and weather CSV files<br>- Identified data type inconsistencies and null values<br>- Utilised **Data Wrangler** for schema preview | Early inspection enhanced transparency by revealing the raw data structure prior to transformation |
| 📉 2 | Dataset Missingness Classification | - Classified missingness (MCAR, MAR, MNAR)<br>- Synthesised published strategies<br>- Applied conservative handling (deletion or flagging) | Missingness was documented and addressed transparently, with trade-offs explicitly detailed |
| 🧹 3 | Cleaning Approach | - Corrected typographical errors and normalised data formats<br>- Coerced values to numeric types<br>- Removed duplicates and extraneous columns | Cleaning enhanced data quality and usability while preserving transparency and reproducibility |
| 📑 4 | Schema and Audit Exports | - Defined authoritative schemas<br>- Applied schemas following data cleaning<br>- Exported JSON schema files<br>- Documented audit processes | Schema enforcement ensured consistency, and exports served as transparent artefacts |
| 📦 5 | Flight Batching | - Partitioned JSON files into monthly batches<br>- Audited file sizes to support reproducibility | Batching maintained a lightweight and version-friendly repository |
| 🛬 6 | Arrivals Workflow | - Cleaned and reconstructed arrival delay fields<br>- Applied hourly flooring<br>- Concatenated data batches<br>- Enforced schema compliance | Arrivals data was cleaned, schema-aligned, and standardised for integration |
| 🛫 7 | Departures Workflow | - Replicated arrivals workflow<br>- Cleaned and reconstructed departure delay fields<br>- Ensured schema consistency | Departures workflow mirrored arrivals, facilitating direct comparison |
| 🔗 8 | Integration | - Integrated arrivals, departures, and weather data on an hourly basis<br>- Verified accuracy of hourly flooring<br>- Generated a unified data table | Integration resulted in a unified, schema-compliant dataset suitable for correlation and modelling |
| 📈 9 | Weather Impact Plots | - Generated scatterplots and regression lines<br>- Reported R² values | Visualisations illustrated weather impacts, offering context prior to correlation analysis |
| 🔥 10 | Correlation Analysis | - Created correlation heatmaps<br>- Compared arrivals and departures<br>- Identified visibility and humidity as primary predictors | Correlation analysis confirmed visibility and humidity as the strongest predictors of delays |
| 📊 10a–10i | Extended Data Analysis | - Generated boxplots to identify outliers<br>- Calculated daily aggregates<br>- Constructed rainfall timelines<br>- Produced humidity versus visibility scatterplots<br>- Computed rolling averages<br>- Analysed wind speed and direction<br>- Integrated weather risk factors<br>- Conducted weather code frequency analysis using WMO standards | Extended visualisations provided categorical context and deeper insights into environmental conditions |
| 🤖 11 | Modelling | - Established baseline using linear regression<br>- Applied Random Forest to assess feature importance<br>- Implemented CatBoost for incremental gains<br>- Performed hyperparameter tuning<br>- Summarised performance metrics (R², RMSE) | Random Forest outperformed baseline regression, while CatBoost provided modest improvements |
| 📝 12 | Conclusion | - Synthesised key findings<br>- Identified study limitations<br>- Outlined practical implications<br>- Proposed future enhancements | The conclusion delivered reproducible insights, acknowledged limitations, and recommended clear avenues for improvement |

---

## 4. Database Integration

To enhance reproducibility and transparency, the workflow stores cleaned and merged datasets in SQLite databases.
These databases function as durable audit artifacts and analysis engines, allowing reviewers to independently verify results, reproduce plots, and query the merged dataset without executing the entire notebook.

| Step | Title | Tables Created | Purpose | Reviewer Takeaway |
|:-----|:------|:---------------|:--------|:------------------|
| 📂 27 | Audit Databases | - `weather` → cleaned hourly weather records (visibility, humidity, wind, precipitation)<br>- `arrivals` → cleaned arrivals dataset with reconstructed delay fields<br>- `departures` → cleaned departures dataset with schema parity | - Provides independent audit artifacts for each dataset<br>- Enables reviewers to query cleaned data without rerunning the notebook<br>- Documents missingness (e.g., flights without weather matches, NaT checks) | Databases act as audit checkpoints, ensuring transparency and reproducibility of cleaned datasets |
| 🔗 29 | Merged Flights + Weather Database | - `flights_weather` → unified dataset combining arrivals, departures, and weather on hourly join key | - Operationalises merged dataset into a persistent table<br>- Enables SQL‑driven plots (delays by hour/day, distributions, delays vs rainfall)<br>- Demonstrates database as an **active analysis engine**<br>- Plots saved into `project/plots/` | Integration database supports reproducible analysis and plot generation directly from SQL queries |

### 📑 Reviewer Takeaway 
Databases are employed at two critical checkpoints: initially for audit purposes and subsequently for analysis. This approach ensures transparency, reproducibility, and auditability throughout the workflow.

---

### 4b. Database Example Queries & Plots
The following example SQL queries illustrate the process used to generate plots directly from the merged `flights_weather` database.

### Average Delay by Day of Week
This query calculates the average flight delay for each day of the week, where 0 represents Sunday and 6 represents Saturday:
```sql
SELECT strftime('%w', date_hour) AS day_of_week, AVG(computed_delay) AS avg_delay
FROM flights_weather
GROUP BY day_of_week
ORDER BY day_of_week;
```

The plot below was generated using the results of this query:
![Average Delay by Day of Week](plots/s29b_dbase_avg_delay_by_day.png)
  *The chart displays the average flight delay for each day of the week, with 0 corresponding to Sunday and 6 to Saturday.*

### Distribution of Flight Delays
This query retrieves all computed flight delays to facilitate histogram plotting:
```sql
SELECT computed_delay
FROM flights_weather
WHERE computed_delay IS NOT NULL;
```

The plot below was generated using the results of this query:
![Distribution of Flight Delays](plots/s29b_dbase_delay_distribution.png)
  *The chart illustrates the distribution of flight delays across various time intervals.*

### Average Delay by Rainfall Bin
This query categorises rainfall amounts into discrete bins and calculates the average flight delay for each bin:
```sql
SELECT CASE
    WHEN rain = 0 THEN '0 mm'
    WHEN rain > 0 AND rain <= 2 THEN '0-2 mm'
    WHEN rain > 2 AND rain <= 5 THEN '2-5 mm'
    ELSE '>5 mm'
END AS rain_bin,
AVG(computed_delay) AS avg_delay
FROM flights_weather
WHERE rain IS NOT NULL
GROUP BY rain_bin
ORDER BY rain_bin;
```

The plot below was generated using the results of this query:
![Average Delay by Rainfall Bin](plots/s29b_dbase_avg_delay_by_rain.png)
  *The chart displays the average flight delay corresponding to different ranges of rainfall.*

---

## 5. Data Sources & Roles in Workflow

| Source | Purpose | Role in Workflow |
|:-------|:--------|:-----------------|
| **🌦️ Met Éireann hourly (hly532.csv)** | Supplies environmental predictors such as temperature, rainfall, visibility, relative humidity, wind speed and direction, and cloud height. | Serves as the core weather dataset. Cleaned and audited in **Steps 3–4**, then used for exploratory plots (distributions, boxplots, rolling averages, wind roses) and integrated into the merged dataset for modelling. Visibility and humidity were identified as the strongest predictors of delays. |
| **✈️ Aviation Edge API (DUB)** | Supplies raw arrivals and departures data for Dublin Airport, including scheduled and actual times as well as delay context. | Queried in **Step 2** with dry‑run logging to ensure reproducibility. Batched into monthly JSON files (**Step 5**) for GitHub compatibility. Cleaned and reconstructed in the arrivals (**Step 6**) and departures workflows (**Step 7**), then merged with weather data for predictive modelling (**Step 8**). |
| **🌍 WMO Code Tables** | Standardises categorisation of weather events (present and past codes). | Applied during weather cleaning (**Step 3**) to classify conditions such as fog, mist, or precipitation. Facilitated categorical analysis and risk scoring, ensured consistency across weather records, and provided operational context for delay analysis. |
| **⚠️ Risk Scoring Framework (derived)** | Composite index constructed from thresholds (e.g., visibility < 2000 m, wind ≥ 25 knots, heavy rain ≥ 25 mm). | Developed in **Step 9** to quantify adverse conditions. Generated histograms and exceedance tables summarising combined weather hazards, which were subsequently used to contextualise modelling results. |
| **📑 Schema & Audit Exports (derived)** | Text exports of schema and missingness audits from raw JSON flight data. | Ensured reproducibility and transparency in **Step 4**. Enabled reviewers to verify data integrity and understand the structure of large raw files prior to batching. |

### 📑 Reviewer Takeaway
This project integrates multiple complementary data sources:
- **Met Éireann** supplied the environmental context.
- **Aviation Edge API** supplied operational flight delay data.
- **WMO Code Tables** standardised weather event categorisation.
- Derived **risk scores and schema audits** strengthened transparency and reproducibility.  

- Collectively, these sources enabled the creation of a merged dataset that supported exploratory analysis, correlation studies, and predictive modelling of flight delays.
- This approach demonstrates effective integration of multiple datasets, external APIs, and derived features, aligning with module expectations for data acquisition and research.

---

## 6. Environment and Dependencies

The project was developed and tested within a controlled Python 3.11 environment to ensure reproducibility and consistency.

### ⚙️ Core Environment
- **Python:** 3.11 (tested locally; selected to ensure full CatBoost wheel support)
- **Editor:** Visual Studio Code with Jupyter Notebook integration
- **Extensions:** Data Wrangler (used for initial data inspection and summarising data types and missing values)

### 📚 Key Libraries
| Library          | Version (pinned) | Role in Workflow |
|:-----------------|:-----------------|:-----------------|
| **🐼 pandas**       | 2.3.0            | Data cleaning, schema handling, missing value audits |
| **🔢 numpy**        | 1.26.4           | Numerical coercion, array operations, dtype management (pinned <2.0 for CatBoost compatibility) |
| **📊 matplotlib**   | 3.9.0            | Core plotting (histograms, wind roses, regression visuals) |
| **📈 seaborn**      | 0.13.2           | Statistical visualisations (heatmaps, scatterplots, regression lines) |
| **🤖 scikit-learn** | 1.5.0            | Baseline modelling, Random Forest, GridSearchCV, metrics (R², RMSE) |
| **🚀 catboost**     | 1.2.5            | Gradient boosting models, categorical feature handling |
| **📄 json (stdlib)**| built-in         | Parsing raw flight JSON files |
| **📄 csv (stdlib)** | built-in         | Reading historic weather CSV files |

### 🔄 Reproducibility Measures
- **requirements.txt** and **environment.yml** files specify all package versions to ensure consistent installations using pip or conda.
- **Schema exports** and **audit tables** documented data structure and missing values to enhance reviewer transparency.
- **Batching strategy** divided large files into manageable monthly segments to maintain compatibility with GitHub.

### 📑 Reviewer Takeaway 
This environment configuration ensured that all workflows were reproducible, cross-platform compatible, and accessible for reviewers. Explicit version pinning, and Python 3.11 compatibility reinforced transparency and consistency.

---

### 7. Initial Visual Inspection

Prior to automated cleaning or batching, the workflow commenced with a manual visual inspection of the raw datasets.
This step was critical for transparency, allowing reviewers to see the data in its original form and understand the challenges that shaped the technical approach.  
The inspection identified multiple inconsistencies and underlying complexities, which rendered the datasets difficult to process without systematic cleaning and schema enforcement.

#### Flight activity JSON files (arrivals & departures):  
  - Contained detailed operational records including scheduled times, actual times, statuses, and identifiers.  
  - Manual inspection uncovered **mixed content types and irregular formatting**:  
    - Delay minutes were sometimes stored as strings instead of integers, making calculations unreliable.  
    - Null values appeared in multiple inconsistent forms (`null`, `"null"`, or missing entirely), complicating automated parsing.  
    - Some records had incomplete or contradictory fields, requiring reconstruction of delay values.  
  - These issues prevented straightforward loading into Pandas and risked producing misleading results.
  - As a result, cleaning required explicit data type conversions (such as applying `astype(int)` to delay fields), the use of imputation flags to indicate reconstructed values, and schema enforcement to ensure consistency.

  ![Flight JSON Screenshot](plots/inspection_arrival_history_json.png)  
  *Figure 1: Raw arrivals JSON inspection showing inconsistent delay field formats.*

#### Historic weather CSV files:  
  - Provided meteorological variables such as wind speed, visibility, temperature, precipitation, and cloud height.  
  - Visual inspection identified systematic formatting problems:
    - Numeric values were stored as strings (e.g., `"12.5"` instead of `float`), preventing direct statistical analysis.  
    - Missing entries were concentrated in critical fields such as visibility, frequently during fog events, which are the conditions most relevant to delay prediction.
    - Some columns contained redundant indicators or placeholder codes that needed to be dropped.  
  - These irregularities rendered the dataset unsuitable for direct modelling and necessitated coercion (using `pd.to_numeric(errors="coerce")`), missingness audits, and risk scoring to quantify adverse conditions.

  ![Weather CSV Screenshot](plots/inspection_weather_dataset.png)  
  *Figure 2: Raw weather CSV inspection showing string‑encoded numeric values and missing visibility data.*

#### Data Wrangler visualisation: 
  - Data Wrangler was used to interactively explore both flight and weather datasets prior to any transformations.
  - The tool provided schema previews, column type checks, and sample row inspection within a reviewer-friendly interface.
  - Data Wrangler highlighted the extent of missing content and data type inconsistencies, making these gaps visible prior to cleaning.
  - For arrivals data, Data Wrangler clearly indicated where delay fields were mis-typed or missing, reinforcing the necessity of a structured cleaning pipeline.
  - This inspection confirmed that manual fixes alone were insufficient. A reproducible technical approach was required to normalise formats, enforce schemas, and document trade-offs.

![Data Wrangler Screenshot](plots/inspection_data_wrangler_summary.png)  
*Figure 3: Data Wrangler inspection highlighting missing and inconsistent fields in the arrivals dataset.*

### Resources
- [Data Wrangler GitHub Repository](https://github.com/microsoft/vscode-data-wrangler) – code‑centric data viewing and cleaning tool integrated into VS Code.  
- [Data Wrangler Extension for Visual Studio Code (Microsoft)](https://marketplace.visualstudio.com/items?itemName=ms-toolsai.datawrangler) – installation guide for VS Code.  
- [Python JSON Module Documentation](https://docs.python.org/3/library/json.html) – authoritative reference for parsing JSON files.  
- [Python CSV Module Documentation](https://docs.python.org/3/library/csv.html) – official guide for reading and writing CSV files.  
- [GeeksforGeeks – Working with JSON in Python](https://www.geeksforgeeks.org/python/working-with-json-data-in-python/) – practical examples for nested JSON structures.  
- [GeeksforGeeks – Reading CSV Files in Python](https://www.geeksforgeeks.org/pandas/reading-csv-files-in-python/) – step‑by‑step guide for handling CSVs.  

### 📑 Reviewer Takeaway 
This section emphasises the importance of initial transparency through visual inspection of both flight activity data (operational outcomes) and weather data (environmental context).

- This process reveals the raw structure of the datasets prior to any transformations, thereby building trust in the workflow.
- It establishes the dual foundation of the project, in which operational delays are interpreted through meteorological conditions.
- It shows how inspection findings directly shaped later technical steps, including:  
  - **Schema documentation and enforcement** (`arrivals_schema.txt`, `departures_schema.txt`)  
  - **dtype corrections** to ensure reliable modelling inputs  
  - **missingness audits** that guided imputation and conservative cleaning strategies  

Inspection revealed that both datasets contained non-standard formats, inconsistent null representations, and missing values in critical fields.
These irregularities made the data unsuitable for direct analysis and justified the need for a **systematic, reproducible cleaning and schema enforcement process**.  
Without this step, subsequent correlation and predictive modelling would have been unreliable or misleading.

By linking raw inspection to subsequent workflow decisions, this section ensures that all cleaning and modelling choices remain traceable, reproducible, and accessible to reviewers.

---

## 8. Dataset Missingness Classification and Handling

After the initial inspection, the subsequent stage involved diagnosing and classifying missing data across both datasets.
This step focused on understanding the mechanisms of missingness, rather than immediately addressing missing values, to ensure that subsequent cleaning decisions would be justified and reproducible.
Inspection revealed significant differences in missingness patterns between weather and flight data, with gaps frequently associated with operational or environmental contexts.

### Theoretical Background
Across the literature, missing data is classified into three main types:  
- **MCAR (Missing Completely at Random):** absence unrelated to any variable, often due to random technical errors.  
- **MAR (Missing at Random):** missingness depends on observed variables, such as survey responses skipped by certain groups.  
- **MNAR (Missing Not at Random):** missingness is tied to the unobserved value itself, e.g., exam scores missing because students did not attend.  

Published strategies indicate that deletion, naive imputation, and advanced methods each involve trade-offs. Transparent documentation of these trade-offs is essential for reproducibility.

### Weather Data
- **Observed issues:** Random gaps in visibility and precipitation readings, malformed datetime entries, and numeric values stored as strings.  
- **Classification:** Mostly **MCAR**, caused by technical recording errors or sensor dropouts.  
- **Implication:** These gaps may be considered noise; however, excluding them would result in a slight reduction in sample size.
- **Diagnostic insight:** Highlighted the need for safe numeric coercion and robust datetime parsing in later cleaning.

### Flight Arrivals
- **Observed issues:** Missing actual arrival times, especially for flights marked “unknown” or cancelled.  
- **Classification:** Primarily **MAR**, linked to flight status or airline reporting, with some **MNAR** where actual times were systematically absent.  
- **Implication:** Missingness was not random — it reflected operational realities.  
- **Diagnostic insight:** Any imputation would risk underestimating true delays, so conservative handling would be required.

### Flight Departures
- **Observed issues:** Similar to arrivals, with gaps in actual departure times and categorical inconsistencies in status fields.  
- **Classification:** Mostly **MAR**, with some **MNAR** tied to reporting gaps.  
- **Implication:** Missingness patterns mirrored those observed in arrivals, reinforcing the need for schema parity.
- **Diagnostic insight:** Flooring and categorical conversion would later be necessary to align departures with arrivals.

### Integrated Dataset (Flights + Weather)
- **Observed issues:** Alignment gaps when merging hourly flight records with weather observations.  
- **Classification:** A combination of **MCAR** (random weather gaps) and **MAR/MNAR** (systematic flight reporting issues).  
- **Implication:** Hourly flooring was necessary to ensure compatibility, although this approach reduced temporal precision.
- **Diagnostic insight:** Sub-hour disruptions would be masked; however, integration required a consistent time granularity.

### Resources
- [MCAR vs MAR vs MNAR: Understanding Types of Missing Data](https://www.linkedin.com/pulse/mcar-vs-mar-mnar-why-missing-isnt-all-same-datasets-fahim-ahamed-alxee)  
- [Types of Missing Data: MCAR, MAR, and MNAR Explained](https://learndata.xyz/posts/types%20of%20missing%20data%20mcar,%20mar,%20and%20mnar%20explained/)  
- [Understanding missing data mechanisms using causal DAGs](https://cameronpatrick.com/post/2023/06/untangling-mar-mcar-mnar/)

### 📑 Reviewer Takeaway
This step confirmed that **weather gaps were largely random (MCAR)**, while **flight data missingness was systematic (MAR/MNAR)**, reflecting operational reporting practices.  
By classifying missingness prior to cleaning and grounding these classifications in published literature, the workflow ensured that subsequent strategies such as coercion, imputation, flooring, and schema enforcement would be traceable, reproducible, and accessible for reviewers.
Without this diagnostic stage, cleaning could have introduced hidden bias or misrepresented operational realities.

---

## 9. Cleaning Approach Taken in This Project

After classifying and understanding missingness in Step 7, the subsequent stage addressed data cleaning.
The adopted strategy was intentionally conservative and transparent, prioritising reproducibility and clarity for reviewers over the use of complex imputation methods.
Data cleaning was performed prior to schema enforcement to ensure that datasets remained consistent, auditable, and compatible with weather data aggregated at hourly intervals.

```text
Raw Data
   │
   ▼
[Data Cleaning]
   - Handle missing values
   - Correct typos / normalise formats
   - Remove duplicates
   - Drop irrelevant or noisy columns
   │
   ▼
Cleaned Data
```

**Connection to Missingness Classification**
- Weather data (MCAR): Random gaps were considered noise. Records containing malformed datetimes or string-encoded numerics were either safely coerced or excluded.
- Flight data (MAR/MNAR): Systematic gaps in actual times necessitated cautious imputation using scheduled values, with flags implemented to indicate reconstructed delays.
- Integrated dataset: Hourly flooring was applied to align flight data with weather data. This compromise reduced temporal precision but ensured dataset compatibility.

---

### Table showing Cleaning Steps, Purpose, and Limitations

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

### 📑 Reviewer Takeaway
This project emphasised clear parsing, safe data conversions, and transparent auditing. Imputation maintained dataset continuity but resulted in an underestimation of true delays. Although hourly flooring reduced temporal granularity, it was essential for integration with weather data. These measures, taken together, demonstrate reproducibility and transparency, directly supporting the 40% code and 40% documentation criteria.

---

## 9b. Importance of Data Types (dtypes) in this project

In addition to data cleaning procedures, proper handling of data types was fundamental to maintaining consistency and usability of datasets for subsequent modelling tasks.

### Why Data Types Matter
Data types (dtypes) determine how values are stored and processed within Python libraries such as **NumPy** and **Pandas**. Proper dtype management is essential for the following reasons:
- **Performance:** Efficient memory usage and faster computations.  
- **Accuracy:** Ensuring calculations behave as expected (e.g., numbers treated as numbers, not strings).  
- **Compatibility:** Allowing datasets to merge correctly without type conflicts.  
- **Data Integrity:** Preventing unintended conversions that distort results.  

Inspection identified several significant issues related to data types:
- Flight JSON files contained mixed types (strings, integers, nulls).  
- Weather CSV files had numeric values stored as strings.  
- Inadequate dtype management resulted in suboptimal model training outcomes, such as negative R² values in CatBoost.

A key lesson was that dtype inspection needed to be incorporated into the initial stages of the cleaning pipeline, utilising tools such as Data Wrangler for schema previews.

### Common Data Types and Their Applications

| Data Type | Description | Typical Use Cases | Project Application |
|-----------|-------------|-------------------|---------------------|
| **int64 / int32** | Whole numbers (signed integers). | Counts, IDs, categorical codes. | Flight delay minutes, airline codes, flight IDs. |
| **float64 / float32** | Decimal numbers with precision. | Continuous variables, measurements. | Weather variables (temperature, rainfall, wind speed, visibility). |
| **object (string)** | Text values. | Labels, categorical names, metadata. | Flight status (“scheduled”, “cancelled”), airline names, WMO weather codes. |
| **datetime64[ns]** | Date and time values. | Time series, scheduling, and temporal alignment. | Scheduled vs actual flight times, hourly flooring for integration with weather data. |
| **bool** | True/False values. | Flags, binary indicators. | Risk scoring flags (e.g., visibility < 2000m). |
| **category** | Optimised storage for repeated string values. | Large categorical datasets. | Airline names, flight types, weather event codes. |

### Resources
- **Pandas Documentation – Missing Data & dtypes**  
  [Pandas User Guide: Missing Data](https://pandas.pydata.org/docs/user_guide/missing_data.html) – explains sentinel values (NaN, None) and dtype handling for consistency.  
- **NumPy Documentation**  
  [NumPy Reference Guide](https://numpy.org/doc/stable/reference/) – details array dtypes, vectorised operations, and performance considerations.  
- **Dataquest – NumPy and Pandas for Data Analysis**  
  [NumPy and Pandas for Data Analysis (Dataquest)](https://www.dataquest.io/blog/working-with-dataframes-in-pyspark/) – highlights that understanding the raw data structure is a crucial initial step in any data project.


### 📑 Reviewer Takeaway
Effective management of data types was vital for ensuring reproducibility and accuracy. Integrating dtype inspection into the cleaning pipeline prevented silent errors, facilitated reliable data merges, and improved modelling results.

The integration of inspection, missingness classification, dtype enforcement, and cleaning procedures ensured that the workflow remained traceable, reproducible, and accessible for review.

---

## 10. Schema and Audit Exports

### What is a Schema?
A **schema** is a formal blueprint that defines data structure, specifying field names, data types, and relationships between elements.
In analytics, schemas ensure consistency, accuracy, and reproducibility by explicitly defining how datasets are to be interpreted and integrated.

### Purpose in This Project
- **Schema Documentation (record‑only artefacts):**  
  Raw JSON structures for arrivals and departures were flattened and saved to text files (`arrivals_schema.txt`, `departures_schema.txt`).  
  These artefacts offer a transparent snapshot of the raw keys, although they are not directly utilised within the workflow.

- **Schema Enforcement (authoritative definitions):**  
  Authoritative schemas (`weather_cols`, `arrivals_cols`, `departures_cols`) were defined and applied immediately after the cleaned data was loaded or concatenated.  
  This process ensured retention of only validated fields for subsequent integration.

- **Audit Integration:**  
  Coverage audits, such as identifying flights missing weather matches and performing NaT checks, were conducted concurrently with schema enforcement to document any rows excluded due to alignment issues.

- **Cleaned Dataset Views:**  
  Reproducible DataFrames (`df_weather_clean`, `df_arrivals_clean`, `df_departures_clean`) were generated to serve as the authoritative source for integration.

- **Reviewer Transparency:**  
  Artefacts document the resolution of missing data, data type handling, and coverage mismatches, thereby ensuring clarity for assessment.


### 🔄 Schema Enforcement in Workflow

| Dataset | Schema | Application | Purpose |
|:--------|:-------|:------------|:--------|
| **🌦️ Weather Data** | `weather_cols` | Applied immediately after loading the cleaned CSV (`dublin_airport_clean.csv`) | Ensures only validated weather variables (rain, temp, humidity, visibility, etc.) are retained |
| **🛬 Arrivals Data** | `arrivals_cols` | Applied directly after concatenating all cleaned arrival batches | Captures datetime parsing, imputes missing actual times, reconstructs delays, and freezes into `df_arrivals_clean` for integration |
| **🛫 Departures Data** | `departures_cols` | Applied after concatenating all cleaned departure batches | Mirrors the arrivals schema to ensure parity, applies consistent handling of categorical fields, and finalises `df_departures_clean` using `reindex` for robust enforcement |
| **🔗 Integrated Dataset** | Unified schema | Combines arrivals (113,520) + departures (121,389) with weather data (total 234,909 records) | Aligns flights with weather conditions and risk features; supports correlation analysis and modelling of weather impacts on delays |

### Example Artefacts
- `arrivals_schema.txt` and `departures_schema.txt` — record‑only schema documentation of raw JSON keys.  
- Code cells defining `weather_cols`, `arrivals_cols`, and `departures_cols` — authoritative schema references applied after cleaning.  
- Audit outputs (e.g., “Arrivals missing weather match: 14,448”) provide a transparent record of exclusions during schema enforcement.
- `dublin_airport_clean.csv` – cleaned, integrated dataset combining arrivals, departures, weather variables, and derived risk scores.

### Resources
- [Pandas Documentation – `json_normalize`](https://pandas.pydata.org/docs/reference/api/pandas.json_normalize.html)  
  *Confirms the method used to flatten nested JSON structures into tabular form for inspection.*  
- [GitHub Documentation – Managing Large Files](https://docs.github.com/en/repositories/working-with-files/managing-large-files)  
  *Details GitHub’s 100 MB file size limit, which necessitates monthly batching of arrivals and departures.*
- [Python JSON Module Documentation](https://docs.python.org/3/library/json.html)  
  *Outlines reliable methods for loading and saving JSON data, thereby ensuring reproducibility in batching.*

### 📑 Reviewer Takeaway
Schemas fulfill two primary roles within this workflow:
- **Documentation:** Text files record the raw JSON structure for transparency.  
- **Enforcement:** Applied in‑code after cleaning to guarantee reproducible, validated datasets.  

Audits enhance transparency regarding rows excluded due to coverage mismatches, while schema enforcement ensures consistency across arrivals, departures, and weather datasets.
Reviewers may verify structure, data type handling, and missingness classification directly from the schema code cells and audit outputs, eliminating the need for access to full raw datasets.

---

## 11. Core Functions and Components

The notebook introduces several core functions and reusable components that organise the workflow.
Each component serves a distinct role in maintaining data quality, reproducibility, and outputs suitable for review.

### 🧹 Cleaning Functions

| Function | Role | Key Actions |
|:---------|:-----|:------------|
| **`clean_data` (weather & arrivals)** | Provides a consistent cleaning pipeline for weather and arrivals datasets | - Parses datetime fields and applies seasonal filters<br>- Converts numeric values safely<br>- Removes noisy indicator columns<br>- Handles missing data and enforces schema consistency |
| **`clean_departures`** | Tailored cleaning for departure data, mirroring arrivals workflow | - Reconstructs delay fields<br>- Applies hourly flooring<br>- Converts categorical variables<br>- Ensures departures integrate smoothly with arrivals and weather |

### 📊 Visualisation Components

| Function | Role | Key Actions |
|:---------|:-----|:------------|
| **`plot_monthly_wind_roses`** | Provides clear visualisations of directional wind patterns | - Generates polar plots of wind regimes for each month<br>- Highlights operational thresholds (≥20/25 knots)<br>- Links weather conditions to runway usage and planning |

### 🤖 Modelling Components

| Function | Role | Key Actions |
|:---------|:-----|:------------|
| **`tune_catboost`** | Implements safe manual loop for CatBoost hyperparameter tuning | - Avoids integration issues with `GridSearchCV`<br>- Selects best models based on R² scores<br>- Safeguards against invalid runs<br>- Documents parameter choices and runtime trade‑offs |

### ⚠️ Risk Scoring Block

| Component | Role | Key Actions |
|:----------|:-----|:------------|
| **Composite index (Step 10h)** | Quantifies adverse weather conditions in a reproducible format | - Built from thresholds (visibility < 2000 m, wind ≥ 25 knots, heavy rain ≥ 25 mm)<br>- Produces histograms and exceedance tables<br>- Provides operational insight into combined hazards<br>- Strengthens transparency by documenting risk scoring |

### 📑 Reviewer Takeaway  
These functions and components constitute the technical foundation of the project.
They ensure that data cleaning, visualisation, modelling, and risk scoring processes remain modular, reproducible, and transparent.
Centralising definitions within `project/project.ipynb` facilitates auditing, extension, and adaptation of the workflow for future enhancements.

---

## 12. Exploratory Data Analysis (EDA)

Exploratory Data Analysis was conducted following data cleaning and schema enforcement to examine the distribution, variability, and relationships within the weather dataset.
Most plots were generated prior to merging with flight delay data to facilitate analysis of the weather dataset in isolation.
Additional plots involving delay outcomes were produced after the datasets were merged, as these analyses required the integrated data.

Visualisations functioned as both diagnostic tools and narrative aids, promoting transparency for reviewers and informing subsequent modelling decisions.
All plots were saved in the `project/plots/` directory using systematic naming conventions (`sXX_<descriptor>.png`) to support reproducibility and facilitate reference.

---
### 🌤️ Weather Analysis (Pre‑Merge)

#### Distribution of Key Weather Variables 
  ![Distribution of Key Weather Variables Plot](plots/s6b_distributions_combined.png)  
Purpose: Illustrates the spread and skewness of weather variables, confirming their suitability for statistical comparison.

#### Temperature Distribution 
  ![Temperature Distribution Plot](plots/s6b_temp.png)  
Purpose: Depicts variability and outliers, establishing baseline context for subsequent regression models.

#### Rainfall Totals (Histogram) 
  ![Rainfall Totals Plot](plots/s6b_rain.png)  
Purpose: Highlights the frequency of heavy rainfall events, which is relevant for threshold-based risk scoring.

#### Wind Speed Distribution  
  ![Wind Speed Distribution Plot](plots/s6b_wdsp.png)  
Purpose: Provides operational context for runway usage and the identification of hazard thresholds.

### 🔗 Weather Relationships (Pre‑Merge)

#### Humidity vs Visibility (Scatter) 
  ![Humidity vs Visibility Plot](plots/s10d_humidity_vs_visibility.png)  
Purpose: Demonstrates the inverse relationship, confirming humidity as a primary predictor of delays.

#### Temperature vs Humidity (Scatter)  
  ![Temperature vs Humidity Plot](plots/s10f_temp_vs_rhum.png)  
Purpose: Illustrates seasonal clustering and the interdependence among weather variables.

### 🌦️ Operational Context (Pre‑Merge)

#### Wind Rose (Observed Conditions) 
  ![Wind Rose Plot](plots/s10g_windrose_2025-05-01.png)  
Purpose: Visualises prevailing wind directions and speeds, which are critical for runway operations during May 2025.

#### WMO Weather Codes Frequency  
  ![Weather Codes Plot](plots/s10i_weather_codes_counts_table.png)  
Purpose: Displays the distribution of coded weather events (fog, rain, storms), providing context for delay risk assessment.

#### Risk Score Distribution (Threshold Exceedances) 
  ![Risk Score Distribution Plot](plots/s10h_risk_score_distribution.png)  
Purpose: Quantifies exceedances of operational thresholds, including visibility below 2000 meters, wind speeds of at least 25 knots, and rainfall of at least 25 millimeters.

---

### ✈️ Delay Analysis (Post‑Merge)

#### Correlation Matrix (Arrivals + Weather)  
  ![Correlation Matrix Plot](plots/s31f_correlation_matrix_arrivals_weather.png)  
Purpose: Identifies visibility and humidity as the strongest drivers of arrival delays.

#### Correlation Heatmap (Departures + Weather) 
  ![Correlation Heatmap Plot](plots/s31g_correlation_matrix_departures_weather.png)  
Purpose: Confirms similar patterns for departures, reinforcing the importance of visibility and humidity as key variables.

#### Daily Arrivals vs Departures
  ![Daily Arrivals vs Departures Plot](plots/s26c_top_airlines_flight_volume.png)  
Purpose: Provides baseline context for operational flight volumes.

#### Average Hourly Delays  
  ![Average Hourly Delays Plot](plots/s26b_average_hourly_delay.png)  
Purpose: Highlights peak periods of delay throughout the day.

#### Airline Comparison (Delay Rates)  
  ![Airline Comparison Plot](plots/s26d_top_airlines_average_delay.png)  
Purpose: Illustrates variability in delays across carriers, providing context for the impact of weather.

#### Weather Impact on Delays (Boxplots)  
  ![Weather Impact Plot](plots/s10a_boxplots.png)  
Purpose: Compares delay distributions across different weather categories, including clear, fog, and rain conditions.

#### Feature Importance (Random Forest)  
  ![Feature Importance Plot](plots/s37_feature_importance_arrivals_departures.png)  
Purpose: Ranks weather features by predictive influence, confirming visibility and humidity as the dominant factors.

---

### 📑 Reviewer Takeaway  
Exploratory Data Analysis confirmed that visibility and humidity are the strongest correlates of delays, whereas rainfall and temperature exhibited weaker associations.
Pre-merge plots provided diagnostic insights into weather distributions, relationships, and operational context.
Post-merge plots demonstrated the interaction between weather and flight delays, highlighting hourly peaks, airline variability, and correlation matrices.

Collectively, these plots established a transparent and reproducible foundation for subsequent correlation and risk scoring analyses.

---

## 13. Integrated Risk Scoring Framework

Flags were assigned to key adverse conditions, including wind (≥20, ≥25 knots), extreme temperature (≤0 °C or ≥30 °C), visibility (≤5000 m, ≤2000 m), heavy rain (≥25 mm), and low cloud (≤500 m).
The aggregate risk score was determined by summing the binary flags. Outputs comprised histograms and exceedance percentage tables, which were retained to ensure reproducibility.

### 📑 Reviewer Takeaway
This framework quantified adverse weather conditions using schema-aligned thresholds, offering operational insight into the interaction of multiple hazards. Retained outputs ensured reproducibility and transparency in risk assessment.

---

## 14. Modelling Results and Metrics

### What Are Large Language Models (LLMs)?
Large Language Models (LLMs) are advanced machine learning systems trained on extensive text corpora. These models identify patterns, relationships, and structures in language, enabling the generation, interpretation, and analysis of complex information. Although LLMs were not directly employed in this project's predictive modelling, they provide a conceptual foundation. Modern AI systems, including structured models such as Linear Regression, Random Forest, and CatBoost, are designed to capture nonlinear relationships and hidden dependencies in data.

- [IBM: What are Large Language Models (LLMs)?](https://www.ibm.com/think/topics/large-language-models) – Defines LLMs as deep learning models trained on immense datasets, capable of understanding and generating natural language
- [Google Developers: Introduction to Large Language Models](https://developers.google.com/machine-learning/resources/intro-llms) – Explains transformers, self-attention, and applications such as summarisation, translation, and question answering
- [Dun & Bradstreet (DNB): Exploring Large Language Model Capabilities](https://www.dnb.com/en-us/resources/ai/what-are-large-language-models-or-llms.html) – Highlights how LLMs recognise patterns in unstructured data and provide contextually relevant responses across industries

### Background to the Models

#### Linear Regression:
- A classical statistical model that assumes a linear relationship between predictors and outcomes.
- Serves as a baseline benchmark to measure how much variance can be explained by simple linear trends.
- In aviation delay prediction, it highlights whether weather variables alone can linearly explain delays.

#### Random Forest:
- An ensemble learning method that builds multiple decision trees and averages their predictions.
- Known for robustness, ability to capture nonlinear interactions, and interpretability via feature importance.
- Particularly useful in flight/weather contexts where variables like temperature, humidity, and visibility interact in complex ways.

#### CatBoost:
- A gradient boosting algorithm optimised for handling categorical features and reducing overfitting.
- Excels in tabular datasets with mixed feature types, though in this project, the dataset was mostly numerical.
- Its inclusion ensured benchmarking against a state-of-the-art boosting approach widely used in predictive analytics.

#### Relevance of These Models for Flight and Weather Analysis
Flight delays are influenced by multiple interacting factors: weather conditions, operational constraints, and airport congestion.
- Linear Regression provides transparency and a baseline.
- Random Forest captures nonlinear weather effects (e.g., humidity interacting with visibility).
- CatBoost tests whether boosting methods can extract subtle signals from limited features.
- Studies confirm that ensemble methods such as Random Forest and CatBoost are widely applied in aviation delay prediction, as they effectively handle heterogeneous and imbalanced data while improving reliability. https://ceur-ws.org/Vol-4055/icaiw_waai_10.pdf

#### Model Contributions to the Project
- **Linear Regression:** Showed negligible explanatory power (R² ≈ 0.002), confirming delays are not linearly driven by weather alone.
- **Random Forest:** Consistently outperformed other models, with temperature and humidity emerging as dominant predictors. Tuned versions improved departure predictions (RMSE reduced to ~25 min).
- **CatBoost:** Delivered weaker results than Random Forest, reflecting the dataset’s limited categorical features. Still valuable as a benchmark for boosting approaches.

#### Consideration of Neural Network Approaches
Neural Networks were considered but ultimately not implemented due to:
- Neural networks (e.g., TensorFlow or Keras models) may be advantageous for large, diverse datasets with complex nonlinear relationships. However, for structured tabular weather data with relatively few features, Random Forest typically outperforms neural networks due to greater robustness, ease of tuning, and interpretability.
- [Random Forest significantly outperforms neural net for my regression task - Reddit](https://www.reddit.com/r/learnmachinelearning/comments/umvcne/random_forest_significantly_outperforms_neural/)

#### Results Summary
Models were benchmarked using R² and RMSE for both arrivals and departures.

| Model | Arrivals R² | Arrivals RMSE | Departures R² | Departures RMSE | Notes |
|-------|-------------|---------------|---------------|-----------------|-------|
| Linear Regression | ~0.0018 | ~31.6 min | ~0.0021 | ~30.2 min | Baseline, negligible variance explained. |
| Random Forest (default) | ~0.106 | ~29.9 min | ~0.066 | ~29.2 min | Nonlinear gains, strongest performer under weather‑only features. |
| CatBoost (default) | ~0.072 | ~30.5 min | ~0.055 | ~29.4 min | Limited signal, weaker than RF. |
| Random Forest (tuned) | ~0.114 | ~30.1 min | ~0.062 | ~25.0 min | Marginal improvement for departures. |
| CatBoost (tuned) | ~0.076 | ~30.7 min | ~0.003 | ~25.8 min | Still weaker than RF due to limited feature set. |

**Feature Importance (Random Forest):**  
- Arrivals: Temperature ≈46%, Humidity ≈28%, Visibility ≈21%, Rainfall ≈4%.  
- Departures: Temperature ≈44%, Humidity ≈32%, Visibility ≈17%, Rainfall ≈7%.  

### Reviewer Takeaway
Random Forest demonstrated the highest effectiveness, confirming that nonlinear ensemble methods are better suited for weather-driven delay prediction. Temperature and humidity emerged as the most influential variables, consistent with the exploratory analysis.

Sources:

- [Momtaz et al., Scalable Arrival Flight Delay Prediction: Multi-airport Benchmarking of Random Forest, XGBoost and CatBoost](https://ceur-ws.org/Vol-4055/icaiw_waai_10.pdf)
- [Hatıpoğlu & Tosun, Predictive Modelling of Flight Delays at an Airport Using Machine Learning Methods](https://www.mdpi.com/2076-3417/14/13/5472)
- [DataScienceBase, CatBoost vs Other Algorithms](https://datasciencebase.com/catboost-vs-other-algorithms/)

---

## 15. Key Findings

The analysis yielded several key insights regarding the relationship between weather conditions and flight delays.
These findings illustrate both the strengths and limitations inherent in a weather-only modelling approach.

| Finding | Detail | Implication |
|:--------|:-------|:------------|
| **Modest explanatory power** | Weather‑only predictors reached an ≈11% R² ceiling for arrivals | Confirms that weather explains only a small portion of delay variance |
| **Dominant variables** | Temperature and humidity emerged as strongest predictors; visibility and rainfall contributed minor variance | Suggests that operational features (airline, runway usage, staffing) are needed to improve accuracy |
| **Departures less sensitive** | Departures showed weaker correlations with weather compared to arrivals | Indicates missing operational context (e.g., gate logistics, turnaround times) |
| **Hourly aggregation limits granularity** | Aggregating data to hourly bins reduced ability to capture short‑term disruptions | Highlights trade‑off between reproducibility and temporal precision |

### 📑 Reviewer Takeaway  
The findings confirm that weather-only predictors account for a limited proportion of variance in flight delays.
- Arrivals demonstrate moderate sensitivity to temperature and humidity.
- Departures exhibit weaker dependence on weather, indicating the absence of key operational features.
- Hourly aggregation enhanced reproducibility but reduced the ability to detect short-term variations.

Overall, the results emphasise the necessity of integrating operational data, such as airline schedules, runway assignments, and staffing levels, with weather variables to improve predictive performance.
These findings provide a foundation for the Conclusion section, which will propose future enhancements and the integration of operational data.

---

## 16. Project Limitations

- **Data limitations:**  
  - Flight delay records lacked integration with **airline schedules, traffic density, ATC interventions, and maintenance states** — all major operational drivers of delays.  
  - Weather data was limited to **surface observations and forecasts**; no vertical profiles (e.g., upper‑air winds, turbulence) were available.  
  - Missing contextual features (e.g., runway usage, seasonal traffic surges, airline staffing) constrained explanatory power.

- **Methodological limitations:**  
  - **Hourly aggregation (“flooring”)** obscured sub‑hour disruptions and micro‑bursts of weather variability.  
  - Thresholds for risk scoring were **simplified and generic**, not tailored to airport‑specific SOPs or ICAO/EASA standards.  
  - Correlation analysis was restricted to **linear associations**, potentially missing nonlinear or lagged effects (e.g., cumulative rainfall impact).  
  - Forecast integration was exploratory only — **no back‑testing** against actual delay outcomes was performed.

- **Modelling limitations:**  
  - Models were trained on **weather‑only predictors**, yielding modest explanatory power (R² ceiling ≈0.11 for arrivals).  
  - **CatBoost underperformed** relative to Random Forest due to limited feature set and lack of categorical operational variables.  
  - Feature importance results were **dominated by visibility and humidity**, but this reflects correlation strength rather than causal certainty.  
  - Predictive outputs were **sensitive to aggregation choices** and lacked robustness across different temporal resolutions.

### 📑 Reviewer Takeaway
The limitations indicate that, although weather accounts for some delay variance, operational and contextual features are essential for more robust modelling. Documenting these constraints demonstrates transparency and critical reflection, supports the 40% documentation criterion, and informs future workflow extensions.

---

## 17. Future Role of LLMs and Proposed Enhancements  

### 🔮 Extending Beyond Structured Models  
Although the current project focused on structured models such as Linear Regression, Random Forest, and CatBoost applied to tabular weather data, Large Language Models (LLMs) present significant opportunities for future development. LLMs can incorporate unstructured data sources, including textual weather reports (METARs, TAFs), pilot logs, and air traffic control communications. These models are adept at extracting meaning from natural language, enabling the transformation of qualitative weather descriptions, such as “low visibility due to fog,” into structured features that complement numerical data. Integrating these textual insights with traditional weather variables has the potential to enrich predictive models, reveal hidden dependencies, and enhance accuracy in operational contexts. This approach would enable future systems to transcend purely numerical weather metrics by capturing the nuances present in human and textual reporting, in conjunction with ensemble methods.

### 🚀 Proposed Future Enhancements  
The following enhancements are intended to address the limitations identified in the Key Findings and Conclusion sections. These improvements extend the workflow beyond weather-only predictors, thereby increasing predictive accuracy, operational relevance, and usability for reviewers.

| Enhancement | Addresses Limitation | Impact |
|:------------|:---------------------|:-------|
| **✈️ Add operational features (airline, turnaround time, seasonal demand)** | Missing operational drivers | Increases predictive signal beyond weather, capturing airline‑specific and demand‑related delay factors |
| **📡 Integrate ATC / capacity metrics** | Absent congestion effects | Captures systemic delay drivers such as air traffic control restrictions and airport capacity bottlenecks |
| **⏱️ Sub‑hour timestamp precision** | Hourly flooring limitation | Recovers fine‑grained delay triggers, enabling analysis of short‑term disruptions and peak congestion periods |
| **🤖 Advanced ensemble stacking (RF + CatBoost)** | Modelling weakness | Improves robustness by combining strengths of multiple models, enhancing variance capture and predictive stability |
| **🗄️ Database layer (PostgreSQL / SQLite)** | Scaling & reproducibility | Provides queryable reproducibility, supports larger datasets, and enables integration with external systems |
| **📊 Dashboard (interactive forecast + risk ledger)** | Usability | Operationalises outputs into a stakeholder‑friendly interface, enabling real‑time forecasts and risk monitoring |
| **🤖 LLM integration (METARs, pilot logs, ATC comms)** | Lack of unstructured data | Adds qualitative insights, enriching predictors with textual weather and operational context |

### 📑 Reviewer Takeaway  
These enhancements directly tackle the limitations identified earlier:  

- **Operational features** and **ATC metrics** strengthen explanatory power by adding missing drivers.  
- **Sub‑hour precision** restores temporal granularity lost in hourly aggregation.  
- **Ensemble stacking** improves modelling resilience and accuracy.  
- **Database integration** and **dashboards** elevate reproducibility and usability.  
- **LLM integration** bridges structured and unstructured data, enabling richer, context-aware forecasting.  

Collectively, these enhancements establish a clear roadmap for advancing the project from a research prototype to a practical, operational forecasting tool that leverages both structured ensemble methods and advanced language models.

---

## 📊 Visual Roadmap  

```mermaid
flowchart TD
    A[Current Project: Weather-only Predictors] --> B[Structured Models: Linear Regression, Random Forest, CatBoost]
    B --> C[Feature Importance: Temp, Humidity, Visibility, Rainfall]
    C --> D[Proposed Enhancements]
    D --> D1[✈️ Operational Features]
    D --> D2[📡 ATC / Capacity Metrics]
    D --> D3[⏱️ Sub-hour Precision]
    D --> D4[🤖 Ensemble Stacking]
    D --> D5[🗄️ Database Layer]
    D --> D6[📊 Interactive Dashboard]
    D --> D7[🤖 LLM Integration: METARs, Pilot Logs, ATC Comms]
    D7 --> E[Future System: Hybrid Structured + LLM Forecasting]
    E --> F[Operational Tool: Real-time Forecasts & Risk Monitoring]
```

This diagram illustrates:  
- The **starting point** (weather-only predictors and structured models).  
- The **enhancement pathway** (operational features, ATC metrics, precision, stacking, database, dashboard).  
- The **integration of LLMs** to handle unstructured data.  
- The **end goal**: a hybrid forecasting system operationalised into a real-time tool.  

---

## 18. Reproducibility and Consistency Strategy

- Dry-run toggles are implemented to avoid mandatory API dependencies.
- Monthly batching is used to minimise issues associated with large files.
- Explicit header detection and schema exports are performed to ensure data integrity.
- Hourly bin audits are conducted to ensure deterministic data merges.
- Parameter grids are documented, ensuring that tuned models are reproducible.
- Plots are named systematically using the format `sXX_<descriptor>.png`.

### Large Batch File Handling
Raw JSON files obtained from the Aviation Edge API were substantial in size and surpassed GitHub's file size limitations.
To maintain compatibility, the workflow incorporated a batching mechanism that divided data into monthly segments. Schema exports and missingness audits were stored in place of oversized raw files, enabling reviewers to verify data structure without requiring access to the complete raw dataset.

#### GitHub File Size Considerations
[GitHub guidance](https://docs.github.com/en/repositories/working-with-files/managing-large-files/about-large-files-on-github) highlights:  
- **Individual file limit:** ~100 MB (hard limit for pushes).  
- **Recommended repository size:** <1 GB for smooth cloning and usage.  
- **Large files:** Can cause slow downloads, version control friction, and may be rejected by GitHub.  

### Project Strategy
- **Monthly Batching:** Raw flight JSON files were split into monthly segments, keeping each file below the 100 MB threshold.  
- **Schema & Audit Exports:** Oversized raw files were replaced with schema text exports and missingness audits, ensuring transparency.  
- **Toggle Control:**  
  - `RUN_BATCHING = False` by default, preventing unnecessary re‑batching.  
  - Monthly files are already included for analysis; re‑running batching is not required in this repository.  
  - `RUN_BATCHING = True` only if using your own dataset locally.  

### 📑 Reviewer Takeaway 
This strategy ensured that the repository remained lightweight, reproducible, and accessible for reviewers.
- **Batching** maintained GitHub compatibility for large raw files while preserving transparency.
- **Schema and audit exports** offered verifiable structural and missingness records as substitutes for oversized data files.
- **Deterministic merges and systematic naming** ensured that outputs could be reproduced with precision.

Collectively, these measures demonstrated consistency and reproducibility, directly supporting the **10% consistency criterion** and providing reviewers with confidence that the workflow can be rerun and audited efficiently.

---

## 19. Research and Attribution

The following resources were consulted and directly integrated into the notebook workflow.
Each citation corresponds to a specific workflow step, thereby supporting transparency and reproducibility for reviewers.

| Resource | Applied In | Role in Workflow |
|----------|------------|------------------|
| [**Project Specification Document**](https://vlegalwaymayo.atu.ie/pluginfile.php/1804303/mod_resource/content/2/Project%20Description.pdf) | Entire workflow | Provided the foundational requirements and assessment criteria. Guided the overall structure, deliverables, and evaluation metrics for the project. |
| [**Pandas Missing Data Documentation**](https://pandas.pydata.org/docs/user_guide/missing_data.html) | Cleaning & schema enforcement (Steps 7–9) | Guided handling of missing values, schema consistency, and robust data import/export operations. Ensured reproducible cleaning pipelines for both weather and flight datasets. |
| [**NumPy Documentation**](https://numpy.org/doc/stable/) | Cleaning transformations (Step 8) | Supported numerical coercion, array handling, and efficient calculations across weather variables. |
| [**Python Standard Library (os, json)**](https://docs.python.org/3/library/) | Flight batching & API handling (Step 9) | `os` managed file paths and reproducibility for saving plots and batched JSON files; `json` parsed raw API responses into structured formats for cleaning and batching. |
| [**Seaborn Documentation**](https://seaborn.pydata.org/) | EDA & modelling visuals (Steps 13, 15) | Provided statistical visualisations for correlation matrices, scatterplots, and regression lines. Enhanced interpretability of relationships between weather variables and delays. |
| [**Matplotlib Documentation**](https://matplotlib.org/stable/contents.html) | EDA & risk scoring (Steps 13–14) | Backbone for most static plots saved to `project/plots/`. Enabled polar wind rose plots, histograms, and regression visualisations. |
| **WMO Code Tables** | Weather code mapping (Step 14) | Standardised classification of present and past weather events. Allowed categorical analysis of conditions such as fog, mist, and precipitation. |
| [**Scikit‑Learn Documentation**](https://scikit-learn.org/stable/documentation.html) | Modelling (Step 15) | Provided implementation details for regression models, ensemble methods, and systematic hyperparameter tuning. Ensured reproducibility and fairness in model benchmarking. |
| [**Scikit‑Learn Metrics Documentation**](https://scikit-learn.org/stable/modules/model_evaluation.html) | Model evaluation (Step 15) | Supplied formulas and functions for R² and RMSE, ensuring transparent evaluation of model performance. |
| [**CatBoost Quickstart Guide**](https://catboost.ai/en/docs/) | Modelling (Step 15) | Supported integration of CatBoost into the modelling pipeline. Guided parameter selection and explained default handling of categorical features. |
| **Time Series & Rolling Guides** | Weather aggregation & smoothing (Steps 8, 13) | Informed rolling averages and daily aggregation methods. Helped clarify medium‑term weather trends and seasonal cycles. |
| [**Aviation Edge API Documentation**](https://aviation-edge.com/developers/) | Raw flight acquisition (Step 9) | Provided schema and query details for retrieving arrivals and departures data. Supported reproducible API calls and dry‑run logging. |
| [**GitHub Large‑Files Guidance**](https://docs.github.com/en/repositories/working-with-files/managing-large-files/about-large-files-on-github) | Batching strategy justification (Step 19) | Informed the decision to split raw JSON flight data into monthly batches. Ensured repository compatibility and reproducibility for large datasets. |

### 📑 Reviewer Takeaway
Every major step in the workflow was grounded in authoritative resources.
Inline citation of documentation and explicit explanation of its application maintained transparency, reproducibility, and reviewer confidence.
Each resource directly shaped cleaning, schema enforcement, visualisation, modelling, or operationalisation stages of the notebook.  
This approach demonstrates effective use of external resources and directly supports the 10% research criterion.

---

## 20. Difficulties Experienced and Lessons Learned  

Several challenges were encountered during the project. The following list summarises these difficulties and the corresponding lessons learned from each experience.

| Difficulty | Lesson Learned | Impact |
|------------|----------------|--------|
| **Initial Analysis and Planning** | Careful scoping at the start is essential to avoid wasted effort and ensure alignment with assessment criteria. | Improved focus and efficiency in documentation. |
| **Saving Files vs Leaving in Memory** | Leaving more in memory reduced clutter and improved reproducibility, while only key outputs were saved. | Cleaner repository and easier reviewer navigation. |
| **File Size Issues (Repository Uploads)** | Large files must be batched or excluded from version control to avoid repository corruption and workflow disruption. | Prevented repository crashes and loss of commit history. |
| **Unmonitored JSON File Sizes** | Always audit file sizes before committing or uploading, especially when working with APIs that generate large nested structures. | Avoided repeated upload failures and repository resets. |
| **Data Type Compatibility** | Correct dtype handling is critical for reliable modelling. Poor treatment of dtypes can severely impact merging and training. | Ensured stable model training and accurate results. |
| **Model Training and Runtime** | CatBoost underperformed compared to Random Forest, reinforcing that weather alone is insufficient for strong predictive modelling. | Highlighted the need for richer feature sets beyond weather data. |
| **Python Version Compatibility (CatBoost)** | Reverting to Python 3.11.14 resolved runtime errors since CatBoost was not supported in Python 3.12. The README was updated to highlight this requirement. | Ensured reproducibility and clear reviewer guidance. |
| **Library Version Conflicts (Pandas)** | Careful dependency management is essential. Pinning compatible versions in the environment file ensured stability and reproducibility. | Prevented workflow breakages and maintained consistent results. |
| **Instructor Guidance (Batching)** | An online meeting introduced batching, which solved file size issues and improved reproducibility. | Enabled smoother handling of large datasets. |
| **Improved Visualisation (Data Wrangler)** | Discovered **Data Wrangler**, which improved schema previews, dtype inspection, and reviewer‑friendly transparency. | Enhanced clarity and usability of data exploration. |
| **Dataset Limitations** | Refined the project objective to focus on correlations between weather and delays, while suggesting further studies to incorporate operational and scheduling variables. | Delivered a realistic scope while identifying pathways for future research. |

### Key Takeaways
- Environment management is essential: Compatibility issues with Python (3.12 vs 3.11.14) and Pandas highlighted the importance of pinning versions and clearly documenting requirements.
- Reproducibility is critical: Decisions regarding file saving, batching, and dependency management ensured that reviewers could replicate results without workflow failures.
- Feature limitations shape outcomes: Reliance on weather-only predictors constrained model performance, reinforcing the need for operational and scheduling features in future work.
- Transparency improves usability: Tools such as Data Wrangler and clear README updates enhanced reviewer experience and project clarity.

Overall, the project demonstrated that technical stability, reproducibility, and scope management are as important as modelling choices in delivering a credible and reviewer-friendly analysis.

---

## 21. Conclusion and Overall Takeaway

The project established a transparent and reproducible workflow for integrating Dublin Airport flight delays with hourly weather data. Each stage yielded distinct insights:

- **Weather Cleaning & Exploration:**  
  Weather data underwent parsing, cleaning, and auditing, guided by schema enforcement and missingness classification. Visualisations revealed skewed rainfall distributions, seasonal temperature cycles, directional wind regimes, and strong inverse relationships between humidity and visibility. Risk scoring quantified adverse conditions, including low visibility, strong winds, and heavy rainfall.

- **Flight Data Acquisition & Batching:**  
  Arrivals and departures data were obtained via the Aviation Edge API and partitioned into monthly batches to ensure compatibility with GitHub. Batching served as a key reproducibility strategy, enabling reviewers to verify data structure without handling oversized files. Visualisations highlighted daily traffic variability, hourly delay peaks, and airline-level differences in delay performance.

- **Database Integration & Querying:**  
  Cleaned weather and flight datasets were imported into a relational database (PostgreSQL or SQLite). Schema enforcement maintained referential integrity between tables (weather, arrivals, departures). SQL queries were employed to:
  - Join weather and flight records on hourly timestamps.  
  - Aggregate delays by airline, day, and hour.  
  - Compute correlation matrices directly in‑database for reproducibility.  
  - Generate risk exceedance counts without relying solely on notebook logic.  
  The database layer enhanced transparency, reproducibility, and efficiency, allowing reviewers to replicate results using straightforward queries.

- **Integration & Flooring:**  
  Weather and flight datasets were aligned on an hourly basis using flooring. This approach ensured deterministic merges and schema consistency but reduced variance and weakened correlations by aggregating sub-hour delays into hourly bins. Short-lived weather events, such as fog patches and sudden rainfall, were dampened, limiting explanatory power.

- **Correlation Analysis:**  
  Heatmaps and scatterplots identified visibility and humidity as the strongest correlates of arrival delays, whereas temperature and rainfall had minor effects. Departures exhibited weaker associations, highlighting the influence of non-weather operational factors.

- **Modelling:**  
  Linear regression established a transparent baseline but explained minimal variance. Random Forest models captured non-linear effects, improving explanatory power (R² approximately 0.11 for arrivals and 0.06 for departures) and ranking temperature and humidity as primary drivers, with visibility and rainfall contributing less. CatBoost provided modest gains for arrivals but demonstrated near-zero explanatory power for departures. Hyperparameter tuning yielded incremental improvements; however, predictive performance remained limited without operational features.

- **Limitations and External Factors:**  
  The limited explanatory power (≤11% for arrivals, ≤6% for departures) reflects the absence of critical operational drivers, including airline schedules, traffic density, air traffic control constraints, and turnaround times. Incorporating these factors in future work is necessary to achieve greater predictive capacity.


#### 📑 **Overall Takeaway:**  
Weather‑only modelling sets a clear upper bound on predictive accuracy. Humidity and visibility emerge as the strongest correlates, while modelling feature importance highlights temperature and humidity as dominant drivers. Departures are less weather‑sensitive, and the flooring reduces temporal granularity, further constraining results. The addition of a **database analysis layer** ensured reproducibility, efficient querying, and transparent schema enforcement, strengthening the project’s credibility.  

Despite these limitations, the project established a transparent and reproducible foundation that fulfilled all assessment requirements, including structured acquisition, data cleaning, schema enforcement, database integration, exploratory analysis, correlation analysis, modelling, and benchmarking.
This conclusion demonstrates that the project satisfied the criteria of 40% code, 40% documentation, 10% research, and 10% consistency, while also outlining a roadmap for future enhancements.

---

## 22. Quick Start Summary

The following summary presents a step-by-step checklist for reproducing the project:

1. Install dependencies.  
2. Open the notebook.  
3. (Optional) Set API key and enable downloads.  
4. Run sequentially and verify audit outputs (e.g., minutes arrays = `[0]`).  
5. Review plots, metrics, and risk tables.  
6. Extend the feature set for improved predictive capacity.

---

## 23. References

A consolidated list of all external sources cited throughout the README and notebook:

- Pandas Documentation – [Missing Data](https://pandas.pydata.org/docs/user_guide/missing_data.html)  
- NumPy Documentation – [Reference Guide](https://numpy.org/doc/stable/reference/)  
- Dataquest – [NumPy and Pandas for Data Analysis](https://www.dataquest.io/blog/numpy-pandas-cheat-sheet/)  
- Analytics Vidhya – [Handling Missing Values](https://www.analyticsvidhya.com/blog/2021/10/handling-missing-value/)  
- Kaggle – [Guide to Handling Missing Values in Python](https://www.kaggle.com/code/parulpandey/a-guide-to-handling-missing-values-in-python)  
- Towards Data Science – [Handling Missing Data](https://towardsdatascience.com/handling-missing-data-f998715fb73f/)  
- Python Data Science Handbook – [Handling Missing Data](https://jakevdp.github.io/PythonDataScienceHandbook/03.04-missing-values.html)  
- GeeksforGeeks – [Working with JSON in Python](https://www.geeksforgeeks.org/python/working-with-json-data-in-python/)  
- GeeksforGeeks – [Reading CSV Files in Python](https://www.geeksforgeeks.org/pandas/reading-csv-files-in-python/)  
- Microsoft – [Data Wrangler Extension for VS Code](https://marketplace.visualstudio.com/items?itemName=ms-toolsai.datawrangler)  
- Scikit‑Learn Documentation – [User Guide](https://scikit-learn.org/stable/documentation.html)  
- Scikit‑Learn Metrics – [Model Evaluation](https://scikit-learn.org/stable/modules/model_evaluation.html)  
- CatBoost – [Quickstart Guide](https://catboost.ai/en/docs/)  
- Aviation Edge – [API Documentation](https://aviation-edge.com/developers/)  
- GitHub – [Large Files Guidance](https://docs.github.com/en/repositories/working-with-files/managing-large-files/about-large-files-on-github)  
- WMO – [Code Tables](https://community.wmo.int/en/activity-areas/wmo-codes)  


**Background Reading on Schema Design**
These resources were consulted for conceptual clarity on schema design and data documentation, but were not directly implemented in the notebook:
- DataCamp – [Database Schema Tutorial](https://www.datacamp.com/tutorial/database-schema)  
- Sifflet Data – [Data Schema Explained](https://www.siffletdata.com/blog/data-schema)  
- PlainSignal – [What is a Data Schema in Analytics?](https://plainsignal.com/glossary/schema)  

---

## 24. Ethical and Transparency Considerations

### Data Ethics
- **API Usage:** All Aviation Edge API queries were logged using a dry-run option to minimise unnecessary calls and ensure compliance with rate limits.
- **Privacy:** No personally identifiable information (PII) was collected or stored. Flight records were aggregated exclusively at the operational level.
- **Bias Awareness:** The use of weather-only predictors limited the explanatory scope. Results were interpreted conservatively to avoid overstating predictive accuracy.

### Transparency
- **Imputation Decisions:** All imputations (e.g., reconstructing actual times from scheduled times) were flagged in schema exports (`imputed_flag` columns).  
- **Schema Documentation and Enforcement:** Arrivals and departures schemas were exported to text files to enhance transparency, while authoritative schemas were enforced in code to ensure reproducibility.
- **Audit Trails:** Missingness audits and risk scoring thresholds were documented in markdown cells, making trade‑offs explicit.  
- **Reproducibility:** Dependencies were pinned in `requirements.txt` and verified using GitHub Actions. Large files were batched to maintain GitHub compatibility and facilitate reviewer transparency.

### Reviewer Takeaway
The project was designed to be transparent, ethical, and reproducible.
- Ethical safeguards ensured responsible API usage and mitigated privacy risks.
- Transparency measures, including schema exports, audit tables, and imputation flags, made data cleaning decisions explicit.
- Reproducibility strategies (pinned dependencies, CI/CD checks, batching) ensured the workflow can be reliably rerun by reviewers and future users.  

Collectively, these measures demonstrate alignment with the 10% consistency criterion and reinforce reviewer confidence in the integrity of the project.

---

## 25. Acknowledgements

This project was supported by a combination of technical resources, external references, and academic guidance:

- **Data Providers:**  
  Aviation Edge (flight arrivals and departures API) and Met Éireann (weather observations and forecasts).

- **Technical Tools:**  
  Python libraries (`pandas`, `numpy`, `matplotlib`, `seaborn`, `scikit-learn`, `catboost`) and database systems (PostgreSQL and SQLite) were utilised for analysis, modelling, and reproducibility.
  The Microsoft Data Wrangler extension for Visual Studio Code was employed to streamline data cleaning, schema validation, and exploratory checks.

- **Documentation & References:**  
  Online tutorials, official library documentation, and background literature on schema design and data cleaning were consulted (see Section 24).

- **AI   Microsoft Copilot was utilised throughout the project to refine documentation, structure sections, and ensure clarity in presenting results and limitations. This support contributed to enhanced transparency and alignment with assessment criteria.

- **Grammarly Editor Assistance**
Grammarly was used to proofread and enhance the readability of the documentation, ensuring clear communication of complex concepts.

- **Academic Guidance:**  
  Special thanks are extended to Mr. Andrew Beatty, Atlantic Technological University (ATU), for his guidance and support in shaping the project structure, ensuring academic rigor, and aligning the workflow with assessment requirements.

---

# END
