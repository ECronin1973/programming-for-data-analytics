# lab04_anonymise_ips.py

# This program anonymises the octets of IP addresses in access.log.txt
# It Xs out the last two triplets of each IP address and writes the result to a new file
# Author: Edward Cronin

import re
import os

regex = r"(\d{1,3}\.\d{1,3}\.)\d{1,3}\.\d{1,3}"
replacementText = r"\1XXX.XXX"
filename = "../data/access.log.txt"
outputFileName = "../data/lab04_anonymisedIPs.txt"

with open(filename, encoding="utf-8") as inputFile:
    with open(outputFileName, 'w', encoding="utf-8") as outputFile:
        for line in inputFile:
            newLine = re.sub(regex, replacementText, line)
            outputFile.write(newLine)

print(f"Anonymised IPs written to {os.path.abspath(outputFileName)}")
