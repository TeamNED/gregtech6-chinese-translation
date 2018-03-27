#!/usr/bin/python3
import os

print("cleanup_obsoleted_items.py loading")

ORIGINAL_LOCATION = "Original/Gregtech.lang"
TRANSLATED_LOCATION = "Gregtech.lang"
OBSOLETED_ZH_CN_LOCATION = "Archive/zh_cn_obsoleted.lang"

en_file = open(ORIGINAL_LOCATION, "r", encoding="utf-8")
zh_file = open(TRANSLATED_LOCATION, "r+", encoding="utf-8")


en_dict = dict()
zh_dict = dict()
zh_output_dict = dict()


def make_dict(lang_file, lang_dict):
    for line in lang_file.readlines():
        if line != None and line[0] != "#" and line[0] != "{" and "=" in line and "S:"in line:
            line_list = line.split("=", 1)        # 依据等号切分语言文件条目
            lang_dict[line_list[0].strip()] = line_list[1].strip()


make_dict(en_file, en_dict)
make_dict(zh_file, zh_dict)


if os.path.isfile(OBSOLETED_ZH_CN_LOCATION):
    # open existed file ready to write
    zh_output_file = open(OBSOLETED_ZH_CN_LOCATION, "r+", encoding="utf-8")
    make_dict(zh_output_file, zh_output_dict)
    zh_output_file.seek(0)
else:
    # create a new file if not exist
    zh_output_file = open(OBSOLETED_ZH_CN_LOCATION, "w", encoding="utf-8")


zh_file.seek(0)  # restore location ready to write


for k, v in sorted(zh_dict.items(), key=lambda x: x[0]):
    if k not in en_dict.keys():
        zh_output_dict[k] = v  # k is an obsoleted item, updating

for k, v in sorted(zh_output_dict.items(), key=lambda x: x[0]):
    zh_output_file.writelines(k.strip(" ") + "=" + zh_output_dict[k]+"\n")

# Writes heading
zh_file.write(
    "# Configuration file\n\nenablelangfile {\n    B:UseThisFileAsLanguageFile=true\n}\n\n\nlanguagefile {\n")

for k, v in sorted(en_dict.items(), key=lambda x: x[0]):
    if(k not in zh_dict.keys()):
        # new item, using original
        zh_file.writelines("\t"+k.strip(" ") + "=" + v+"\n")
    else:
        # translated item, porting
        zh_file.writelines("\t"+k.strip(" ") + "=" + zh_dict[k]+"\n")


# Writes ending
zh_file.write("}\n")

zh_file.truncate()
zh_output_file.truncate()

zh_file.close()
zh_output_file.close()
en_file.close()

print("cleanup_obsoleted_items.py loaded")
