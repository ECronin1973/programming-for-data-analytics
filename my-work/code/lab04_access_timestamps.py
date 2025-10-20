# This is code will find some text in an access file 
# Author: Edward Cronin

# this code will find the dates and time in a file, this will return the date/time in 
# this format [15/Feb/2021:18:44:39]

import re 
regex = r"\[.*\]"
filename = "../data/access.log.txt" 
with open(filename) as inputFile: 
	for line in inputFile: 
		foundTextList = re.findall(regex, line) 
		if (len(foundTextList)!= 0): 
			#print(foundTextList) 
			foundText = foundTextList[0] 
			print(foundText)