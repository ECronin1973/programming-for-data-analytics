# Programming For Data Analytics Module

Welcome to Edward Cronin's repository for the Programming For Data Analytics Module 2025/2026. This repository contains the student's submissions for the module, including detailed tasks and a comprehensive project.

## Table of Contents
[Overview](#overview)

[Author](#author)

[How to Download this Repository](#how-to-download-this-repository)

[Code of Conduct](#code-of-conduct)

[Contents](#contents)

[Assignment 2 (Part A): Northern bank holidays](#assignment-2-northern-bank-holidays)

[Assignment 2 (Part B): Northern bank holidays unique to Northern Ireland](#assignment-2-northern-bank-holidays-part-b)

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

### Assignment 2: Northern bank holidays (Part A)

### Overview
This assignment involves creating a Python script that connects to the UK government's public API to get a list of bank holidays. It uses the requests library to send a GET request and then reads the JSON data returned. The script focuses on holidays listed under Northern Ireland, but some of these dates may also be shared with other UK regions like England, Wales, or Scotland.

### Objectives

- **API Interaction:** Demonstrate how to interact with a RESTful API in Python by making GET requests and parsing JSON responses.
- **Data Extraction:** Extract specific fields from the JSON payload—namely, the dates of bank holidays in Northern Ireland.
- **Output Display:** Present the extracted dates clearly in the terminal.
- **Output Formatting:** Ensure the output is clean, readable, and user-friendly, with each date printed on a separate line.

# Code Used To Complete Part A

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

# Loop through each event and print only the date
print("Bank Holiday Dates in Northern Ireland:")
for event in ni_events:
    print(event['date'])

```
### Save the assignment02-bankholidays.py program

Save the program as assignment02-bankholidays.py.

### Run the program using Python:

```python
python assignment02-bankholidays.py
```

### Expected Output

When the script is executed, it prints the dates of upcoming Northern Ireland bank holidays to the terminal. The output shown below is a truncated version created by the student for demonstration purposes:

```plaintext
Bank Holiday Dates in Northern Ireland:
2025-12-25
2025-12-26
2026-01-01
2026-03-17
2026-04-03
2026-04-06
2026-05-04
2026-05-25
2026-07-13
2026-08-31
2026-12-25
2026-12-28
2027-01-01
2027-03-17
2027-03-26
2027-03-29
2027-05-03
2027-05-31
2027-07-12
2027-08-30
2027-12-27
2027-12-28

```

### Assignment 2: Northern bank holidays (Part B)

This part of the assignment involves enhancing the initial script to identify and display bank holidays that are unique to Northern Ireland, meaning they are not observed in England, Wales, or Scotland. This requires comparing the holiday titles across the different regions and filtering out any that are shared.

### Objectives
- **Data Comparison:** Compare holiday titles across Northern Ireland, England/Wales, and Scotland to identify unique holidays.
- **Conditional Logic:** Implement logic to filter out shared holidays and retain only those unique to Northern Ireland.
- **Output Clarity:** Ensure the output clearly indicates which holidays are unique to Northern Ireland, along with their dates.


# Code Used To Complete Part B

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
### Save the assignment02-bankholidays-ni.py program

Save the program as assignment02-bankholidays-ni.py.

### Run the program using Python:

```python
python assignment02-bankholidays-ni.py
```

### Expected Output

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