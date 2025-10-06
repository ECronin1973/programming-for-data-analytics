# Programming For Data Analytics — my-work

This README documents the student work inside the `my-work/` folder for the Programming For Data Analytics module. It summarises the assignments, code, data, and generated charts in this workspace and explains how to reproduce the results.

## Contents
- Overview
- Files and folders in `my-work`
- How to run (script and notebook)
- Data sources and assumptions
- Approach taken (brief)
- Dependencies
- Where outputs are saved
- References and sources

---

## Overview
This folder contains sample student work for a short assignment that demonstrates loading CSO CSV data, fitting a simple linear model to historical counts, projecting future values, and saving resulting charts. The content is intentionally lightweight and educational — it focuses on reproducibility and clarity rather than production-grade pipelines.

The main artifacts are:
- A Python script that locates the CSO CSV, fits a linear model, plots historical and projected births, and saves a timestamped PNG.
- A Jupyter notebook that walks through the same steps interactively for teaching.
- Input CSV files and generated charts used as outputs.

---

## Project structure (this folder)

- assignments/
  - `week01_projected_births_notebook.ipynb` — student notebook that loads the CSV, fits a linear model, projects 30 years forward, plots the results, and saves a timestamped PNG to `generated_charts/`.

- code/
  - `projected_births.py` — standalone script that implements the same steps as the notebook; robust file search for the CSV is included and outputs are saved to `my-work/generated_charts`.

- data/
  - `projectedbirths-cso.csv` — CSO-provided projected births dataset used by the notebook and script.
  - `cso-populationbyage.csv` — population data (supporting context dataset, not strictly required by the simple projection script).

- generated_charts/
    - `projected_births_2025-10-06_112723.png`

---

## How to run

Prerequisites:
- Python 3.8+ (recommended)
- The following Python packages: pandas, numpy, matplotlib, scikit-learn

You can install dependencies with:

```powershell
pip install pandas numpy matplotlib scikit-learn
```

Run the script (from its folder) with:

```powershell
python .\projected_births.py
```

This script will:
- Search for `projectedbirths-cso.csv` in nearby `data/` and `code/data/` folders.
- Fit a simple LinearRegression on Year (t = Year - yr0).
- Project 30 years into the future and plot historical points, fitted line, and projection segment.
- Save a timestamped PNG in `my-work/generated_charts/` and print the filename.

Run the notebook interactively:
- Open `assignments/week01_projected_births_notebook.ipynb` in Jupyter or VS Code.
- Run the cells in order (Imports, Find CSV, Load/Clean, Fit/Plot, Save/Show, Summary).

The notebook contains the same robust out_dir resolution used by the script and prints the resolved output folder when saving.

---

## Data sources and assumptions
- The CSV `projectedbirths-cso.csv` was sourced from the Central Statistics Office (CSO) projected births dataset.
- The script/notebook assume the CSV contains a `Year` column and a numeric column `VALUE` (or `BirthRate` or other numeric column). The code picks `VALUE` if present, otherwise falls back to other numeric columns.
- The projection is a simple linear regression on historical counts; it is illustrative and not a full demographic forecast.

---

## Approach taken
- Data discovery: both script and notebook use a small search utility to locate `projectedbirths-cso.csv` in nearby `data/` folders. The notebook includes a fallback that searches parent directories for a `my-work` folder to place outputs consistently.
- Preprocessing: `Year` and the selected numeric column are coerced to numeric and rows with missing values are dropped.
- Modeling: fit a scikit-learn LinearRegression on t = Year - yr0.
- Projection: generate predictions for a 30-year horizon and plot the fitted line across historical years and a different color/style for the projected segment.
- Output: timestamped PNG files saved to `my-work/generated_charts`.

---

## Dependencies
- pandas
- numpy
- matplotlib
- scikit-learn

(Install with `pip install pandas numpy matplotlib scikit-learn`)

---

## Where outputs are saved
All generated plots are saved to `my-work/generated_charts/`. Filenames include a timestamp to avoid accidental overwrite, for example:

`projected_births_2025-10-06_112436.png`

The notebook prints the resolved save directory when it runs so students can see exactly where files are written.

---

## Code sources and references
- scikit-learn LinearRegression (model fitting): https://scikit-learn.org/stable/modules/linear_model.html
- pandas data loading and cleaning: https://pandas.pydata.org/
- matplotlib plotting: https://matplotlib.org/
- CSO data portal (for dataset provenance): https://data.cso.ie/

The scripts and notebook include brief comments in-line referencing these libraries and the assumptions made.

---

## Notes and future improvements
- Replace simple linear model with richer demographic projection models if required.
- Add CLI flags to the script to control projection horizon, output folder, and filename format.
- Add unit tests for data-loading and model-fitting functions.

---

## Contact
If you need clarifications on the code or data, contact the author (Edward Cronin) at g00425645@atu.ie.
