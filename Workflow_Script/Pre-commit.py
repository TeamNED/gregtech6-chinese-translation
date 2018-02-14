#!/usr/bin/python3
# Read -> filter -> write
INPUT_LOCATION = "../Weblate/zh_cn.lang"
OUTPUT_LOCATION = "../Gregtech.lang"

SOFT_TAB = "    "

inputFile = open(INPUT_LOCATION, "r", encoding="utf-8")
outputFile = open(OUTPUT_LOCATION, "w", encoding="utf-8")


def filter_string(inputLine):
    return SOFT_TAB + inputLine


resultLines = [
    "# Configuration file\n",
    "\n",
    "enablelangfile {\n",
    "    B:UseThisFileAsLanguageFile=true\n",
    "}\n",
    "\n",
    "\n",
    "languagefile {\n"
]

for line in inputFile:
    result = filter_string(line)
    if result is not None:
        resultLines.append(result)

resultLines.append("}\n")

outputFile.writelines(resultLines)

inputFile.close()
outputFile.close()
