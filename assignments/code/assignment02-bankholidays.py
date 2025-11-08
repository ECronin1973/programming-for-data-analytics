#!/usr/bin/env python3
"""
assignment02-bankholidays.py
Author: Edward Cronin

Fetches and displays upcoming bank holidays in Northern Ireland
using the UK Government's public JSON API.
"""

import requests

def fetch_bank_holidays(region="northern-ireland"):
    url = "https://www.gov.uk/bank-holidays.json"
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        return data[region]["events"]
    except requests.RequestException as e:
        print(f"Error fetching data: {e}")
        return []

def display_bank_holidays(events):
    print("Bank Holidays in Northern Ireland:")
    for event in events:
        print(f"{event['date']} - {event['title']}")

if __name__ == "__main__":
    holidays = fetch_bank_holidays()
    display_bank_holidays(holidays)
