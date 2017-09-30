import re
def readFile(path="./test.py"):
	with open(path, "r") as f:
		content = f.read()
	return content


def checkWhitespace(line):
	if not line:
		return True
	if line[0] == "\n":
		return True
	if ord(line[0]) == 9:
		#decimal for horizontal tab
		return True
	if ord(line[0]) == 10:
		#decimal for new line
		return True
	return False


# SOMEthing to DO WITH THE SCOPE OF I - NOT BEING UPDATED
def extractLines(cont):
	lines = [i for i in cont.split("\n") if i]
	funcPattern = re.compile("def .+(.*):")
	functions = []
	#print(lines)

	index = 0
	while index < len(lines):
		curLine = lines[index]
		if funcPattern.match(curLine):
			startIndex = cont.find(curLine)
			endIndex = -1
			tmpIndex = index+1
			#iterate and find the end of the func
			while tmpIndex < len(lines):
				if not checkWhitespace(lines[tmpIndex]):
					subStr = lines[tmpIndex-2] + "\n" + lines[tmpIndex-1]
					endIndex = cont.find(subStr) + len(subStr)
					break
				tmpIndex += 1

			if endIndex == -1:
				#means end of func not found, go to end of file
				endIndex = len(cont) -1
			#now read from startIndex to endIndex and append to functions
			functions.append(cont[startIndex:endIndex])
		index += 1
	return functions


a = extractLines(readFile("./extractFunc.py"))
for i in a:
	print(i)
	print("-"*30)
