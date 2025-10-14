# assignment02-bankholdiays.py
# Author: Edward Cronin

# Import the requests library to make HTTP requests
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
    
    