# Test various regex patterns on access.log.txt
# Author: Edward Cronin (adapted)

import re

filename = "../data/access.log.txt"

patterns = [
    # a. All the numbers [0-9] or \d
    ("a. All numbers [0-9] or \\d", r"\d+"),
    # b. First digits of the IP address at the start of each line
    ("b. First digits of IP at start", r"^[0-9]+\\."),
    # c. Digits at the end of each line
    ("c. Digits at end of line", r"\d+$"),
    # d. Dates and times (in brackets)
    ("d. Dates and times", r"\[.*?\]"),
    # e. Times (lazy, just 8 digits/colons)
    ("e. Times :[0-9:]{8}", r":[0-9:]{8}"),
    # f. Variable names in URLs
    ("f. Variable names in URLs", r"\w+="),
    # g. Variable values in URLs
    ("g. Variable values in URLs", r"=\w+"),
    # h. Last 2 triples of an IP address (see note)
    ("h. Last 2 triples of IP", r"\d{1,3}\.\d{1,3}(?!\.)"),
    # i. All IP addresses
    ("i. All IP addresses", r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}"),
]

try:
    with open(filename, encoding="utf-8") as f:
        lines = f.readlines()

    for label, regex in patterns:
        print(f"\n{label}\nPattern: {regex}")
        print("-" * 60)
        compiled = re.compile(regex)
        matches = []
        for line in lines:
            found = compiled.findall(line)
            if found:
                matches.extend(found)
            if len(matches) >= 10:
                break
        if matches:
            for m in matches[:10]:
                print(m)
            if len(matches) > 10:
                print(f"...and {len(matches)-10} more matches")
        else:
            print("(No matches)")
except Exception as e:
    print(f"Error: {e}")
