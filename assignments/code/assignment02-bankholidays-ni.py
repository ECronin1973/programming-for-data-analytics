# assignment02-bankholidays-ni.py
# Author: Edward Cronin

# https://pypi.org/project/requests/
# This script prints bank holidays that are unique to Northern Ireland (i.e. not shared with England/Wales or Scotland)

# Import the requests library to make HTTP requests
# https://pypi.org/project/requests/
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

# Note: This program checks for holidays unique to Northern Ireland by comparing titles with those in England & Wales and Scotland.