
# This script tests the regex pattern '\d+$' (matches digits at the end of a line)
# on the file '../data/access.log.txt'.
# It prints the total number of lines, the first line, regex matches on the first line,
# and counts how many lines end with digits.

import re
import os

# Test the regex
regex = r"\d+$"
filename = "../data/access.log.txt"

if not os.path.exists(filename):
    print(f"File not found: {filename}")
else:
    with open(filename, encoding='utf-8') as inputFile:
        lines = inputFile.readlines()
        print(f"Total lines: {len(lines)}")
        if not lines:
            print("File is empty.")
        else:
            # Check first line
            first_line = lines[0]
            print(f"\nFirst line: {repr(first_line)}")
            print(f"First line ends with: {repr(first_line[-20:])}")
            # Test regex
            result = re.findall(regex, first_line)
            print(f"Regex match on first line: {result}")
            # Try without newline
            result2 = re.findall(regex, first_line.strip())
            print(f"Regex match on stripped line: {result2}")
            # Count matches
            count = 0
            for line in lines:
                if re.findall(regex, line.strip()):
                    count += 1
            print(f"\nTotal matches with strip(): {count}")
