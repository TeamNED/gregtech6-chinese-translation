#!/usr/bin/python3
# Read -> filter -> write

INPUT_LOCATION = "../Original/Gregtech.lang"
OUTPUT_LOCATION = "../Weblate/en_us.lang"


def filter_string(inputLine):
    inputLine = inputLine.strip()
    if inputLine.startswith('S:'):
        return inputLine
    else:
        return None


inputFile = open(INPUT_LOCATION, 'r', encoding="utf-8")
outputFile = open(OUTPUT_LOCATION, 'w', encoding="utf-8")
resultLines = []


for line in inputFile:
    result = filter_string(line)
    if result is not None:
        resultLines.append(result + '\n')

outputFile.writelines(resultLines)

inputFile.close()
outputFile.close()
