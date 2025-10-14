# Programming For Data Analytics Module

Welcome to Edward Cronin's repository for the Programming For Data Analytics Module 2025/2026. This repository contains the student's submissions for the module, including detailed tasks and a comprehensive project.

## Table of Contents
[Overview](#overview)

[Author](#author)

[How to Download this Repository](#how-to-download-this-repository)

[Code of Conduct](#code-of-conduct)

[Contents](#contents)

[Assignment 2 (Part A): Northern Ireland bank holidays](#assignment-2-northern-ireland-bank-holidays)

[Assignment 2 (Part B): Bank holidays unique to Northern Ireland](#assignment-2-bank-holidays-unique-to-northern-ireland)

[Assignment 3 domains](#assignment-3-domains)

[Assignment 3 Pie Chart Image](#assignment-3-pie-chart-output)

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

#### Objectives

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

This part of the assignment involves enhancing the initial script to identify and display bank holidays that are unique to Northern Ireland, meaning they are not observed in England, Wales, or Scotland. This requires comparing the holiday titles across the different regions and filtering out any that are shared.

#### Objectives
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

### Objectives:
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

The pie chart below visualizes the distribution of the top email domains found in the dataset. There are only three email domains identified and represented.

![Pie chart of email domains](assignments/data/assignment-03-pie-chart.jpg)

### References

- ATU Lecture: Acquiring data
  I watched the lecture in [25-26: 4369 -- Programming For Data Analytics](https://vlegalwaymayo.atu.ie/course/view.php?id=12815) to understand how to acquire data from various sources, including downloading datasets from the web. This helped me understand the importance of data acquisition in data analytics.

  - ATU Assignment 3 domains Instructions
  I followed the assignment instructions provided in [Assignment 3 domains](https://vlegalwaymayo.atu.ie/mod/page/view.php?id=1204040) to complete the task of extracting email domains and visualizing them using a pie chart. The instructions guided me through the steps of data extraction, processing, and visualisation.

- [`assignment03-pie.ipynb`](assignments/notebooks/assignment03-pie.ipynb)  
  Main notebook for Assignment 3. It loads the dataset, extracts email domains, counts them, and creates a pie chart.

- [`people.csv`](assignments/data/people.csv)  
  Dataset of 1,000 people. The `Email` column is used to extract domain names for analysis.

- [pandas](https://pandas.pydata.org/)  
  Used to load the dataset (`read_csv`), extract email domains from strings (`str.split`), and count how often each domain appears (`value_counts`).

- [matplotlib](https://matplotlib.org/)  
  Used to create and customize the pie chart (`plot.pie`), adjust layout (`tight_layout`), display the chart (`show`), and save it as an image file (`savefig`).

- [seaborn](https://seaborn.pydata.org/)  
  Used to apply a pastel color palette for the pie chart (`color_palette`) to improve visual clarity and style.

# END