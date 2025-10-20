
# quiz.py
# Author: Edward Cronin

# This script searches for lines in '../data/sample-files/quiz.txt' that start with 'Hello ' followed by a capital letter.
# It prints each matching line to the console.

import re

regex = r"^Hello [A-Z]"
filename = r"../data/sample-files/quiz.txt"

try:
    with open(filename) as quiz_file:
        for line in quiz_file:
            search_result = re.search(regex, line)
            if search_result:
                matching_line = line
                # I set the end to blank because each line will already have a \n
                print(matching_line, end="")
except FileNotFoundError:
    print(f"Error: The file '{filename}' was not found.")
except Exception as e:
    print(f"An error occurred: {e}")
