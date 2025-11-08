#!/usr/bin/env python3
"""
assignment02-bankholidays-ni.py
Author: Edward Cronin

This script prints bank holidays that are unique to Northern Ireland
(i.e. not shared with England/Wales or Scotland), using the UK Government's
public JSON API: https://www.gov.uk/bank-holidays.json
"""

import requests

def fetch_bank_holiday_data():
    """Fetches bank holiday data from the UK Government API."""
    url = "https://www.gov.uk/bank-holidays.json"
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        print(f"Error fetching data: {e}")
        return None

def find_unique_ni_holidays(data):
    """Identifies holidays unique to Northern Ireland."""
    ni_events = data['northern-ireland']['events']
    ew_titles = set(event['title'] for event in data['england-and-wales']['events'])
    scot_titles = set(event['title'] for event in data['scotland']['events'])

    unique_events = [
        event for event in ni_events
        if event['title'] not in ew_titles and event['title'] not in scot_titles
    ]
    return unique_events

def display_unique_holidays(events):
    """Prints unique Northern Ireland holidays to the terminal."""
    print("Unique Bank Holidays in Northern Ireland:")
    if events:
        for event in events:
            print(f"{event['date']} - {event['title']}")
    else:
        print("No unique holidays found.")

if __name__ == "__main__":
    data = fetch_bank_holiday_data()
    if data:
        unique_holidays = find_unique_ni_holidays(data)
        display_unique_holidays(unique_holidays)
