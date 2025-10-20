
# This script tests a list of regular expressions on the file '../data/sample-files/quiz.txt'.
# For each pattern, it prints and writes to an output file the matching lines and their line numbers.
# Results are saved to '../data/quiz_results.txt'.
# Author: Edward Cronin

import re

import os
filename = os.path.join(os.path.dirname(__file__), "..", "data", "sample-files", "quiz.txt")

# List of regex patterns to test
patterns = [
    ("a", "hello"),
    ("b", "Hello"),
    ("c", "^Hello"),
    ("d", "^Hell*o"),
    ("e", "^Hell+o"),
    ("f", "^Hell?o"),
    ("g", "^hello [A-Z]"),
    ("h", "^Hello [A-Z]"),
    ("i", "="),
    ("j", "#"),
    ("k", r"\["),
    ("l", "^$")
]

try:

    with open(filename) as quizFile:
        lines = quizFile.readlines()

    output_lines = []
    for label, regex in patterns:
        header = f"\n{label}. Pattern: '{regex}'\n" + ("-" * 50) + "\n"
        print(header, end="")
        output_lines.append(header)
        found = False
        for idx, line in enumerate(lines, 1):
            searchResult = re.search(regex, line)
            if searchResult:
                found = True
                numbered_line = f"Line {idx}: {line}"
                print(numbered_line, end="")
                output_lines.append(numbered_line)
        if not found:
            print("(No matches)\n")
            output_lines.append("(No matches)\n")

    # Write results to file in data directory
    results_path = os.path.join(os.path.dirname(__file__), "..", "data", "quiz_results.txt")
    with open(results_path, "w", encoding="utf-8") as f:
        f.writelines(output_lines)

except FileNotFoundError:
    print(f"Error: The file '{filename}' was not found.")
except Exception as e:
    print(f"An error occurred: {e}")
