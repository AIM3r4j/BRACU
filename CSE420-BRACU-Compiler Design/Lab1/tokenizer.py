#reading the input
str=open("input.txt","r").read()

#splits the file's string
tokens=str.split()

#lists of all the possible C program tokens
key=["auto","break","case","char","const","continue","default","do","double","else","enum","extern","float","for","goto","if","int","long","register","return","short","signed","sizeof","static","struct","switch","typedef","union","unsigned","void","volatile","while"]
num=["0","1","2","3","4","5","6","7","8","9"]
op=["+","-","*","/","="]
lOp=[">","<",">=","<=","==","!=","&&","||"]
oth=[",",";","(",")","{","}","[","]"]


#lists for resultant tokens 
keywords=[]
numbers=[]
identifiers=[]
operators=[]
logOpertors=[]
others=[]

#methods for checking
def checkKey(token):
	if token in key:
		keywords.append(token)
		return True
	else:
		return False

def checkId(token):
	identifiers.append(token)

def checkNum(token):
	ts=token.split(".")
	if ts[0].isnumeric():
		numbers.append(token)
		return True
	else:
		return False

def checkOP(token):
	if token in op:
		operators.append(token)
		return True
	else:
		return False

def checkLOP(token):
	if token in lOp:
		logOpertors.append(token)
		return True
	else:
		return False

def checkOth(token):
	if token in oth:
		others.append(token)
		return True
	else:
		return False

#The main function
def tokenizer():
	for token in tokens:
		if checkKey(token)==False:
			if checkOP(token)==False:
				if checkLOP(token)==False:
					if checkOth(token)==False:
						if checkNum(token)==False:
							checkId(token)
		
		


#run the main function
tokenizer()


#removing the duplicates
keywords = list( dict.fromkeys(keywords))
numbers = list( dict.fromkeys(numbers))
identifiers = list( dict.fromkeys(identifiers))
operators = list( dict.fromkeys(operators))
logOpertors = list( dict.fromkeys(logOpertors))
others = list( dict.fromkeys(others))

#Printing the tokens
print("Keywords: ",end="")
for x in range(len(keywords)):print(keywords[x],end="  ")
print("\n")
print("Identifiers: ",end="")
for x in range(len(identifiers)):print(identifiers[x],end="  ") 
print("\n")
print("Math Operators: ",end="")
for x in range(len(operators)):print(operators[x],end="  ")
print("\n")
print("Logical Operators: ",end="")
for x in range(len(logOpertors)):print(logOpertors[x],end="  ")
print("\n")
print("Numerical Values: ",end="")
for x in range(len(numbers)):print(numbers[x],end="  ")
print("\n")
print("Others: ",end="")
for x in range(len(others)):print(others[x],end="  ")
print("\n")
