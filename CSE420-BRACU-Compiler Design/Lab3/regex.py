#importing regex library
import re

#initialing the lists
patterns=[]
strings=[]
matches=[]
#function for matching with patterns
def match(strings, patterns):
	for s in strings:
		for p in patterns:
			if re.search(p,s) is not None:
				matches.append(patterns.index(p)+1)
				break
		else:
			matches.append(0)
#function for printing the output
def output(matches):
	print("\nOutput:")
	for m in matches:
		if m == 0:
			print("No,0")
		else:
			print("Yes,"+str(m))
			
#the instructions that will run
#taking the pattern input
inputCount=int(input("Please enter the number of patterns to match with: "))
for i in range(inputCount):
	pattern=str(input("Enter the pattern: "))
	patterns.append(pattern)
#taking the string input
stringCount=int(input("Please enter the number of strings to match: "))
for s in range(stringCount):
	string=str(input("Enter the string: "))
	strings.append(string)
#calling the functions
match(strings, patterns)
output(matches)