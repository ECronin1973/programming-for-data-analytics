## 🧮 Programming For Data Analytics Module – 2025/2026

Welcome to Edward Cronin’s repository for the Programming For Data Analytics module. This repository contains submissions for assigned tasks, a comprehensive final project, and additional practice work completed during the academic year.

---

## 📁 Repository Structure

This repository is organised into three main sections:

- **Assignments 2025/2026**  
  Includes all formally assessed tasks from the module, demonstrating applied skills in data analysis, visualisation, and Python programming.

- **Final Project 2025/2026**  
  Integrates concepts from across the module into a single, cohesive analysis project.

- **MyWork 2025/2026**  
  Contains exploratory and practice notebooks not submitted for assessment, but useful for demonstrating progress and experimentation.

---

## 👤 Author

- **Name:** Edward Cronin  
- **Student ID:** g00425645  
- **Email:** g00425645@atu.ie

---

## 📥 How to Download This Repository

To download and run the code:

1. Visit [Edward Cronin’s Programming For Data Analytics repository](https://github.com/ECronin1973/programming-for-data-analytics)
2. Click the green **Code** button and select **Download ZIP**
3. Extract the ZIP file locally
4. Ensure Python is installed before running any scripts or notebooks

---

## 📜 Code of Conduct

A code of conduct is included in the repository to guide respectful collaboration and responsible use. Reviewers and contributors are encouraged to follow its principles.

---

## 🧠 Coding Guidelines and References

This repository follows established best practices for coding, documentation, and reproducibility in computational notebooks:

- **Jupyter Best Practices**  
  Narrative text explains the rationale behind each step, with references included where appropriate.  
  🔗 [Jupyter.org/practices](https://jupyter.org/practices)

- **The Turing Way**  
  Emphasises documenting *why* decisions were made, not just *what* was done.  
  🔗 [The Turing Way](https://the-turing-way.netlify.app/reproducible-research/overview/overview.html)

- **Diátaxis Documentation Framework**  
  Encourages separating conceptual documentation (why) from procedural steps (how), with background placed in README files.  
  🔗 [Diátaxis](https://diataxis.fr/)

- **PEP 8 – Python Style Guide**  
  Promotes clear, readable code and consistent commenting. Markdown cells in notebooks serve as the narrative layer.  
  🔗 [PEP 8](https://peps.python.org/pep-0008/)

---

## 🏛️ Assignment 02 – Bank Holidays (Part A)

### Display All Bank Holidays

This task involves writing a Python script that connects to the UK Government’s public API to retrieve a list of bank holidays. The script focuses on holidays listed under Northern Ireland, although some of these dates may also be shared with other UK regions such as England, Wales, or Scotland.

#### Learning Objectives

- Interact with a RESTful API using Python and the `requests` library
- Parse JSON responses and extract structured data
- Filter and display region-specific information
- Format terminal output for clarity and readability

#### Source File

`assignment02-bankholidays.py`

#### Run the program using Python:

```python
python assignment02-bankholidays.py
```

#### Sample Output

```plaintext
Bank Holidays in Northern Ireland:
2026-03-17 - St Patrick’s Day
2026-07-13 - Battle of the Boyne (Orangemen’s Day)
```

## 🏛️ Assignment 02 – Bank Holidays (Part B)

### Display bank Holidays Unique to Northern Ireland

This task builds on Part A by enhancing the script to identify bank holidays that are **exclusive to Northern Ireland** — those not observed in England, Wales, or Scotland. It demonstrates how to compare datasets across regions and apply conditional logic to filter unique entries.

## 🎯 Learning Objectives

By completing this task, users will learn to:

- Compare structured data across multiple regions
- Apply set logic to identify unique values
- Implement conditional filtering in Python
- Display filtered results clearly in the terminal

## 📁 Source File

This script is saved as:  
`assignment02-bankholidays-ni.py`

#### Run the program using Python:

```python
python assignment02-bankholidays-ni.py
```

#### Sample Output

When the script is executed, it should print a list of unique bank holidays in Northern Ireland that are not observed in England/Wales or Scotland.

```plaintext
Unique Bank Holidays in Northern Ireland:
2024-03-18 - St. Patrick's Day
2024-07-12 - Battle of the Boyne (Orangemen's Day)
2025-03-17 - St. Patrick's Day
2025-07-14 - Battle of the Boyne (Orangemen's Day)
2026-03-17 - St. Patrick's Day
2026-07-13 - Battle of the Boyne (Orangemen's Day)
2027-03-17 - St. Patrick's Day
2027-07-12 - Battle of the Boyne (Orangemen's Day)
```

## Further Reading and References

To help complete assignment 02 Part A and Part B, I used the following resources to learn how to work with JSON data and APIs in Python, and to compare data across multiple regions for identifying unique holidays (Part B):

- **ATU Lecture: Representing Data**  
  I watched the lecture in [25-26: 4369 -- Programming For Data Analytics](https://vlegalwaymayo.atu.ie/course/view.php?id=12815) to understand how data like JSON is used in programming and how APIs provide structured data. This helped with both retrieving the data (Part A) and comparing it across regions (Part B).

- ATU Assignment 2 Instructions
  I followed the assignment instructions provided in [Assignment 2](https://vlegalwaymayo.atu.ie/mod/page/view.php?id=1204016) to complete the task of extracting bank holidays for Northern Ireland and comparing them with those in England/Wales and Scotland.

- **ATU Lab: Topic 01 – Representing Data**  
  I followed the lab exercises in [Lab 01 Datarepresentation.pdf](https://vlegalwaymayo.atu.ie/pluginfile.php/1590492/mod_url/intro/Lab%2001%20Datarepresentation.pdf?time=1759329869806), which showed how to read JSON from the internet using Python. This was useful for accessing and printing data in Part A, and for understanding how to loop through and filter data in Part B.

- **JSON Format – json.org**  
  I used [json.org](https://www.json.org/json-en.html) to learn the basic structure of JSON, including how data is stored in key-value pairs and nested lists. This helped me understand how to navigate and compare JSON structures across different UK regions.

- **gov.uk Bank Holidays API**  
  I explored the [gov.uk bank holidays JSON feed](https://www.gov.uk/bank-holidays.json) to see how the data is organized and where to find the holidays for Northern Ireland, England and Wales, and Scotland. This was essential for comparing holiday titles and identifying which ones are unique to Northern Ireland in Part B.

- **Python Requests Library**  
  I read the [requests library documentation](https://pypi.org/project/requests/) to understand how to fetch data from a website using Python. This was used to retrieve the JSON data needed for both parts of the assignment.

- **W3Schools – Python JSON Tutorial**  
  I used [W3Schools](https://www.w3schools.com/python/python_json.asp) to learn how to convert JSON into Python dictionaries and loop through the data. This helped with extracting and comparing holiday titles across regions.

- **Real Python – API Guide**  
  I read [Real Python’s API guide](https://realpython.com/api-integration-in-python/) to learn good practices for working with APIs, including how to handle errors, validate responses, and format output clearly. This was especially helpful in making the script more robust and readable for both parts of the assignment.

## References

- [25-26: 4369 -- PROGRAMMING FOR DATA ANALYTICS MODULE](https://vlegalwaymayo.atu.ie/course/view.php?id=12815)
- [Lab 01 Datarepresentation.pdf](https://vlegalwaymayo.atu.ie/pluginfile.php/1590492/mod_url/intro/Lab%2001%20Datarepresentation.pdf?time=1759329869806)
- [json.org](https://www.json.org/json-en.html)
- [gov.uk bank holidays API](https://www.gov.uk/bank-holidays.json)
- [requests library documentation](https://pypi.org/project/requests/)
- [W3Schools Python JSON guide](https://www.w3schools.com/python/python_json.asp)
- [Real Python’s guide to working with APIs](https://realpython.com/api-integration-in-python/)

# END

---

## 🏛️ Assignment 03 – Email Domain Analysis (Pie Chart)

This notebook explores a dataset of 1,000 individuals to identify and visualise the most common email domains. It demonstrates how to extract domain names from email addresses, compute frequency counts, and generate a pie chart using Python libraries. Less frequent domains are grouped into an “Others” category to improve readability and visual clarity.

## 🎯 Learning Objectives

By completing this notebook, users will learn to:

- Load and inspect structured CSV data using pandas
- Extract domain names from email addresses using string operations
- Count domain frequencies and group low-frequency entries
- Generate and save a pie chart visualisation using matplotlib and seaborn

## 📁 Source Files

| File Path | Description |
|-----------|-------------|
| `assignments/notebooks/assignment03-pie.ipynb` | Main notebook for Assignment 03. Loads the dataset, extracts email domains, counts them, and creates a pie chart. |
| `assignments/data/people.csv` | Dataset of 1,000 individuals. The `Email` column is used to extract domain names. |

## 🧭 Implementation Approach

The notebook is implemented in modular steps:

### 1. **Load Dataset**
- Read `people.csv` into a pandas DataFrame
- Confirm presence of the `Email` column

**Why:**  
Loading the dataset into a DataFrame enables efficient manipulation and analysis. Verifying structure ensures robustness before processing.  
🔗 [pandas documentation](https://pandas.pydata.org/)


### 2. **Extract Email Domains**
- Split each email address at the `@` symbol
- Retain the domain portion (e.g. `example.org`)

**Why:**  
Domain extraction is a common string operation in data cleaning. It enables grouping by organisation or provider.  
🔗 [Python string methods](https://docs.python.org/3/library/stdtypes.html#string-methods)


### 3. **Count Domain Frequencies**
- Use `value_counts()` to tally domain occurrences
- Identify top domains and group others

**Why:**  
Frequency counts reveal dominant providers. Grouping less frequent domains into “Others” improves visual clarity.  
🔗 [pandas Series.value_counts](https://pandas.pydata.org/docs/reference/api/pandas.Series.value_counts.html)


### 4. **Generate Pie Chart**
- Plot top domains using `matplotlib` and `seaborn`
- Style chart for accessibility and save as JPG

**Why:**  
Pie charts are effective for showing proportional distribution. Saving the chart ensures reproducibility and supports reviewer access.  
🔗 [matplotlib pie chart guide](https://matplotlib.org/stable/gallery/pie_and_polar_charts/pie_features.html)


### 5. **Run the Notebook**

To execute the notebook:

```bash
cd assignments/notebooks
jupyter notebook assignment03-pie.ipynb
```

**Example output**

- Below is a sample of the first 10 rows from people.csv:

Sample of the data (`assignments/data/people.csv`) — first 10 rows (columns shown):

```
Index,User Id,First Name,Last Name,Sex,Email,Phone,Date of birth,Job Title
1,8717bbf45cCDbEe,Shelia,Mahoney,Male,pwarner@example.org,857.139.8239,2014-01-27,Probation officer
2,3d5AD30A4cD38ed,Jo,Rivers,Female,fergusonkatherine@example.net,+1-950-759-8687,1931-07-26,Dancer
3,810Ce0F276Badec,Sheryl,Lowery,Female,fhoward@example.org,(599)782-0605,2013-11-25,Copy
4,BF2a889C00f0cE1,Whitney,Hooper,Male,zjohnston@example.com,+1-939-130-6258,2012-11-17,Counselling psychologist
5,9afFEafAe1CBBB9,Lindsey,Rice,Female,elin@example.net,(390)417-1635x3010,1923-04-15,Biomedical engineer
6,aF75e6dDEBC5b66,Sherry,Caldwell,Male,kaitlin13@example.net,8537800927,1917-08-06,Higher education lecturer
7,efeb05c7Cc94EA3,Ernest,Hoffman,Male,jeffharvey@example.com,093.655.7480x7895,1984-12-22,Health visitor
8,fb1BF3FED57E9d7,Doris,Andersen,Male,alicia33@example.org,4709522945,2016-12-02,Air broker
9,421fAB9a3b98F30,Cheryl,Mays,Male,jake50@example.com,013.820.4758,2012-12-16,"Designer, multimedia"
10,4A42Fe10dB717CB,Harry,Mitchell,Male,lanechristina@example.net,(560)903-5068x4985,1953-06-29,Insurance account manager
```

### Pie Chart Output

The pie chart below visualises the distribution of the top email domains found in the dataset. Less frequent domains are grouped into an “Others” slice.

![Pie chart of email domains](assignments/data/assignment-03-pie-chart.jpg)

### References

References
ATU Lecture: Acquiring data I watched the lecture in [25-26: 4369 -- Programming For Data Analytics](https://vlegalwaymayo.atu.ie/course/view.php?id=12815) to understand how to acquire data from various sources, including downloading datasets from the web. This helped me understand the importance of data acquisition in data analytics.

ATU Assignment 3 Instructions I followed the assignment instructions provided in Assignment 3 to complete the task of extracting email domains and visualizing them using a pie chart. The instructions guided me through the steps of data extraction, processing, and visualisation.

[assignment03-pie.ipynb](assignments/notebooks/assignment03-pie.ipynb)
Main notebook for Assignment 3. It loads the dataset, extracts email domains, counts them, and creates a pie chart.

[people.csv](assignments/data/people.csv)
Dataset of 1,000 people. The Email column is used to extract domain names for analysis.

[pandas](https://pandas.pydata.org/)
Used to load the dataset (read_csv), extract email domains from strings (str.split), and count how often each domain appears (value_counts).

[matplotlib](https://matplotlib.org/)
Used to create and customize the pie chart (plot.pie), adjust layout (tight_layout), display the chart (show), and save it as an image file (savefig).

[seaborn](https://seaborn.pydata.org/)
Used to apply a pastel color palette for the pie chart (color_palette) to improve visual clarity and style.

END
---

# 📊 Assignment 05 – Population Analysis by Sex and Age

This assignment explores population data by sex and single year of age using official census statistics. It demonstrates how to clean, transform, and analyse demographic data using Python and pandas, with a strong emphasis on clarity, reproducibility, and pedagogical structure.

## Task A: 
Write a jupyter notebook that analyses the differences between the sexes by age in Ireland. 
- Weighted mean age (by sex) 
- The difference between the sexes by age 

This part does not need to look at the regions.

## 🎯 Learning Objectives

This assignment part will:

- Load and clean raw CSV data using pandas
- Pivot data to compare population counts by sex across age groups
- Compute weighted statistics (mean, median, standard deviation)
- Visualise distributions using parametric bell curves and kernel density estimation (KDE)
- Export analysis-ready tables for downstream use or review


## 🧰 Notebook Loader & Helper Functions

This notebook uses a modular design with clearly separated helper blocks to support clarity, reusability, and reviewer understanding. These helpers are defined at the top of the notebook and are reused throughout the analysis cells below.

### 📤 Utility: Save and Display Plots

- **Purpose**: Centralises logic for saving figures to disk and displaying them inline.
- **Why it matters**: Ensures consistent output format, resolution, and reproducibility across all visualisations.
- **Source**: [matplotlib.pyplot.savefig](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.savefig.html)

### 📁 I/O & Loader Helpers

- **Purpose**: Handle robust file loading and saving using canonical paths (e.g. `DATA_DIR`).
- **Why it matters**: Supports reproducibility and avoids hardcoded paths. These helpers also check for in-memory data before falling back to disk.
- **Source**: [pathlib.Path](https://docs.python.org/3/library/pathlib.html), [pandas.read_csv](https://pandas.pydata.org/docs/reference/api/pandas.read_csv.html)

### 📐 Statistical Computation Helper

- **Purpose**: Performs reusable statistical calculations (e.g. weighted mean, standard deviation).
- **Why it matters**: Keeps analysis cells clean and focused on interpretation rather than computation.
- **Source**: [pandas.DataFrame.apply](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.apply.html), [numpy.average](https://numpy.org/doc/stable/reference/generated/numpy.average.html)

### 📊 Plotting Helpers (Parametric and KDE)

- **Purpose**: Generate consistent visualisations such as bar charts, KDE plots, and annotated summaries.
- **Why it matters**: Promotes visual clarity and ensures all plots follow a consistent style and layout.
- **Source**: [seaborn.kdeplot](https://seaborn.pydata.org/generated/seaborn.kdeplot.html), [matplotlib.pyplot.bar](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.bar.html)

### 📌 Display Helper: Show Top-N Ages by Sex

- **Purpose**: Displays a compact preview of the top N age rows for each sex.
- **Why it matters**: Keeps notebook outputs readable and helps reviewers quickly inspect key data slices.
- **Source**: [pandas.DataFrame.sort_values](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.sort_values.html), [pandas.DataFrame.head](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.head.html)

### 📥 Loader: Tidy Age-Difference CSV (Robust Path Handling)

- **Purpose**: Loads the cleaned age-by-sex dataset from disk or memory, normalises column types, and ensures consistent structure.
- **Why it matters**: Enables downstream analysis cells to work reliably without repeating cleaning logic.
- **Source**: [pandas.read_csv](https://pandas.pydata.org/docs/reference/api/pandas.read_csv.html), [pandas.Series.astype](https://pandas.pydata.org/docs/reference/api/pandas.Series.astype.html)


### 🧠 Why This Structure?

Separating helpers from analysis cells allows the notebook to be:

- Easier to maintain and extend
- More readable for students and reviewers
- Reusable across multiple assignments or datasets

Each analysis cell below calls these helpers to perform specific tasks (e.g. comparing sexes in an age band, plotting distributions, identifying regional differences), keeping the workflow modular and pedagogically clear.

---

## 📁 Source File

This notebook is located at:  
[assignment05-population.ipynb](https://github.com/ECronin1973/programming-for-data-analytics/blob/main/assignments/notebooks/assignment05-population.ipynb)

## 🧹 Data Cleaning Steps

The raw dataset is cleaned by:

- Dropping metadata columns not required for analysis
- Filtering to retain only 'Male' and 'Female' rows
- Standardising age labels (e.g. converting 'Under 1 year' to `0`)
- Removing non-numeric age entries and converting types
- Ensuring all population counts are integers

## 📈 Pivot Table Creation

A pivot table is created with:

- Rows: Single year of age
- Columns: Sex ('Male', 'Female')
- Values: Population counts

This structure allows for direct comparison of male and female population counts across age groups.

## 🧮 Statistical Analysis

The notebook computes:

- **Weighted Mean Age**: Average age weighted by population count
- **Weighted Standard Deviation**: Spread of ages around the weighted mean
- **Weighted Median Age**: Age at which half the population is younger and half is older

Each statistic is calculated per sex and saved to CSV for reproducibility.

## 🔍 KDE and Bell Curve Visualisation

Two visualisations are provided:

- **Parametric Bell Curve**: Approximates a normal distribution using weighted mean and standard deviation
- **Kernel Density Estimate (KDE)**: Smoothed density based on actual age counts, without assuming normality

Plots are saved as PNG files and designed for clarity and accessibility.

### Visual outputs

Below are the two main plot outputs produced by the notebook (also saved to `assignments/data/`). These images are embedded here so reviewers can see the results without opening the notebook.

![Parametric bell curves (approx normal) - assignment 05](assignments/data/assignment-05-age-bell-curve.png)

_Parametric bell curves generated using the weighted mean (μ) and weighted standard deviation (σ) for each sex. Useful for a concise, parametric comparison but assumes normality._

![Weighted KDE of age by sex - assignment 05](assignments/data/assignment-05-age-kde.png)

_Weighted KDE computed from the single-year age counts; this non-parametric curve reveals the actual shape of the distribution (skew, modes, tails) that a simple bell curve may miss._

Interpretation (short): use the KDE as the primary visual check for the real distribution shape; use the bell-curve as a compact parametric summary. If the KDE shows strong skew or multiple peaks, prefer the KDE for interpretation and reporting.

## 📊 Age Difference Analysis

The notebook also computes:

- Absolute difference in population count between sexes at each age
- Which sex has a greater count at each age ('Male', 'Female', or 'Equal')

This is exported to `age_difference_by_sex.csv` and supports further visualisation or reporting.

## 📦 Output Files

| Filename                              | Description                                      |
|--------------------------------------|--------------------------------------------------|
| `weighted_stats_by_sex.csv`          | Pivot table of population counts by age and sex |
| `weighted_mean_std_by_sex.csv`       | Weighted mean and standard deviation by sex     |
| `weighted_median_std_by_sex.csv`     | Weighted median and standard deviation by sex   |
| `assignment-05-age-bell-curve.png`   | Bell curve visualisation                        |
| `assignment-05-age-kde.png`          | KDE visualisation                               |
| `age_difference_by_sex.csv`          | Age-wise population difference by sex           |
| `assignment-05-mean-age-bar.png`     | Bar chart of weighted mean age by sex           |

## 📚 Dependencies

- Python 3.x
- pandas
- numpy
- matplotlib
- seaborn

## 🧠 Pedagogical Design

This notebook is designed to be:

- **User-friendly**: Clear comments, modular structure, and reproducible outputs
- **Reviewer-friendly**: Explicit validation steps, consistent formatting, and saved artefacts
- **Future-proof**: Code blocks are reusable and adaptable for other datasets or assignments

---

## 🧮 Assignment 05 – Part B: Age-Band Sex Comparison

This section compares the population of males and females within a selected age band (e.g. ages 30–40) and produces both a visual and tabular summary.

---

### ⚙️ What This Cell Does

- **Data Input**  
  Loads a tidy age-by-sex table using `load_age_difference()`.  
  - Prefers in-memory `df_out`  
  - Falls back to: `assignments/data/age_difference_by_sex.csv`

- **Filtering**  
  Selects rows where `age` is within `[target_age − band, target_age + band]`.

- **Aggregation**  
  Sums `female` and `male` counts across the band.  
  Calculates:
  - Total population
  - Difference (Male − Female)
  - Percentage difference of band total

- **Visual Output**  
  Saves a compact bar chart comparing totals to:  
  `assignments/data/age_group_{target_age}_sex_comparison.png`  
  _(e.g. `age_group_35_sex_comparison.png`)_

- **Tabular Output**  
  Displays the filtered rows with a new column indicating which sex is more populous for each age.

- **Text Output**  
  Prints a concise summary:

```plaintext
Female = 25,901, Male = 23,996, Diff (M−F) = -1,905, % of Band = -3.82%
```
---

### ▶️ How to Run

1. Restart the notebook kernel and run all cells up to the one that creates `df_out`.
2. Run the Part B cell.  
 You can change `target_age = 35` to inspect other bands.

---

### 📊 Visual

![Age-Band Sex Comparison (Ages 30–40)](assignments/data/age_group_35_sex_comparison.png)

### 📊 Output Table

**Age-Band Sex Comparison Table (Ages 30–40)**

| Age | Female | Male | Difference | Majority |
|-----|--------|------|------------|----------|
| 30  | 2,052  | 1,928 | -124       | Female   |
| 31  | 2,106  | 2,014 | -92        | Female   |
| 32  | 2,148  | 2,025 | -123       | Female   |
| 33  | 2,155  | 1,993 | -162       | Female   |
| 34  | 2,267  | 2,070 | -197       | Female   |
| 35  | 2,371  | 2,168 | -203       | Female   |
| 36  | 2,439  | 2,239 | -200       | Female   |
| 37  | 2,449  | 2,276 | -173       | Female   |
| 38  | 2,556  | 2,344 | -212       | Female   |
| 39  | 2,662  | 2,421 | -241       | Female   |
| 40  | 2,696  | 2,518 | -178       | Female   |

---

### 🧠 Interpretation Guidance

> “Which sex has the larger population in the selected age band, and by how much?”

In the age band 30–40, females have a larger population than males by a total of 1,905 people, which is approximately 3.82% of the age-band total.

---

### 📂 Files Produced

- `assignments/data/age_group_{target_age}_sex_comparison.png` – bar chart
- `assignments/data/age_difference_by_sex.csv` – tidy source data

---

### 📚 References and Learning Resources

The following resources were consulted and integrated throughout the notebook to support implementation, conceptual understanding, and reviewer transparency:

#### 🎓 ATU Learning Materials

- **ATU Lecture: Analysis and Some Stats**  
  [25-26: 4369 – Programming For Data Analytics](https://vlegalwaymayo.atu.ie/course/view.php?id=12815)  
  *Use:* This lecture provided foundational guidance on statistical analysis and visualisation techniques. It helped clarify the expectations for weighted measures and KDE plots, and informed the structure of the notebook.

- **ATU Assignment 5 Instructions**  
  [Assignment 5](https://vlegalwaymayo.atu.ie/mod/page/view.php?id=1362128)  
  *Use:* The assignment brief outlined the required tasks: analysing differences between sexes by age in Ireland, computing weighted mean age (by sex), and calculating the difference between sexes by age. These instructions directly shaped the notebook’s modular design and output structure.

---

#### 🐍 Python Libraries and Documentation

- **pandas (Data Cleaning & Pivoting)**  
  [pandas documentation](https://pandas.pydata.org/)  
  *Use:* Referenced for loading CSVs, cleaning data, grouping by sex and age, pivoting tables, and exporting results. Enabled reproducible and reviewer-friendly data transformations.

- **NumPy (Weighted Averages & Numerics)**  
  [NumPy documentation](https://numpy.org/)  
  *Use:* Used for computing weighted mean, variance, and standard deviation. Also supported array manipulations and numeric precision throughout the notebook.

- **SciPy – `gaussian_kde`**  
  [SciPy KDE documentation](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.gaussian_kde.html)  
  *Use:* Practical reference for implementing weighted KDE. Informed how to supply weights and interpret bandwidth parameters.

- **seaborn – `kdeplot`**  
  [seaborn KDE documentation](https://seaborn.pydata.org/generated/seaborn.kdeplot.html)  
  *Use:* Used to plot KDEs with custom bandwidth and style options. Helped visualise age distributions clearly and accessibly.

---

#### 📊 Statistical Concepts and Visualisation

- **Kernel Density Estimation (KDE)**  
  [Wikipedia – KDE](https://en.wikipedia.org/wiki/Kernel_density_estimation)  
  *Use:* Provided conceptual background for KDE plots. Explained why KDE is preferred over parametric fits for real-world age distributions.

- **Normal Distribution (Definition & PDF)**  
  [Wikipedia – Normal Distribution](https://en.wikipedia.org/wiki/Normal_distribution)  
  *Use:* Supported the parametric bell-curve visualisation. Explained the probability density function (PDF), assumptions, and role of μ and σ.

- **Weighted Mean & Variance (Formulas & Explanation)**  
  [Wikipedia – Weighted Arithmetic Mean](https://en.wikipedia.org/wiki/Weighted_arithmetic_mean)  
  *Use:* Referenced for computing weighted mean and variance. Ensured statistical accuracy and transparency in the notebook’s calculations.

- **Weighted Median Explanation**  
  [Real Statistics – Weighted Measures](https://real-statistics.com/descriptive-statistics/measures-central-tendency/weighted-mean-and-median/)  
  *Use:* Provided conceptual steps for computing the weighted median using cumulative weights. Informed the logic used in the notebook’s median cell.

---

#### 📈 Data Source and Teaching Aids

- **CSO FY006A – Raw Population Dataset**  
  [CSO API – FY006A CSV Endpoint](https://ws.cso.ie/public/api.restful/PxStat.Data.Cube_API.ReadDataset/FY006A/CSV/1.0/en)  
  *Use:* Official source for the population data used in the notebook. Cited to ensure reproducibility and allow reviewers to re-download the exact dataset.

- **XKCD Comic – Normal Distribution**  
  [XKCD #221](https://xkcd.com/221/)  
  *Use:* Embedded in the notebook as a light-hearted teaching aid. Highlights why real data often deviates from idealised bell curves.

# END

