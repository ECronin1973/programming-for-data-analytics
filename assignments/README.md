# 📑 Assignments – Programming For Data Analytics 2025/2026

This folder contains all formally assessed tasks for the **Programming For Data Analytics** module.  
Each assignment demonstrates applied skills in Python programming, data analysis, visualisation, and workflow organisation, completed during the 2025/2026 academic year.

---

## 📂 Contents
- Individual assignment notebooks and scripts, each with clear documentation and outputs.
- Supporting datasets used for analysis.
- notes where required to explain methodology and results.

---

## 🎯 Purpose
The assignments showcase:
- Practical application of module concepts.
- Use of Python libraries for data handling, visualisation, and statistical analysis.
- Reviewer‑friendly documentation and repository organisation.

---

## 👤 Author
- **Name:** Edward Cronin  
- **Student ID:** g00425645  
- **Email:** g00425645@atu.ie

---

## ▶️ How to Run

1. Clone the repository and navigate to the `Assignments` folder:
   ```bash
   git clone https://github.com/EdwardCronin1973/programming-for-data-analytics.git
   cd programming-for-data-analytics/Assignments
    ```

2. Install required packages (see requirements.txt in the root):
```bash
pip install -r ../requirements.txt
```

3. Open the assignment notebooks in Jupyter or VS Code:
```bash
jupyter notebook
```
Then select the relevant .ipynb file.

4. Run all cells in order to reproduce the analysis and outputs

5. Run Scripts directly from the command line where applicable:
```bash
python <input script file name>
```

6. all output files (plots, CSVs) will be automatically saved in the `plots/` or `data/` subfolders as specified in each assignment.

---

## Table of Contents
- [Assignment 02 – Bank Holidays](#️-assignment-02--bank-holidays)
    - [Part A: Display All Bank Holidays](#-part-a-display-all-bank-holidays)
    - [Part B: Display Unique Bank Holidays in Northern Ireland](#-part-b-display-unique-bank-holidays-in-northern-ireland)
- [Assignment 03 – Email Domain Analysis (Pie Chart)](#️-assignment-03--email-domain-analysis-pie-chart)
    - [Pie Chart of Email Domains](#-pie-chart-output)
- [Assignment 05 – Population Analysis](#-assignment-05--population-analysis-by-sex-and-age)
    - [Task A — Sex-Based Age Analysis (70%)](#task-a--sex-based-age-analysis-70)
    - [Task B - Age-Band Sex Comparison (20%)](#task-b----age-band-sex-comparison-20)
    - [Task C - Regional Sex Difference Analysis (10%)](#task-c---regional-sex-difference-analysis-10)
- [Assignment 06: Climate Data Analysis – Summer 2025, Knock Airport](#-assignment-06-climate-data-analysis--summer-2025-knock-airport)
    - [Temperature Analysis (60% of marks)](#temperature-analysis-60-of-marks)
    - [Windspeed Analysis (40% of marks)](#windspeed-analysis-40-of-marks)

---

## Assignment 02 – Bank Holidays

For this assignment, I worked with two Python scripts that connect to the UK Government’s public API. The aim was to pull down and analyse bank holiday data, focusing specifically on Northern Ireland.

## Part A: Display All Bank Holidays

The first part of the task was fairly straightforward: I had to write a Python script that talks to the UK Government’s bank holidays API and prints out all the holidays for Northern Ireland. Interestingly, some of these dates overlap with holidays in England, Wales, or Scotland, so it was important to recognise that the dataset isn’t unique to one region.

### 🎯 Learning Objectives

From Part A, I was expected to:

- Learn how to connect to a RESTful API using Python and the requests library.
- Understand how to parse JSON data and extract useful information.
- Focus on filtering results so they only show Northern Ireland’s holidays.
- Present the output neatly in the terminal so it’s easy to read.

### 📁 Source File

The script for Part A is saved in the root folder of the repo as: 
`assignment02-bankholidays.py`

### ▶️ Run the program from the root directory using Python:

To run the program, I just used:
```python
python assignment02-bankholidays.py
```

#### Sample Output

```plaintext
Bank Holidays in Northern Ireland:
2025-12-25 - Christmas Day
2025-12-26 - Boxing Day
2026-01-01 - New Year’s Day
2026-03-17 - St Patrick’s Day
2026-04-03 - Good Friday
2026-04-06 - Easter Monday
2026-05-04 - Early May bank holiday
2026-05-25 - Spring bank holiday
2026-07-13 - Battle of the Boyne (Orangemen’s Day)
2026-08-31 - Summer bank holiday
2026-12-25 - Christmas Day
2026-12-28 - Boxing Day
2027-01-01 - New Year’s Day
2027-03-17 - St Patrick’s Day
2027-03-26 - Good Friday
2027-03-29 - Easter Monday
2027-05-03 - Early May bank holiday
2027-05-31 - Spring bank holiday
2027-07-12 - Battle of the Boyne (Orangemen’s Day)
2027-08-30 - Summer bank holiday
2027-12-27 - Christmas Day
2027-12-28 - Boxing Day
2028-01-03 - New Year’s Day
2028-03-17 - St Patrick’s Day
2028-04-14 - Good Friday
2028-04-17 - Easter Monday
2028-05-01 - Early May bank holiday
2028-05-29 - Spring bank holiday
2028-07-12 - Battle of the Boyne (Orangemen’s Day)
2028-08-28 - Summer bank holiday
2028-12-25 - Christmas Day
2028-12-26 - Boxing Day
```

*This gave me a full list of holidays, including ones that are shared with other UK regions.*

## Part B: Display Unique Bank Holidays in Northern Ireland

Part B built directly on Part A. Instead of just listing all holidays, the challenge was to figure out which ones are unique to Northern Ireland. That meant comparing the Northern Ireland dataset against England, Wales, and Scotland, and then filtering out any dates that were shared. This part was more about applying logic and comparison rather than just displaying data.

## 🎯 Learning Objectives

From Part B, I learned how to:

- Compare structured datasets across multiple regions.
- Use set logic in Python to identify values that only appear in Northern Ireland.
- Apply conditional filtering to make sure the results were accurate.
- Display the unique holidays clearly in the terminal.

## 📁 Source File

The script for Part B is also in the root folder and is saved as:
`assignment02-bankholidays-ni.py`

#### Run the program from the root directory using Python:

To run the program, I used:
```python
python assignment02-bankholidays-ni.py

```

#### Sample Output

This showed me which holidays are specific to Northern Ireland and not celebrated elsewhere in the UK.

```plaintext
Example of Unique Bank Holidays in Northern Ireland:
2025-07-14 - Battle of the Boyne (Orangemen’s Day)
2026-03-17 - St Patrick’s Day
2026-07-13 - Battle of the Boyne (Orangemen’s Day)
2027-03-17 - St Patrick’s Day
2027-07-12 - Battle of the Boyne (Orangemen’s Day)
2028-03-17 - St Patrick’s Day
2028-07-12 - Battle of the Boyne (Orangemen’s Day)
```

### Resources for Completion of Assignment 02

To get through both parts of the assignment, I leaned on a mix of academic materials from ATU and online tutorials. These helped me understand JSON structures, how APIs work, and how to compare datasets effectively.

#### 🏫 Academic Materials from ATU

**Lecture: Representing Data**

The lecture from [Module 4369 – Programming for Data Analytics](https://vlegalwaymayo.atu.ie/course/view.php?id=12815) explained JSON and APIs. This was crucial for Part A because I needed to know how the API delivered data before I could parse it.

**Assignment Brief**

The brief itself guided me on what exactly to do: first extract Northern Ireland’s holidays, then identify which ones were unique. Without this, I wouldn’t have known how Part B linked to Part A.

**Lab Exercise: Topic 01 – Representing Data**

The lab exercise [Lab 02 Datarepresentation.pdf](https://vlegalwaymayo.atu.ie/pluginfile.php/1590492/mod_url/intro/Lab%2001%20Datarepresentation.pdf?time=1759329869806), gave me hands-on practice with JSON in Python. This was especially useful for Part B, where I had to loop through data and apply filters.

#### 🌐 Online Tutorials and Best Practices

[W3Schools – Python JSON Guide](https://www.w3schools.com/python/python_json.asp)

This helped me figure out how to convert JSON into Python dictionaries and loop through them. I used this knowledge in both parts, but especially in Part B when I had to apply conditional logic.

[Real Python – API Integration Guide](https://realpython.com/python-requests/)

This tutorial taught me how to handle API requests properly, including error handling and formatting the output. It made my scripts more reliable and easier to read.

### 🧠 Summary of Learning Outcomes

By finishing Assignment 02, I gained practical skills in:

- Using Python’s requests library to connect to APIs.
- Parsing and navigating JSON data.
- Comparing datasets using set logic and filtering.
- Writing Python scripts that are clear, structured, and easy to run.
- Following best practices for documentation and code readability.
- Using both academic and online resources to support my learning.

Overall, this assignment gave me a solid foundation in working with real-world data sources and reinforced the importance of clean, maintainable code in data analytics.

### 📖 References

- **ATU Lecture: Representing Data** – Helped me understand JSON and APIs, which was essential for Part A.
- **Assignment Brief** – Provided the step-by-step instructions that linked Part A and Part B together.
- **ATU Lab Exercise** – Showed me how to fetch and process JSON data, which I applied when filtering unique holidays in Part B.
- **W3Schools Python JSON Guide** – Guided me on converting JSON into Python dictionaries and looping through data, used in both parts.
- **Real Python API Integration Guide** – Improved my API handling and output formatting, making my scripts more robust and readable.

# END

---

## 🏛️ Assignment 03 – Email Domain Analysis (Pie Chart)

The task this time was to work with a dataset of 1,000 individuals and focus on their email addresses. The notebook had to pull out the domain part of each email, count how often each one appeared, and then show the results in a pie chart. Since there were only three unique domains in the dataset, the chart displayed all of them directly without needing to group or simplify the data.

### 📍 Task: Visualise Email Domains

The notebook was designed to load a CSV file, extract the domain portion of each email address, calculate how frequently each domain appeared, and then generate a pie chart to display the distribution. Because the dataset only contained three unique domains, the chart showed them all clearly without any further grouping.

### 🎯 Learning Objectives

From this assignment, I was expected to:
- Learn how to load and inspect structured CSV data using pandas.
- Understand how to extract domain names from email addresses using string operations and regular expressions.
- Count domain frequencies and identify unique domain types.
- Present the results visually by generating and styling a pie chart with matplotlib and seaborn.
- Save the chart so it could be included in reports or submissions.


## 📁 Source Files

| File Path | Description |
|-----------|-------------|
| `assignments/assignment03-pie.ipynb` | Main notebook for Assignment 03. Loads the dataset, extracts email domains, counts them, and creates a pie chart. |
| `assignments/data/assignment03_people.csv` | Dataset of 1,000 individuals. The `Email` column is used to extract domain names. |

### ▶️ Run the notebook

To run the notebook from the root directory, I used:
```bash
jupyter notebook assignments/assignment03-pie.ipynb
```

### Sample Output

When executed, the notebook printed a frequency table and displayed a pie chart showing the distribution of email domains.

```plaintext
📌 Total unique email domain types: 3
📊 Domain frequency table:
domain
example.org    341
example.com    339
example.net    320
Name: count, dtype: int64
```

### 📊 Pie Chart Output

The pie chart below visualises the distribution of all email domain types found in the dataset:

![Pie chart of email domains](plots/assignment-03-pie-chart.jpg)

### 📚 Resources for Completion of Assignment 03

To complete this assignment, I relied on academic materials, technical documentation, and online tutorials. These helped me understand data extraction, string manipulation, and visualisation techniques.

#### 🏫 Academic Materials from ATU

**Lecture: Acquiring Data**

I viewed the lecture in [Module 4369 – Programming for Data Analytics](https://vlegalwaymayo.atu.ie/course/section.php?id=327540), which explained how to acquire and process datasets from different sources. This was essential for preparing the CSV file used in the notebook.

**Assignment Brief**

I followed the instructions in [Assignment 3](https://vlegalwaymayo.atu.ie/mod/page/view.php?id=1204040), which outlined the task of extracting email domains and visualising them using a pie chart. The brief guided the structure and focus of my notebook.

#### 🌐 Online Tutorials and Best Practices

**pandas Documentation**

Pandas Documentation – Helped me use str.extract() and value_counts() to extract domain names and count their frequency.
- [str.extract() explained](https://pandas.pydata.org/docs/reference/api/pandas.Series.str.extract.html#pandas.Series.str.extract)
- [value_counts() explained](https://pandas.pydata.org/docs/reference/api/pandas.Series.value_counts.html).

**matplotlib Pie Chart Guide**

The [matplotlib guide](https://matplotlib.org/stable/gallery/pie_and_polar_charts/pie_features.html) supported the creation of a styled pie chart with labels, colours, and layout adjustments.

**seaborn Documentation**

I used [**seaborn**](https://seaborn.pydata.org/) to apply a pastel colour palette for clarity. The [colour palettes tutorial](https://seaborn.pydata.org/tutorial/color_palettes.html) helped me select and apply consistent colours.


### 🧠 Summary of Learning Outcomes

By completing Assignment 03, I learned how to:
- Load and inspect structured data with pandas.
- Extract and manipulate strings using regular expressions.
- Count and compare categorical values in datasets.
- Visualise categorical distributions with pie charts in matplotlib and seaborn.
- Produce clear, reproducible notebooks suitable for academic submission.

This assignment strengthened my ability to combine data analysis with visualisation, which is a key skill in data analytics and reporting.


# END

---

# 📊 Assignment 05 – Population Analysis by Sex and Age

For this assignment, I worked with official census statistics to explore population data broken down by sex and single year of age. The main goal was to clean, transform, and analyse demographic data using Python and pandas, while keeping the notebook clear, reproducible, and easy to follow.


## Task A — Sex-Based Age Analysis (70%)

The first part of the task focused on looking at differences between males and females across age groups in Ireland. Specifically, I had to:

- Calculate the weighted mean age for each sex.
- Measure the difference between sexes across single-year age groups.

This analysis was done at the national level only, so regional breakdowns were not required.

## 📚 Learning Objectives

From this task, I was expected to:

- Learn how to load and clean raw CSV data using pandas.
- Pivot the dataset to compare population counts by sex across age groups.
- Compute weighted statistics such as mean, median, and standard deviation.
- Visualise distributions using parametric bell curves and kernel density estimation (KDE).
- Export tidy, analysis-ready tables that could be reused or reviewed later.

## 🧰 Notebook Structure and Helper Functions

To keep the notebook organised, I used a modular design with helper functions defined at the top. These helpers made the analysis easier to maintain and ensured the work was transparent and educational. Each helper was documented inline and reused throughout the notebook.

### 🔧 Key Helpers

- **Save and Display Plots**  
  Centralises logic for saving figures and displaying them inline.  
  Ensures consistent formatting and reproducibility.  
  → [`matplotlib.pyplot.savefig`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.savefig.html)

- **I/O and Loader Helpers**  
  Handle robust file loading and saving using canonical paths (e.g. `DATA_DIR`).  
  Avoid hardcoded paths and support fallback to in-memory data.  
  → [`pathlib.Path`](https://docs.python.org/3/library/pathlib.html), [`pandas.read_csv`](https://pandas.pydata.org/docs/reference/api/pandas.read_csv.html)

- **Statistical Computation**  
  Perform reusable calculations such as weighted mean and standard deviation.  
  Keep analysis cells focused on interpretation.  
  → [`numpy.average`](https://numpy.org/doc/stable/reference/generated/numpy.average.html)

- **Plotting (Bell Curve and KDE)**  
  Generate consistent visualisations with clear styling.  
  → [`seaborn.kdeplot`](https://seaborn.pydata.org/generated/seaborn.kdeplot.html), [`matplotlib.pyplot.bar`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.bar.html)

- **Top-N Age Display**  
  Show a compact preview of the top age rows for each sex.  
  → [`pandas.DataFrame.sort_values`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.sort_values.html)

- **Tidy Age-Difference Loader**  
  Load cleaned age-by-sex data with normalised column types.  
  → [`pandas.Series.astype`](https://pandas.pydata.org/docs/reference/api/pandas.Series.astype.html)

- **Administrative County Builder**  
  Construct a tidy CSV showing population differences by age and sex, including county breakdowns.  
  → [`pandas.DataFrame.to_csv`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.to_csv.html)

### 🧠 Why This Structure?

For this assignment, I separated the helper functions from the main analysis cells. Doing this made the notebook much easier to maintain and extend, and it also kept the workflow clear for anyone reviewing the work. By having the helpers defined at the top, I could reuse them across multiple tasks or datasets without rewriting code.

Each analysis cell then called these helpers to perform specific tasks — for example, comparing sexes in an age band, plotting distributions, or identifying differences. This modular approach kept the notebook tidy and pedagogically clear, which was important for both learning and reproducibility.

#### 📖 References:  
- [Real Python – Python Modules and Packages](https://realpython.com/python-modules-packages/) helped me understand how to structure reusable code blocks.
- [GeeksforGeeks – Python Helper Functions](https://www.geeksforgeeks.org/python-helper-functions/) gave practical examples of how helper functions improve readability.
- [Wikipedia – DRY Principle](https://en.wikipedia.org/wiki/Don%27t_repeat_yourself) reinforced the importance of avoiding repetition and keeping code concise.

## 📁 Source File

The notebook for this assignment is saved as: 
[`assignment05-population.ipynb`](https://github.com/ECronin1973/programming-for-data-analytics/blob/main/assignment05-population.ipynb)

## How to run the notebook

1. Ensure you have Python 3.x installed with the required libraries: `pandas`, `numpy`, `matplotlib`, and `seaborn`.
2. Download the repository and navigate to the root directory.
3. Run the notebook using Jupyter:
```bash
jupyter notebook assignment05-population.ipynb
```

## 🧹 Data Cleaning Steps

Before analysis, the raw dataset was cleaned by:

- Dropping metadata columns that weren’t needed.
- Filtering to keep only rows labelled ‘Male’ and ‘Female’.
- Standardising age labels (e.g. converting “Under 1 year” to 0).
- Removing non-numeric age entries and converting types.
- Ensuring all population counts were stored as integers.

## 📈 Pivot Table Creation

Once cleaned, the data was reshaped into a pivot table with:

- **Rows**: Single year of age  
- **Columns**: Sex ('Male', 'Female')  
- **Values**: Population counts

This made it easy to directly compare male and female population counts across age groups.

## 🧮 Statistical Analysis

Finally, the notebook computed several weighted statistics for each sex:

- **Weighted Mean Age** — average age weighted by population count  
- **Weighted Standard Deviation** — spread of ages around the weighted mean  
- **Weighted Median Age** — age at which half the population is younger and half is older

Each of these statistics was saved to CSV files to ensure reproducibility and allow for downstream use.

## 🔍 KDE and Bell Curve Visualisation

As part of the analysis, I produced two different visualisations to show how age is distributed by sex in Ireland. The first was a parametric bell curve, which uses the weighted mean and standard deviation to approximate a normal distribution. The second was a kernel density estimate (KDE), which is based directly on the actual age counts and doesn’t assume the data follows a normal shape.

Both plots were saved as PNG files and designed to be clear and accessible for reporting.


### 📸 Visual Outputs

The notebook generated two main plots, saved in the root plots/ folder:

![Parametric bell curves (approx normal) - assignment 05](plots/assignment05-age-bell-curve.png)
  
_Parametric bell curves generated using the weighted mean (μ) and weighted standard deviation (σ) for each sex. Useful for a concise, parametric comparison but assumes normality._

![Weighted KDE of age by sex - assignment 05](plots/assignment05-age-kde.png)  
_Weighted KDE computed from the single-year age counts; this non-parametric curve reveals the actual shape of the distribution (skew, modes, tails) that a simple bell curve may miss._

**Interpretation**: The KDE should be used as the primary visual check because it reflects the real distribution shape. The bell curve is useful as a concise parametric summary, but if the KDE shows strong skew or multiple peaks, then the KDE gives a more accurate picture for interpretation and reporting.

---

## 📊 Age Difference Analysis

Another part of the notebook looked at the differences between males and females across single-year age groups. For each age, I calculated the absolute difference in population count and identified which sex had the greater number (‘Male’, ‘Female’, or ‘Equal’).

The results were exported to assignment05_age_difference_by_sex.csv, which makes it easy to use the data for further visualisation or reporting.


## 📦 Output Files

The notebook produced several outputs, both CSV tables and plots, to keep the analysis reproducible and clear:

| Filename                                      | Description                                      |
|----------------------------------------------|--------------------------------------------------|
| `assignment05_weighted_stats_by_sex.csv`     | Pivot table of population counts by age and sex |
| `assignment05_weighted_mean_std_by_sex.csv`  | Weighted mean and standard deviation by sex     |
| `assignment05_weighted_median_by_sex.csv`    | Weighted median age by sex                      |
| `assignment05-age-bell-curve.png`            | Bell curve visualisation                        |
| `assignment05-age-kde.png`                   | KDE visualisation                               |
| `assignment05_age_difference_by_sex.csv`     | Age-wise population difference by sex           |
| `assignment05-age-mean-difference-bar.png`   | Bar chart of weighted mean age by sex           |

## 📚 Dependencies

To run the notebook successfully, I needed the following Python libraries:

- `pandas` — for data manipulation  
- `numpy` — for numerical operations  
- `matplotlib` — for plotting  
- `seaborn` — for KDE visualisation  
- Python 3.x environment

## 🧠 Pedagogical Design

The notebook was deliberately designed to be:

- User-friendly — with clear comments, a modular structure, and reproducible outputs.
- Reviewer-friendly — including validation steps, consistent formatting, and saved artefacts for transparency.
- Future-proof — with reusable code blocks that can be adapted to other datasets or assignments.

---

## Task B -  Age-Band Sex Comparison (20%)

This part of the assignment looked at how males and females compare within a chosen age band. I set the target age to 35, which meant analysing the band from ages 30–40. The notebook pulled out the relevant rows, added up the totals for each sex, and then showed the difference both in numbers and percentages.

The results were displayed in a table and a bar chart, making it easy to see which sex had the majority at each age. In this band, females consistently outnumbered males, with a total difference of 1,905 people, which works out to about 3.82% of the population in that group

### ⚙️ What This Cell Does

- Loads a tidy age-by-sex table from memory or from `assignment05_age_difference_by_sex.csv`
- Filters rows where `age` is within `[target_age − 5, target_age + 5]`
- Aggregates total counts for each sex and calculates:
  - Total population
  - Difference (Male − Female)
  - Percentage difference of band total
- Saves a bar chart to `assignment05-age-group-35-sex-comparison.png`
- Displays a table with per-age breakdown and majority sex
- Prints a concise summary of the result

### ▶️ How to Run

1. Restart the notebook kernel and run all cells from the top to ensure helper functions and data loading steps are executed.
2. Run the Part B cell to perform the age-band comparison.  
   You can change `target_age = 35` to inspect other age bands.
3. Run the Part C cell to perform the regional analysis.  
   Ensure the dataset `assignment05_age_difference_by_sex_with_region.csv` has been created or loaded.


### 📊 Output Table — Ages 30–40

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

### 🧠 Interpretation

In the age band 30–40, females outnumber males by **1,905 people**, which is approximately **3.82%** of the total population in that band.

### 📂 Files Produced

- ![Age Group Comparison](plots/assignment05-age-group-35-sex-comparison.png) - bar chart

- `assignment05_age_difference_by_sex.csv` — tidy age-by-sex table

---

## Task C - Regional Sex Difference Analysis (10%)

The final part of the assignment extended the analysis to counties in Ireland. Here, I wanted to see which county had the biggest difference between males and females in the same age band (30–40).

The notebook grouped the data by county, calculated the differences, and then plotted the top 10 counties with the largest gaps. Fingal County Council came out on top, with 2,942 more females than males, which is about 5.33% of the population in that band.

The bar chart used colour coding to show whether the majority was male or female, making the differences easy to interpret at a glance.


### ⚙️ What This Cell Does

1. Loads `assignment05_age_difference_by_sex_with_region.csv`  
2. Filters to the selected age band (e.g. ages 30–40)  
3. Excludes the national total ("Ireland")  
4. Aggregates male and female counts by county  
5. Calculates signed and absolute differences  
6. Identifies the county with the largest gap  
7. Visualises the top 10 counties using a colour-coded bar chart  
8. Prints a summary of the result

### 📊 Output Table — Top 10 Counties (Female Majority)

| Administrative County                     | Male   | Female | Difference (M−F) | Majority |
|-------------------------------------------|--------|--------|------------------|----------|
| Fingal County Council                     | 26,150 | 29,092 | -2,942           | Female   |
| Cork County Council                       | 23,706 | 26,545 | -2,839           | Female   |
| South Dublin County Council               | 23,637 | 26,361 | -2,724           | Female   |
| Kildare County Council                    | 18,671 | 20,602 | -1,931           | Female   |
| Meath County Council                      | 15,981 | 17,715 | -1,734           | Female   |
| Wicklow County Council                    | 10,338 | 11,943 | -1,605           | Female   |
| Galway County Council                     | 12,421 | 13,904 | -1,483           | Female   |
| Dún Laoghaire Rathdown County Council     | 17,074 | 18,450 | -1,376           | Female   |
| Wexford County Council                    | 10,824 | 12,162 | -1,338           | Female   |
| Kerry County Council                      | 9,957  | 11,125 | -1,168           | Female   |

### 🧠 Interpretation

In this age band, Fingal County Council had the largest difference, with 2,942 more females than males. This represents about 5.33% of the population in that group.

🎨 **Legend**  
- 🔵 Blue = Male majority  
- 🌸 Pink = Female majority  
Each bar represents the absolute population difference in the selected age band.  
📍 Age Band: Ages 30–40 (Centre = 35)

### 📂 Files Produced

- ![assignment05-age-group-35-region-sex-diff.png](plots/assignment05-age-group-35-region-sex-diff.png) — bar chart

## 🧠 Personal Reflection

Assignment 05 was definitely the toughest one so far. I had to revisit earlier modules to remind myself how to apply weighted statistics and create KDE visualisations properly. I leaned heavily on the course notebooks and documentation to get everything working.

I kept the notebook modular throughout — selecting the data, aggregating it, visualising the results, and then interpreting what it all meant. Part C was particularly challenging because of the regional breakdowns, so I created a new dataset by county to make the analysis more manageable. I also tidied up the code cells so the notebook would be easier to follow and more readable overall.

## 🙏 Acknowledgements

This work was partially supported by **GitHub Copilot**, an AI-powered code completion tool developed by GitHub, which assisted in generating parts of the code.

## 📚 References and Learning Resources

The following resources were consulted and integrated throughout the notebook to support implementation, conceptual understanding, and reviewer transparency:

### 🎓 ATU Learning Materials

- **Lecture: Analysis and Some Stats**  
  [Programming For Data Analytics](https://vlegalwaymayo.atu.ie/course/view.php?id=12815)  
  Provided foundational guidance on statistical analysis and visualisation techniques.

- **Assignment 05 Brief**  
  [Assignment Instructions](https://vlegalwaymayo.atu.ie/mod/page/view.php?id=1362128)  
  Defined the three-part structure and shaped the notebook’s modular design.

### 🐍 Python Libraries and Documentation

- [`pandas`](https://pandas.pydata.org/) — data cleaning, pivoting, and exporting  
- [`NumPy`](https://numpy.org/) — weighted statistics and numeric operations  
- [`SciPy`](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.gaussian_kde.html) — KDE implementation  
- [`seaborn`](https://seaborn.pydata.org/generated/seaborn.kdeplot.html) — KDE plotting  
- [`matplotlib`](https://matplotlib.org/stable/contents.html) — bar charts and legends

### 📊 Statistical Concepts and Visualisation

- [Kernel Density Estimation (Wikipedia)](https://en.wikipedia.org/wiki/Kernel_density_estimation)  
- [Normal Distribution (Wikipedia)](https://en.wikipedia.org/wiki/Normal_distribution)  
- [Weighted Mean & Variance (Wikipedia)](https://en.wikipedia.org/wiki/Weighted_arithmetic_mean)  
- [Weighted Median (Real Statistics)](https://real-statistics.com/descriptive-statistics/measures-central-tendency/weighted-mean-and-median/)

### 📈 Data Source and Teaching Aids

![XKCD Comic](https://imgs.xkcd.com/comics/normal_distribution_2x.png)
*This comic image humorously illustrates the concept of a normal distribution, highlighting the common misconception that data should always fit a perfect bell curve. In reality, many datasets exhibit variations and deviations from this idealized shape, reminding us that statistical distributions can be complex and diverse.*

- [CSO FY006A – Population Dataset](https://ws.cso.ie/public/api.restful/PxStat.Data.Cube_API.ReadDataset/FY006A/CSV/1.0/en)  
- [GitHub Copilot](https://github.com/features/copilot) — used during development


# END

---

## 📘 Assignment 06: Climate Data Analysis – Summer 2025, Knock Airport

### 🗂️ Overview

For this assignment, I analysed climate data from Knock Airport during Summer 2025, with a particular focus on the heatwave between 10–16 July — the hottest week of the season and a record-breaking event for Ireland.

The analysis was built around two main themes:

- Temperature trends — daily and monthly summaries, seasonal comparisons.
- Windspeed behaviour — hourly patterns, rolling averages, and daily peaks.

Because the dataset was quite large, I segmented the data by season to make it easier to process. The week of 10–16 July was chosen as the main analytical window since it coincided with Ireland’s highest recorded temperatures of the year, Knock Airport’s highest July temperature on record (28.7°C), and a short-lived heatwave driven by the Azores High. This gave me the chance to explore weather extremes and think about their implications for aviation, energy, and public safety.

#### 📌 Climate Context

Met Éireann climatologist Paul Moore noted: “Ireland is experiencing the effects of climate change, and our climate projections show that our climate is going to become warmer.”

According to The Irish Times, Summer 2025 was Ireland’s warmest season since records began in 1900, with sustained heat and unusually high nighttime temperatures. The week of July 10–16 saw peaks of 31°C, marking a national heatwave. Knock Airport was one of the affected stations, recording 28.7°C — its highest July temperature on record.

#### Sources:

[Irish Times – Summer of 2025 becomes warmest on record](https://www.irishtimes.com/environment/2025/09/01/summer-of-2025-becomes-warmest-on-record-met-eireann/)

[BreakingNews.ie – July 2025 heatwave summary](https://www.breakingnews.ie/ireland/july-2025-heatwave-summary)


## 📁 Source File

The notebook for this assignment is saved as: 
[`assignment06-weather.ipynb`](https://github.com/ECronin1973/programming-for-data-analytics/blob/main/assignment06-weather.ipynb)

## How to run the notebook

1. Ensure you have Python 3.x installed with the required libraries: `pandas`, `numpy`, `matplotlib`, and `seaborn`.
2. Download the repository and navigate to the root directory.
3. Run the notebook using Jupyter:
```bash
jupyter notebook assignment06-weather.ipynb
```
4. Follow the instructions in the notebook to execute each analysis section.

---

## Temperature Analysis (60% of marks)

The first part of the assignment focused on temperature data from Knock Airport. I cleaned the raw dataset and extracted hourly values to analyse how temperatures changed during the July heatwave. This gave me the chance to look at fluctuations across the day as well as broader daily and monthly averages.

### 📊 Hourly Temperature Data
I began by examining hourly temperature readings for each day of the heatwave (10–16 July). This helped me see how temperatures rose and fell throughout the day.

**Files Generated:**
- `assignments/data/assignment06_temperature_range.csv` — Hourly temperature data  

**Plots Created:** (Plot Example for 10th July 2025, one created for each day)
![Hourly Temperature 10.07.2025](plots/assignment06_hourly_temperature_2025-07-10.png)


### 📊 The Mean Temperature Each Day
Next, I calculated the mean temperature for each day in Summer 2025. This highlighted how the heatwave compared to surrounding days and showed the daily progression of average temperatures.

**Files Generated:**
- `assignments/data/assignment06_climate_data_mean_daily_summer_2025.csv` — Daily mean temperatures  

**Plots Created:**
Daily mean temperature plot
![Daily Mean Temperature](plots/assignment06_mean_daily_custom_range.png)


### 📊 The Mean Temperature Each Month
Finally, I aggregated the data to monthly averages. This gave a broader view of how July compared to the rest of the summer season and confirmed that July was the standout month for extreme heat.

**Files Generated:**
- `assignments/data/assignment06_monthly_mean_by_season_2025.csv` — Monthly mean temperatures  

**Plots Created:**
Monthly mean temperature plot
![Monthly Mean Temperature](plots/assignment06_monthly_mean_by_season_2025.png)

---

## Windspeed Analysis (40% of marks)
The second part of the assignment focused on windspeed data. I cleaned the dataset, handled missing values, and then explored different ways of summarising and visualising windspeed behaviour during the July heatwave.

### 📊 The Windspeed
I first looked at the cleaned hourly windspeed data to get a sense of overall patterns during the week of 10–16 July 2025.

**Files Generated:**
- `assignments/data/assignment06_windspeed_cleaned_summer_2025.csv` — Cleaned windspeed data  

**Plots Created:**
![Cleaned windspeed Plot](plots/assignment06_windspeed_hourly_2025-07-10_to_2025-07-16.png)


### 📊 The Rolling 24-Hour Average Windspeed
To smooth out short-term fluctuations, I calculated a 24-hour rolling average. This helped highlight longer-term trends across the heatwave period.

**Files Generated:**
- `assignments/data/assignment06_windspeed_rolling_24hr_2025-07-10_to_2025-07-16.csv` — 24-hour rolling average  

**Plots Created:**
Rolling average windspeed plot
![Rolling Average Windspeed Plot](plots/assignment06_windspeed_rolling_24hr_2025-07-10_to_2025-07-16.png) 

### 📊 The Maximum Windspeed Each Day and Time
I then identified the maximum windspeed for each day and recorded the time it occurred. This highlighted extreme conditions and when they happened.

**Files Generated:**
- `assignments/data/assignment06_daily_max_windspeed_with_time_10_16_July_2025.csv` — Daily max windspeed with time  

**Plots Created:**
Daily max windspeed with time
![Daily max windspeed with time plot](plots/assignment06_daily_max_windspeed_line_10_16_July_2025.png)

### 📊 The Mean of the Maximum Windspeed Each Month
Finally, I aggregated the daily maximum values to monthly averages. This gave a broader view of how July compared to the rest of the summer.

**Files Generated:**
- `assignments/data/assignment06_daily_max_windspeed_July_2025.csv` — Daily max windspeed for July
- `assignments/data/assignment06_monthly_mean_of_daily_max_windspeed_July_2025.csv` — Monthly mean of daily max wind

**Plots Created:**
Monthly mean of daily max windspeed plot
![Monthly Mean of Daily Max Windspeed Plot](plots/assignment06_daily_max_windspeed_with_monthly_mean_July_2025.png)

### 🧠 Personal Reflection

This assignment was both challenging and rewarding. I had to apply the full data science process — collecting raw data, cleaning it, organising it, and then creating visualisations — all based on real climate data. Focusing on the July heatwave meant I had to carefully filter the dataset and interpret the findings in context.

From my previous assignment, I learned how useful helper functions are for breaking code into smaller parts. I used that approach again here, which made the notebook easier to follow. I revisited course materials on time series analysis, rolling averages, and seasonal patterns, and worked on improving the notebook layout so each task was clearly explained and backed up with saved outputs.

Handling missing windspeed data was a particular challenge, but I managed to produce clear plots that highlighted important trends and extreme values. I also used Copilot to help with some of the coding, which gave me a good starting point, though I spent time refining the code to make sure it was accurate and met all the assignment requirements.

### 📚 Resources and Learning Materials

This section lists the key resources consulted and integrated throughout the assignment to support implementation, conceptual understanding, and reviewer transparency.

### 🎓 ATU Learning Materials
- **Lecture: Analysis and Some Stats**  
  [Programming For Data Analytics](https://vlegalwaymayo.atu.ie/course/view.php?id=12815)  
  Provided guidance on time series analysis, rolling averages, and seasonal aggregation.

- **Assignment Brief**  
  [Assignment Instructions](https://vlegalwaymayo.atu.ie/mod/page/view.php?id=1204078)  
  Defined the assessment structure and outlined the temperature and windspeed objectives.

### 🐍 Python Libraries and Documentation
- [`pandas`](https://pandas.pydata.org/) — data cleaning, grouping, pivoting, and exporting  
- [`NumPy`](https://numpy.org/) — numeric operations and array handling  
- [`matplotlib`](https://matplotlib.org/stable/contents.html) — plotting and visual styling  
- [`seaborn`](https://seaborn.pydata.org/) — enhanced statistical visualisation  
- [`datetime`](https://docs.python.org/3/library/datetime.html) — timestamp parsing and manipulation  
- [`Pathlib`](https://docs.python.org/3/library/pathlib.html) — file path management

### 🌍 Climate Context and News Articles
- [Irish Times – Summer of 2025 becomes warmest on record](https://www.irishtimes.com/environment/2025/09/03/summer-of-2025-becomes-warmest-season-on-record-in-ireland)  
- [BreakingNews.ie – July 2025 heatwave summary](https://www.breakingnews.ie/ireland/july-2025-was-9th-hottest-on-record-with-highest-temperature-of-31-degrees-1789636.html)

### 📈 Statistical Concepts and Visualisation
- [Rolling Mean (pandas)](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.rolling.html)  
- [Time Series Analysis (Wikipedia)](https://en.wikipedia.org/wiki/Time_series)  
- [Climate Data Interpretation (Met Éireann)](https://www.met.ie/climate/what-we-measure)


# END
