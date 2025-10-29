# Programming For Data Analytics Module

Welcome to Edward Cronin's repository for the Programming For Data Analytics Module 2025/2026. This repository contains the student's submissions for the module, including detailed tasks and a comprehensive project.

## Table of Contents
- [Overview](#overview)
- [Author](#author)
- [How to Download this Repository](#how-to-download-this-repository)
- [Code of Conduct](#code-of-conduct)
- [Contents](#contents)
- Assignment 2: Northern Ireland bank holidays
  - [Part A — list Northern Ireland bank holidays](#assignment-2-northern-ireland-bank-holidays)
  - [Part B — holidays unique to Northern Ireland](#assignment-2-bank-holidays-unique-to-northern-ireland)
- [Assignment 3 — domains (pie chart)](#assignment-3-domains)
- [Assignment 5 — Population by Age and Sex](#assignment-05-population-by-age-and-sex)

## Overview

This README file is structured into three main sections:

Section 1: Programming For Data Analytics Assignments 2025/2026: This section includes various tasks assigned throughout the module, showcasing the student's understanding and application of Programming For Data Analytics.

Section 2: Programming For Data Analytics Project 2025/2026: This section presents the student's final project, which integrates the knowledge and skills acquired during the course.

Section 3: MyWork 2025/2026:  This section contains students practice work which is not part of the assessment but showcases work completed throughout the course.

Feel free to explore the repository to see the students' approaches and solutions to the tasks and project. Feedback is always welcome!

## Author

__Name:__ Edward Cronin

__Student ID:__ g00425645

__Email:__ g00425645@atu.ie

## How to download this repository

Logon to GitHub to locate the student's specific repository dedicated to this project located at [My repository for programming-for-data-analytics](https://github.com/ECronin1973/programming-for-data-analytics) on GitHub .
- Click the download button.
- To run the code, ensure that python is installed.

## Code of Conduct

A code of conduct governs the use of this repository and has been uploaded within the repository for ease of reference.

## Contents

### Assignment 2: Northern Ireland bank holidays (Part A)

### Overview
This assignment involves creating a Python script that connects to the UK government's public API to get a list of bank holidays. It uses the requests library to send a GET request and then reads the JSON data returned. The script focuses on holidays listed under Northern Ireland, but some of these dates may also be shared with other UK regions like England, Wales, or Scotland.

### Objectives

- **API Interaction:** Demonstrate how to interact with a RESTful API in Python by making GET requests and parsing JSON responses.
- **Data Extraction:** Extract specific fields from the JSON payload—namely, the dates of bank holidays in Northern Ireland.
- **Output Display:** Present the extracted dates clearly in the terminal.
- **Output Formatting:** Ensure the output is clean, readable, and user-friendly, with each date printed on a separate line.

#### Code Used To Complete Part A

**The following code is used to complete Part A**

```python
# Import the requests library to make HTTP requests
https://pypi.org/project/requests/
import requests

# Define the URL for the UK government bank holidays JSON feed
url = "https://www.gov.uk/bank-holidays.json"

# Send a GET request to the URL and store the response
response = requests.get(url)

# Convert the response to a Python dictionary
data = response.json()

# Access the list of holiday events for Northern Ireland
ni_events = data['northern-ireland']['events']

# Loop through each event and print the name and date
print("Bank Holidays in Northern Ireland:")
for event in ni_events:
    name = event['title']
    date = event['date']
    print(f"{date} - {name}")

```
#### Save the assignment02-bankholidays.py program

Save the program as assignment02-bankholidays.py.

#### Run the program using Python:

```python
python assignment02-bankholidays.py
```

#### Expected Output

When the script is executed, it prints the dates and names of upcoming Northern Ireland bank holidays to the terminal. The output shown below is a truncated version created by the student for demonstration purposes:

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

```

### Assignment 2: Bank holidays unique to Northern Ireland (Part B)

### Overview
This part of the assignment involves enhancing the initial script to identify and display bank holidays that are unique to Northern Ireland, meaning they are not observed in England, Wales, or Scotland. This requires comparing the holiday titles across the different regions and filtering out any that are shared.

### Objectives
- **Data Comparison:** Compare holiday titles across Northern Ireland, England/Wales, and Scotland to identify unique holidays.
- **Conditional Logic:** Implement logic to filter out shared holidays and retain only those unique to Northern Ireland.
- **Output Clarity:** Ensure the output clearly indicates which holidays are unique to Northern Ireland, along with their dates.


#### Code Used To Complete Part B

**The following code is used to complete Part B**

```python
# Import the requests library to make HTTP requests
import requests

# Define the URL for the UK government's bank holidays JSON feed
url = "https://www.gov.uk/bank-holidays.json"

# Send a GET request to the URL and store the response
response = requests.get(url)

# Check if the request was successful (status code 200 means OK)
if response.status_code == 200:
    # Convert the response content to a Python dictionary
    data = response.json()

    # Get the list of holiday events for Northern Ireland
    ni_events = data['northern-ireland']['events']

    # Create sets of holiday titles for England/Wales and Scotland
    # These will be used to compare and find unique holidays
    ew_titles = set(event['title'] for event in data['england-and-wales']['events'])
    scot_titles = set(event['title'] for event in data['scotland']['events'])

    # Print heading for output
    print("Unique Bank Holidays in Northern Ireland:")

    # Flag to check if any unique holidays are found
    found = False

    # Loop through each Northern Ireland holiday
    for event in ni_events:
        # If the holiday title is not found in England/Wales or Scotland, it's unique
        if event['title'] not in ew_titles and event['title'] not in scot_titles:
            # Print the date and title of the unique holiday
            print(f"{event['date']} - {event['title']}")
            found = True

    # If no unique holidays were found, print a message
    if not found:
        print("No unique holidays found.")
else:
    # If the request failed, print the error status code
    print("Error fetching data:", response.status_code)

```
#### Save the assignment02-bankholidays-ni.py program

Save the program as assignment02-bankholidays-ni.py.

#### Run the program using Python:

```python
python assignment02-bankholidays-ni.py
```

#### Expected Output

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

## Assignment 3: domains

### Overview
This assignment involves creating a Jupyter notebook that analyzes a dataset of 1,000 people to extract and visualize the most common email domains. The notebook reads a CSV file containing personal information, extracts the domain names from email addresses, counts their occurrences, and generates a pie chart to display the distribution of the top email domains. Less frequent domains are grouped into an "Others" category for clarity.

### Objectives
- **Data Extraction:** Extract email domains from a dataset of 1,000 people downloaded from the web.
- **Frequency Counting:** Count the occurrences of each email domain.
- **Visualisation:** Create a pie chart to visualise the distribution of the top email domains.
- **Image Output:** Save the pie chart as a high-resolution image file (JPG).

### Files
- `assignments/notebooks/assignment03-pie.ipynb`  
  This Jupyter notebook reads `people.csv`, extracts email domains, counts their frequency, and generates a styled pie chart of the top domains. Lower-frequency domains are grouped into an "Others" slice for readability.
- `assignments/data/people.csv`  
  Downloaded dataset of 1,000 individuals. The `Email` column is used to extract domain names.

### How It Works
- Loads `people.csv` into a pandas DataFrame.
- Extracts the domain from each email address using string splitting (`@`).
- Computes domain frequencies using `value_counts()`.
- Groups less frequent domains into an "Others" category.
- Plots the top N domains as a pie chart using `matplotlib` and `seaborn`.

### How to Run
```bash
cd assignments/notebooks
jupyter notebook assignment03-pie.ipynb
```

Example output
- Pie chart of the top email domains saved as a figure when the notebook is run. The notebook also prints the top domain counts.

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

The pie chart below visualises the distribution of the top email domains found in the dataset. There are only three email domains identified and represented.

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

# Assignment 05 Population by Age and Sex

## Assignment Part 1 : Question
Write a jupyter notebook that analyses the differences between the sexes by age in Ireland.
- Weighted mean age (by sex)
- The difference between the sexes by age
**Note:** This part does not need to look at the regions.

The following is an overview, objectives, how the notebook works, example outputs from key cells, and references. Use this section as a quick guide to run and inspect the analysis results in `assignments/data`.

## Overview

The notebook fetches a raw snapshot of the CSO FY006A population table, writes the raw CSV for provenance (`population_for_analysis.csv`), prepares a cleaned pivot table of single-year ages by sex (`weighted_stats_by_sex.csv`), computes weighted descriptive statistics (mean, median, std) by sex, visualises results, and exports a tidy per-age CSV (`age_difference_by_sex.csv`).

## Objectives

- Demonstrate downloading and persisting official data for reproducibility.
- Clean and standardise single-year-of-age population counts.
- Compute population-weighted mean, median and standard deviation by sex.
- Produce two core visualisations: a weighted-mean bar chart and an age-by-age Male−Female difference line plot.
- Export tidy CSVs for inspection and downstream analysis.

## How the notebook works (step-by-step)

1. Consolidated imports and path setup (defines `base_data_dir`, `DATADIR`, `FILENAME` and `FULLPATH`).
2. Fetch raw CSO CSV from the FY006A endpoint and save it to `assignments/data/population_for_analysis.csv`.
3. Read the saved CSV, drop non-data metadata columns, keep only `Sex` rows that are `Male` or `Female`, normalise age labels (replace `Under 1 year` → `0`), coerce ages and counts to numeric types.
4. Pivot into `df_anal` with ages as the index and `Female`/`Male` as columns and save as `assignments/data/weighted_stats_by_sex.csv`.
5. Compute weighted mean and weighted standard deviation per sex using NumPy's weighted average (saved to `weighted_mean_std_by_sex.csv`).
6. Compute weighted median per sex using cumulative weights (saved to `weighted_median_std_by_sex.csv`).
7. Create two visualisations: (a) bar chart of weighted means with value labels, (b) line chart of age-by-age Male−Female difference annotated with min/max.
8. Export a tidy `age_difference_by_sex.csv` that includes `sex_greater_age_difference` (Male/Female/Equal) for each age.

## 📊 Weighted Mean Age (By Sex)

The weighted mean is a statistical measure that calculates the average of a set of values, where each value contributes proportionally to its assigned weight. Unlike the arithmetic mean, which treats all values equally, the weighted mean adjusts for the relative importance, frequency, or reliability of each observation.

### 🧮 Formula

$$
\text{Weighted Mean} = \frac{\sum_{i=1}^{n} x_i \cdot w_i}{\sum_{i=1}^{n} w_i}
$$

Where:
- \(x_i\) = value of the \(i\)-th data point  
- \(w_i\) = weight of the \(i\)-th data point  
- \(n\) = total number of data points

### 🔗 References
- [Pandas Documentation on Weighted Mean](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.mean.html)
- [Numpy Documentation on Average](https://numpy.org/doc/stable/reference/generated/numpy.average.html)
- [Pandas Documentation on Series](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.html)

```python
# 📁 File path
filepath = output_path

# 📥 Load pivot table
df_anal = pd.read_csv(filepath, index_col=0)

# 🧮 Compute weighted mean and weighted std for each sex, save to CSV
results = []
for sex in df_anal.columns:
    weights = df_anal[sex].fillna(0).astype(float)
    ages = df_anal.index.astype(float)

    if weights.sum() > 0:
        wmean = float(np.average(ages, weights=weights))
        wvar = float(np.average((ages - wmean) ** 2, weights=weights))
        wstd = float(np.sqrt(wvar))
        total = int(weights.sum())
        print(f"{sex}: Weighted mean age = {wmean:.2f}, weighted std = {wstd:.2f}")
    else:
        wmean = float('nan')
        wstd = float('nan')
        total = 0
        print(f"{sex}: No population data available")

    results.append((sex, total, wmean, wstd))

mean_std_df = pd.DataFrame(results, columns=['sex', 'total_population', 'weighted_mean_age', 'weighted_std_age']).set_index('sex')

# Save to filename
mean_std_filename = 'weighted_mean_std_by_sex.csv'
mean_std_path = os.path.join(DATADIR, mean_std_filename)
os.makedirs(DATADIR, exist_ok=True)
mean_std_df.to_csv(mean_std_path)
print('\nSaved weighted mean & std to', os.path.abspath(mean_std_path))

# Display results
mean_std_df
```

## Probability Density Function

$ f(x) = \frac{1}{\sqrt{2 \pi \sigma^2}} e^{-\frac{(x - \mu)^2}{2 \sigma^2}} $

https://en.wikipedia.org/wiki/Normal_distribution






## Weighted Median (by Sex)

The **weighted median** is the age at which half of the weighted population is younger and half is older. It accounts for the number of individuals at each age, making it more robust than the mean when data is skewed.

### 📘 Definition

Given:
- \(x_i\): sorted age values  
- \(w_i\): weights (e.g., population counts)

The weighted median is the smallest age \(x_j\) such that:

$$
\sum_{i=1}^{j} w_i \geq \frac{\sum_{i=1}^{n} w_i}{2}
$$

If the cumulative weight equals exactly half the total at two adjacent ages, the median is the average of those two.

### 🔗 References
- [NumPy `average()` method](https://numpy.org/doc/stable/reference/generated/numpy.average.html)  
  While NumPy does not directly support weighted medians, its `average()` method is commonly used for weighted means and forms the basis for computing weighted variance and standard deviation.

- [Real Statistics: Weighted Median](https://real-statistics.com/descriptive-statistics/measures-central-tendency/weighted-mean-and-median/)  
  Offers a clear explanation of how the weighted median is calculated, including step-by-step logic using cumulative weights and sorted values.

- [pandas Series API](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.html)  
  pandas provides `.median()` for Series and DataFrames, but does not natively support weighted medians. Custom logic using cumulative weights is required.

```python
median_results = []

for sex in df_anal.columns:
    weight_series = df_anal[sex].fillna(0).astype(float)
    age_index = df_anal.index.astype(float)

    weight_values = weight_series.to_numpy()
    age_values = age_index.to_numpy()

    if weight_values.sum() > 0:
        cutoff = weight_values.sum() / 2.0
        cumsum = weight_series.cumsum()
        mask = cumsum >= cutoff
        if mask.any():
            wmedian = float(age_index[mask][0])
        else:
            wmedian = np.nan
    else:
        wmedian = np.nan

    median_results.append((sex, wmedian))

# 📊 Create median DataFrame
median_df = pd.DataFrame(median_results, columns=['sex', 'weighted_median_age']).set_index('sex')
median_df

```
## Weighted Standard Deviation (by Sex)

The **weighted standard deviation** measures how spread out the ages are, accounting for population size at each age.

#### 📘 Formula

Let \(\bar{x}_w\) represent the **weighted mean**, calculated as the average of values weighted by their respective frequencies or importance.

$$
\sigma_w = \sqrt{ \frac{ \sum w_i (x_i - \bar{x}_w)^2 }{ \sum w_i } }
$$

Where:
- \(x_i\): age values  
- \(w_i\): weights  
- \(\bar{x}_w\): weighted mean age

### 🔗 References for Weighted Standard Deviation

- [NumPy `average()` method](https://numpy.org/doc/stable/reference/generated/numpy.average.html)  
  Used to compute weighted means and intermediate steps for weighted variance and standard deviation. Supports the `weights` parameter for efficient calculation.

- [Real Statistics: Weighted Mean and Standard Deviation](https://real-statistics.com/descriptive-statistics/measures-central-tendency/weighted-mean-and-median/)  
  Provides formulas and examples for computing weighted standard deviation, including the use of weighted variance as a precursor.

- [pandas Series API](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.html)  
  pandas supports `.std()` for standard deviation, but does not natively support weighted standard deviation. Custom logic using NumPy or manual weighting is required.

```python
# 🧮 Compute weighted standard deviation by sex
std_results = []

for sex in df_anal.columns:
    weight_series = df_anal[sex].fillna(0).astype(float)
    age_index = df_anal.index.astype(float)

    weight_values = weight_series.to_numpy()
    age_values = age_index.to_numpy()

    if weight_values.sum() > 0:
        wmean = np.average(age_values, weights=weight_values)
        wstd = float(np.sqrt(np.average((age_values - wmean) ** 2, weights=weight_values)))
    else:
        wstd = np.nan

    std_results.append((sex, wstd))

# 📊 Create std DataFrame
std_df = pd.DataFrame(std_results, columns=['sex', 'weighted_std_age']).set_index('sex')
std_df
```

## Example outputs (extracted from generated CSV files)

These snippets are taken directly from the CSV files produced when the notebook was executed in this workspace. They reflect the actual saved outputs in `assignments/data`.

- Raw data download and save confirmation (notebook printout):

```
Fetching raw data from URL: https://ws.cso.ie/public/api.restful/PxStat.Data.Cube_API.ReadDataset/FY006A/CSV/1.0/en
Saved raw population data to C:\Users\eCron\OneDrive\Documents\ATU_CourseWork\Programming For Data Analytics\programming-for-data-analytics\assignments\data\population_for_analysis.csv
```

- Pivot preview (`assignments/data/weighted_stats_by_sex.csv`) — first 6 rows:

```
Single Year of Age,Female,Male
0,1761.625,1850.625
1,1721.5625,1804.6875
2,1810.875,1889.75
3,1842.6875,1937.5625
4,1863.6875,1980.375
```

- Weighted mean & std (`assignments/data/weighted_mean_std_by_sex.csv`):

```
sex,total_population,weighted_mean_age,weighted_std_age
Female,162786,38.9397958987787,22.998989559036303
Male,159034,37.7394477371039,22.67120435900202
```

- Weighted median & std (`assignments/data/weighted_median_std_by_sex.csv`):

```
sex,weighted_median_age,weighted_std_age
Female,39.0,22.998989559036303
Male,38.0,22.67120435900202
```

## Difference between sexes in Age Groups

This generates a CSV (`age_difference_by_sex.csv`) with age-by-age population counts and the difference (Male − Female).

How the cell works (summary):
- It uses the in-memory pivot `df_anal` created earlier (run the pivot cell that produces `df_anal` before running this cell).
- The pivot index is converted to numeric ages and rows are sorted by age.
- `Male` and `Female` counts are extracted; missing sex columns are filled with zeros to avoid errors.
- A tidy DataFrame is created with columns: `age`, `female`, `male`, `difference` (male − female), and `sex_greater_age_difference`.
- The DataFrame is written to `assignments/data/age_difference_by_sex.csv` and a small preview is displayed.

Inputs and outputs:
- Input: `df_anal` (pivot table; index = single-year ages; expected columns include `Male` and `Female`).
- Output: `assignments/data/age_difference_by_sex.csv` (tidy CSV with columns: `age`, `female`, `male`, `difference`, `sex_greater_age_difference`).

Notes for students and debugging tips:
- If you get a FileNotFoundError, run the pivot cell (the one that creates `df_anal`) first.
- If one sex column is missing, the code uses zeros for that sex and the `difference` will show the imbalance accordingly.
- The `sex_greater_age_difference` column contains `Male`, `Female`, or `Equal`.
- After running this cell, open `assignments/data/age_difference_by_sex.csv` to inspect age-specific differences in a spreadsheet or with pandas.

```python
# 🗃️ Create and save age_difference_by_sex.csv with columns: age, female, male, difference

AGE_DIFF_FILENAME = "age_difference_by_sex.csv"

# Simplified: always use the in-memory pivot `df_anal` created earlier.
# This keeps the notebook straightforward for students and removes file-branch complexity.
if 'df_anal' in globals():
    pivot = df_anal.copy()
else:
    raise FileNotFoundError('df_anal not found in memory; run the pivot cell that creates df_anal before running this cell')

# Ensure index is numeric and sorted (simple, robust conversion)
pivot_index_numeric = pd.to_numeric(pivot.index.to_series(), errors='coerce').fillna(0).astype(int)
pivot.index = pd.Index(pivot_index_numeric, name=pivot.index.name)
pivot = pivot.sort_index()

# Get Male/Female series or default zeros if missing
male_series = pivot.get('Male', pd.Series(0, index=pivot.index)).fillna(0).astype(int)
female_series = pivot.get('Female', pd.Series(0, index=pivot.index)).fillna(0).astype(int)

# Build output dataframe
df_out = pd.DataFrame({
    'age': pivot.index.astype(int),
    'female': female_series.values,
    'male': male_series.values
})
df_out['difference'] = df_out['male'] - df_out['female']

# Which sex is larger at each age
df_out['sex_greater_age_difference'] = np.where(df_out['male'] > df_out['female'], 'Male', np.where(df_out['female'] > df_out['male'], 'Female', 'Equal'))

# Save CSV
age_diff_fp = os.path.join(DATADIR, AGE_DIFF_FILENAME)
os.makedirs(DATADIR, exist_ok=True)
df_out.to_csv(age_diff_fp, index=False)
print('Saved age-difference CSV to', os.path.abspath(age_diff_fp))

# Display preview
try:
    display(df_out.head())
except Exception:
    print('Saved age-difference CSV to', os.path.abspath(age_diff_fp))
```

Output preview (first 5 rows of `age_difference_by_sex.csv`):

```
age,female,male,difference,sex_greater_age_difference
0,1761,1850,89,Male
1,1721,1804,83,Male
2,1810,1889,79,Male
3,1842,1937,95,Male
4,1863,1980,117,Male
```

## References
- [25-26: 4369 -- PROGRAMMING FOR DATA ANALYTICS MODULE](https://vlegalwaymayo.atu.ie/course/view.php?id=12815). This helped understand key concepts in data acquisition, cleaning, analysis, and visualisation.
- [ATU Assignment 5 Instructions](https://vlegalwaymayo.atu.ie/mod/page/view.php?id=1362128).  This helped understand the specific requirements for analysing population by age and sex.
 - [CSO FY006A API (raw CSV endpoint)](https://ws.cso.ie/public/api.restful/PxStat.Data.Cube_API.ReadDataset/FY006A/CSV/1.0/en).  this is the source of the population data used in the analysis.
 - [pandas — data analysis library (read_csv, DataFrame)](https://pandas.pydata.org/).  This helped with understanding how to manipulate and analyse tabular data.
 - [pandas.DataFrame.pivot documentation](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.pivot.html).  This was useful for reshaping the data.
 - [NumPy — numerical computing (average, sqrt)](https://numpy.org/).  This helped with performing numerical calculations, including weighted averages and standard deviations.
 - [NumPy.average documentation](https://numpy.org/doc/stable/reference/generated/numpy.average.html).  This was essential for computing weighted means.
 - [matplotlib — plotting library](https://matplotlib.org/).  This helped with creating visualisations of the analysis results.
 - [matplotlib.pyplot documentation](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.html).  This was useful for understanding how to create and customise plots.
 - [seaborn — statistical data visualization library](https://seaborn.pydata.org/).  This helped with enhancing the visual appeal of the plots.
 - [IPython / Jupyter — display utilities and notebook environment](https://ipython.org/).  This was useful for displaying dataframes and visualisations within the notebook.
 - [Weighted median explanation (Real Statistics)](https://real-statistics.com/descriptive-statistics/measures-central-tendency/weighted-mean-and-median/).  This provided a clear explanation of how to compute the weighted median.
 - [pandas.read_csv documentation](https://pandas.pydata.org/docs/reference/api/pandas.read_csv.html).  This was useful for understanding how to read CSV files into pandas DataFrames.

# END

