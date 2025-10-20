# bank_holidays.py
# Author: Edward Cronin

# Import the requests library to handle HTTP requests
import requests

# Define the URL of the UK government bank holidays API
url = "https://www.gov.uk/bank-holidays.json"

# Send a GET request to the API and store the response
response = requests.get(url)

# Parse the response content as JSON and store it in a Python dictionary
data = response.json()

# Uncomment the line below to inspect the full JSON structure (useful for debugging or exploration)
# print(data)

# Access the 'northern-ireland' section of the data
# Retrieve and print the first holiday event listed for Northern Ireland
print(data['northern-ireland']['events'][0])



'''
The output is a Python dictionary object, not raw JSON.

✅ Python Dict: The syntax uses single quotes (') for keys and string values, 
which is valid in Python but not in JSON.

❌ JSON: JSON requires double quotes (") around keys and string values. 
For example, "title": "New Year’s Day" is valid JSON, but 'title': 'New Year’s Day' is not.'''