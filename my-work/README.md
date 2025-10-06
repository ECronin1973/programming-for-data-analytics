# Programming For Data Analytics — my-work

This README documents the student work inside the `my-work/` folder for the Programming For Data Analytics module. It summarises assignments, code, data, and generated charts, and explains how to reproduce results.

## Contents
- Assignment 1: Projected births
- Assignment 2: Population by age (Galway)
- How to run
- Data sources and assumptions
- Dependencies
- Where outputs are saved
- Notes and future improvements

---

## Assignment 1 — Projected births

Files:
- `code/projected_births.py` — script that finds `projectedbirths-cso.csv`, fits a linear model to historical annual counts, projects 30 years forward, and saves a timestamped PNG to `my-work/generated_charts/`.
- `assignments/week01_projected_births_notebook.ipynb` — interactive notebook that walks through the same workflow and saves a timestamped PNG.

How it works (brief):
- Locates the CSV in nearby `data/` or `code/data/` folders.
- Cleans `Year` and the numeric value column (prefers `VALUE`).
- Fits scikit-learn LinearRegression on t = Year - yr0 and projects 30 years ahead.
- Plots historical points, fitted line, and projection segment; saves a timestamped PNG.

Run:
```powershell
cd my-work/code
python .\projected_births.py
```

---

### Example output
![Projected births example](generated_charts/{{LATEST_PROJECTED_BIRTHS}})

Caption: Historical births (points), fitted line (dotted) and linear projection (solid). Output filename is timestamped.


## Assignment 2 — Population by age (Galway)

Files:
- `code/cso_populationbyage_galway.py` — loads `cso-populationbyage.csv`, filters for CensusYear 2022 and the two Galway councils (Galway City Council and Galway County Council), aggregates population by single-year age, plots a coloured bar chart with annotations and a ledger, highlights the dip between ages 20–40, and saves timestamped PNG(s) to `my-work/generated_charts/`.
- `assignments/week01_populationbyage_galway_notebook.ipynb` — interactive notebook that performs the same analysis and saves two PNGs (main plot and highlighted dip).

How it works (brief):
- Finds the CSV using the same local search heuristic.
- Filters to 2022, Both sexes, and the Galway councils; parses 'Single Year of Age' labels.
- Aggregates city + county counts by single-year age and plots Age vs Population.
- Visual features include per-age colouring, a colorbar, numeric annotations every 10 years, a dashed trend line (slope), and a small ledger showing totals and top ages.
- The notebook additionally shades ages 20–40 and computes a simple relative-drop metric compared to neighbouring age bands; it saves a highlighted image.

Run:
```powershell
cd my-work/code
python .\cso_populationbyage_galway.py
```

---

### Galway population by age — main chart
![Galway population by age](generated_charts/{{LATEST_CSOPOP}})

Caption: Population by single-year age for Galway (Galway City Council + Galway County Council). Bars are coloured by age; annotations appear every 10 years and a dashed trend line summarises the age-related slope.

### Galway population — highlighted dip (ages 20–40)
![Galway highlighted dip](generated_charts/{{LATEST_CSOPOP_HIGHLIGHT}})

Caption: Same data with ages 20–40 shaded to emphasise the dip in counts in that band; a small ledger reports summary statistics for the shaded range.

#### Notebook numeric output (Top 5 ages)

Example Top 5 single-year ages (most populous) produced by the Galway notebook. Run the notebook to refresh these numbers.

| Age | Population |
|-----:|-----------:|
| 42 | 4,570 |
| 41 | 4,562 |
| 40 | 4,489 |
| 39 | 4,332 |
| 43 | 4,294 |

---

## How to run

Install prerequisites (if needed):
```powershell
pip install pandas numpy matplotlib scikit-learn
```

General notes:
- Scripts save timestamped PNG files to `my-work/generated_charts/` to avoid overwriting previous outputs. Filenames include the CSV stem and timestamp, e.g. `cso-populationbyage_galway_2025-10-06_122737.png`.
- The notebooks print the resolved output folder when saving.

---

## Data sources and assumptions
- `projectedbirths-cso.csv` and `cso-populationbyage.csv` were sourced from the Central Statistics Office (CSO).
- Scripts expect a `Year` or `CensusYear` column and a numeric `VALUE` column. The population notebook and script parse 'Single Year of Age' labels into integers ("Under 1 year" -> 0).

---

## Dependencies
- pandas
- numpy
- matplotlib
- scikit-learn

Install with `pip install pandas numpy matplotlib scikit-learn`.

---

## Where outputs are saved
All generated plots are saved to `my-work/generated_charts/`. Filenames include a timestamp to avoid accidental overwrite. Example:

`cso-populationbyage_galway_2025-10-06_122737.png`

---

## Output images

The repository saves a few illustrative PNG images under `my-work/generated_charts/`. Example files you may find there:

- `projected_births_YYYY-MM-DD_HHMMSS.png` — plot of historical births and linear projection (Assignment 1).
- `cso-populationbyage_galway_YYYY-MM-DD_HHMMSS.png` — main bar chart of population by single-year age for Galway (Assignment 2).
- `cso-populationbyage_galway_highlight_YYYY-MM-DD_HHMMSS.png` — the same chart with ages 20–40 shaded and a short ledger summarising the relative drop.

These files are produced by the scripts and by the notebook when run.

## Understanding the outputs

Short guidance to interpret the generated images:

- Projected births plot (`projected_births_...png`):
	- Blue points are historical observed values (annual totals).
	- A dotted blue fitted line shows the model fit over the historical years.
	- A solid contrasting line shows the linear projection into the future.
	- Axis limits are chosen to include both historical and projected values; check the legend and title for the projection horizon.

- Galway population by age (`cso-populationbyage_galway_...png`):
	- X axis: single-year ages (0, 1, 2, ...). 'Under 1 year' is shown at age 0.
	- Y axis: population counts for each age (Galway City + County combined, both sexes).
	- Bars are coloured by age (a continuous colormap) and a vertical colorbar shows the age mapping.
	- Numeric annotations are shown above bars every 10 years (0, 10, 20, ...).
	- A dashed red trend line shows a simple linear fit across ages; the legend lists the slope in population per year of age.
	- A small ledger box shows the total population, approximate median age, and the top 5 single-year ages by population.

- Highlighted dip image (`cso-populationbyage_galway_highlight_...png`):
	- The ages 20–40 are shaded to emphasise the observed dip in counts in that band.
	- A small annotation box reports the total population in that range and a simple relative-drop metric compared with neighbouring age bands.

Tips:
- If you want to inspect the underlying numbers, run the notebook cells to produce `top5` and `decade_df` tables or open the CSV inputs in a spreadsheet.
- For reproducible outputs, run the scripts from `my-work/code/` so the CSV search heuristics find the correct data files.


## Notes and future improvements
- Add CLI flags to control projection horizon, output folder, and filename format.
- Export CSV summaries for each analysis.
- Add more detailed demographic modelling for robust projections.

---

## Contact
If you need clarifications on the code or data, contact the author (Edward Cronin) at g00425645@atu.ie.
