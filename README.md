# Programming For Data Analytics Module

Welcome to Edward Cronin's repository for the Programming For Data Analytics Module 2025/2026. This repository contains the student's submissions for the module, including detailed tasks and a comprehensive project.

## Table of Contents
[Overview](#overview)

[Author](#author)

[How to Download this Repository](#how-to-download-this-repository)

[Code of Conduct](#code-of-conduct)

[Contents](#contents)


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

### Assignment 2: Print Dates of Northern Ireland Bank Holidays from gov.uk API

### Overview
This assignment involves writing a Python script that retrieves and displays the dates of Northern Ireland bank holidays using the UK government's public API. The script utilizes the `requests` library to perform an HTTP GET request and processes the JSON response to extract relevant data.

### Objectives

- **API Interaction:** Demonstrate how to interact with a RESTful API in Python by making GET requests and parsing JSON responses.
- **Data Extraction:** Extract specific fields from the JSON payload—namely, the dates of bank holidays in Northern Ireland.
- **Output Display:** Present the extracted dates clearly in the terminal.
- **Output Formatting:** Ensure the output is clean, readable, and user-friendly, with each date printed on a separate line.

# Import relevant Libraries for Completion of Assignment Two

```python

# Import the requests library to make HTTP requests
https://pypi.org/project/requests/
import requests

```

**The following code is used to complete this task**

```python
# Import the requests library to handle HTTP requests
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
### Save the assignment02bankholdiays.py program

Save the program as assignment02bankholdiays.py.

### Run the program using Python:

```python
python assignment02bankholdiays.py
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


## Further Reading and References

To help complete this assignment, I used the following resources to learn how to work with JSON data and APIs in Python:

- **ATU Lecture: Representing Data**  
  I watched the lecture in [25-26: 4369 -- Programming For Data Analytics](https://vlegalwaymayo.atu.ie/course/view.php?id=12815) to understand how data like JSON is used in programming and how APIs provide structured data.

- **ATU Lab: Topic 01 – Representing Data**  
  I followed the lab exercises in [Lab 01 Datarepresentation.pdf](https://vlegalwaymayo.atu.ie/pluginfile.php/1590492/mod_url/intro/Lab%2001%20Datarepresentation.pdf?time=1759329869806), which showed how to read JSON from the internet using Python. This helped me understand how to access and print specific parts of the data.

- **JSON Format – json.org**  
  I used [json.org](https://www.json.org/json-en.html) to learn the basic structure of JSON, including how data is stored in key-value pairs and nested lists.

- **gov.uk Bank Holidays API**  
  I explored the [gov.uk bank holidays JSON feed](https://www.gov.uk/bank-holidays.json) to see how the data is organized and where to find the Northern Ireland holidays.

- **Python Requests Library**  
  I read the [requests library documentation](https://pypi.org/project/requests/) to understand how to fetch data from a website using Python.

- **W3Schools – Python JSON Tutorial**  
  I used [W3Schools](https://www.w3schools.com/python/python_json.asp) to learn how to convert JSON into Python dictionaries and loop through the data.

- **Real Python – API Guide**  
  I read [Real Python’s API guide](https://realpython.com/api-integration-in-python/) to learn good practices for working with APIs, including how to handle errors and format output clearly.


## References

- [25-26: 4369 -- PROGRAMMING FOR DATA ANALYTICS MODULE](https://vlegalwaymayo.atu.ie/course/view.php?id=12815)
- [Lab 01 Datarepresentation.pdf](https://vlegalwaymayo.atu.ie/pluginfile.php/1590492/mod_url/intro/Lab%2001%20Datarepresentation.pdf?time=1759329869806)
- [json.org](https://www.json.org/json-en.html)
- [gov.uk bank holidays API](https://www.gov.uk/bank-holidays.json)
- [requests library documentation](https://pypi.org/project/requests/)
- [W3Schools Python JSON guide](https://www.w3schools.com/python/python_json.asp)
- [Real Python’s guide to working with APIs](https://realpython.com/api-integration-in-python/)
