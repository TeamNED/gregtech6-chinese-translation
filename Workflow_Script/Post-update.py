#!/usr/bin/python3
# Read -> filter -> write
import re

INPUT_LOCATION = "../Original/Gregtech.lang"
OUTPUT_LOCATION = "../Weblate/en_us.lang"
# Regex patterns: matching every language items
# e.g. "S:enchantment.damage.endermen=Disjunction"
patternTargetKeyValuePair = re.compile("S:.*=.*")


def filter_string(pattern, inputLine):
    reg_match = re.search(pattern, inputLine)
    if reg_match is not None:
        return reg_match.group()
    else:
        return None


inputFile = open(INPUT_LOCATION, 'r', encoding="utf-8")
outputFile = open(OUTPUT_LOCATION, 'w', encoding="utf-8")
resultLines = []

for line in inputFile:
    result = filter_string(patternTargetKeyValuePair, line)
    if result is not None:
        resultLines.append(result + '\n')

outputFile.writelines(resultLines)

inputFile.close()
outputFile.close()
