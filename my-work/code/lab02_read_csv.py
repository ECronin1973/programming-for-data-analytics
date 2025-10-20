'''
# PART 1: Reading CSV files
# read_csv.py

# Author: Edward Cronin

import csv 
FILENAME= "data.csv" 
DATADIR = "../data/"

try:
    with open(DATADIR + FILENAME, "rt") as fp:
        reader = csv.reader(fp, delimiter=",")
        
        for line in reader:
            print(line)            # the list contents
            print(type(line))      # shows: <class 'list'>
except FileNotFoundError:
    print(f"File not found: {DATADIR + FILENAME}")
    
    '''

# Part 2: Improved CSV reading with header handling

''' 
# modify the program to deal with the header line separately
# read_csv.py
# Author: Edward Cronin

import csv       # Imports the CSV module to handle reading CSV files
import os        # Imports OS module for file path operations

# Define the filename and directory where the CSV file is stored
FILENAME = "data.csv"
DATADIR = "../data/"
FILEPATH = os.path.join(DATADIR, FILENAME)  # Joins path components safely across OS types

# Function to read the CSV file and calculate average age
def read_and_analyze_csv(filepath):
    try:
        # Open the CSV file in text mode ('rt' = read text)
        with open(filepath, "rt") as fp:
            # Create a CSV reader object with comma delimiter
            # quoting=csv.QUOTE_NONNUMERIC converts quoted numeric fields to floats
            reader = csv.reader(fp, delimiter=",", quoting=csv.QUOTE_NONNUMERIC)

            # Read the first line (header) separately
            header = next(reader, None)
            if header:
                print(f"Header: {header}\n-------------------")  # Display header with separator

            # Initialize counters for age total and row count
            total_age = 0
            count = 0

            # Iterate over each remaining row in the CSV
            for row in reader:
                print(row)                      # Print the row as a list
                print(f"Type: {type(row)}")     # Confirm it's a list

                total_age += row[1]             # Add the age value (index 1) to total
                count += 1                      # Increment row counter

            # After reading all rows, calculate and print average age
            if count:
                average_age = total_age / count
                print(f"\nAverage age: {average_age:.2f}")  # Format to 2 decimal places
            else:
                print("No data rows found.")  # Handle case where no data rows exist

    # Handle case where file is missing
    except FileNotFoundError:
        print(f"File not found: {filepath}")

# Main execution block — only runs if script is executed directly
if __name__ == "__main__":
    read_and_analyze_csv(FILEPATH)
'''

# PART 3: Using DictReader for better readability

# read_csv_dict.py
# Author: Edward Cronin

import csv
import os

FILENAME = "data.csv"
DATADIR = "../data/"
FILEPATH = os.path.join(DATADIR, FILENAME)

def read_and_analyze_csv_dict(filepath):
    try:
        with open(filepath, "rt") as fp:
            # DictReader uses the first row as fieldnames automatically
            reader = csv.DictReader(fp, delimiter=",", quoting=csv.QUOTE_NONNUMERIC)

            total_age = 0
            count = 0

            print("Header:", reader.fieldnames)
            print("-------------------")

            for row in reader:
                print(row)                      # Each row is a dictionary
                print(f"Type: {type(row)}")     # Confirms it's a dict
                total_age += row['age']         # Access age by field name
                count += 1

            if count:
                average_age = total_age / count
                print(f"\nAverage age: {average_age:.2f}")
            else:
                print("No data rows found.")
    except FileNotFoundError:
        print(f"File not found: {filepath}")

if __name__ == "__main__":
    read_and_analyze_csv_dict(FILEPATH)

'''
There is a subtle but important distinction in how DictReader handles the header row compared to csv.reader

When you use csv.reader, the header row is treated like any other row
so you need to manually skip it (often with next(reader) or by checking linecount == 0).
If you forget to skip it, it gets counted, and you would be dividing by one too many rows
hence the need for linecount - 1.

But with csv.DictReader, the header is automatically consumed and used to map each row into a dictionary. 
The reader starts directly from the first data row.
Each line is a dictionary like {'id': 1, 'age': 20, 'name': 'Joe'}.
No need to skip the header manually.
Therefore, count reflects the actual number of data rows — no adjustment needed.

Sources: https://www.w3schools.com/python/ref_module_csv.asp
         https://realpython.com/python-csv/
'''