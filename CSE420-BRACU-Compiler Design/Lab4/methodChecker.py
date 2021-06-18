#reading the file
file=open("input.txt","r")

#importing the python regex library
import re

#regex for methods
regexMethod="(public|private)*( static|static)*[ (void|int|string|float|double)]+ [a-z][a-zA-Z0-9]+\(((\ )?(\,|\, )*((int|string|float|double)+ [a-zA-Z]+)*)*\)"

#getting every line as a string from the file
strings=[]
for lines in file:
	strings.append(lines)

#matching lines with the regex and adding matches to the temporary method list
tempMethods=[]
for string in strings:
	if re.search(regexMethod, string)!=None:
		tempMethods.append(re.search(regexMethod, string).group())

#checking if method names are proper java identifiers
methods=[]
javakeywords=['abstract', 'continue', 'for', 'new', 'switch', 'assert', 'default', 'if', 'package', 'synchronized', 'boolean', 'do', 'goto', 'private', 'this', 'break', 'double', 'implements', 'protected', 'throw', 'byte', 'else', 'import', 'public', 'throws', 'case', 'enum', 'instanceof', 'return', 'transient', 'catch', 'extends', 'int', 'short', 'try', 'char', 'final', 'interface', 'static', 'void', 'class', 'finally', 'long', 'strictfp', 'volatile', 'const', 'float', 'native', 'super', 'while']
regexProper="(public|private)*( static|static)*[ (void|int|string|float|double)]+ "
for  tempMethod in tempMethods:
	for keyword in javakeywords:
		if re.search(regexProper+str(keyword), tempMethod)!=None:
			tempMethods.remove(tempMethod) #removing the improper methods
			break
		else:
			continue
methods=tempMethods #adding the proper ones to proper method list
	
#adding method name to a list
methodName=[]
for method in methods:
	s=method.split("(")
	t=s[0].split(" ")
	methodName.append(t[-1]+"("+s[-1])

#adding method return type to a list
returnType=[]
regexReturntype="void|int|string|float|double"
for method in methods:
	returnType.append(re.search(regexReturntype, method).group())

#printing the output
for i in range(len(methods)):
	print(methodName[i]+", Return type: "+returnType[i])