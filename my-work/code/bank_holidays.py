# bank_holidays.py

# Author: Edward Cronin

import requests 
 
url =" https://www.gov.uk/bank-holidays.json" 
response = requests.get(url) 
data = response.json() 
# print(data)

# program modified to only print the first holiday in northern ireland
print(data['northern-ireland']['events'][0])



'''
The output is a Python dictionary object, not raw JSON.

✅ Python Dict: The syntax uses single quotes (') for keys and string values, 
which is valid in Python but not in JSON.

❌ JSON: JSON requires double quotes (") around keys and string values. 
For example, "title": "New Year’s Day" is valid JSON, but 'title': 'New Year’s Day' is not.'''