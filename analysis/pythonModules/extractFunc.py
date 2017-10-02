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
	if line[0] == " ":
		return True
	return False


def extractLines(cont, pat):
	lines = [i for i in cont.split("\n") if i]
	functions = []
	index = 0
	while index < len(lines):
		curLine = lines[index]
		if pat.match(curLine):
			startIndex = cont.find(curLine)
			endIndex = -1
			tmpIndex = index+1
			while tmpIndex < len(lines):
				if not checkWhitespace(lines[tmpIndex]):
					subStr = lines[tmpIndex-1]
					#print("finding substr:\t", subStr)
					endIndex = cont.find(subStr, startIndex) + len(subStr)
					#print("Extracting from index ", startIndex, " to ", endIndex)
					break
				tmpIndex += 1

			if endIndex == -1:
				endIndex = len(cont) -1
			functions.append(cont[startIndex:endIndex])
		index += 1
	return functions


funcPattern = re.compile("def .+(.*):")
classPattern = re.compile("class .+:")
con = readFile("physics.py")
a = extractLines(con, funcPattern)
b = extractLines(con, classPattern)
print("There are ", len(a), " functions in the file.")
print("There are ", len(b), " classes in the file.")
print(a)
print(b)
