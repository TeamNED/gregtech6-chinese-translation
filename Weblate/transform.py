#!/usr/bin/python3
print("transform.py loading")

zh_input = open("GregTech.lang", "r", encoding="utf-8")
en_input = open("Original/GregTech.lang", "r", encoding="utf-8")

zh_output = open("Weblate/zh_cn.lang", "w", encoding="utf-8")
en_output = open("Weblate/en_us.lang", "w", encoding="utf-8")

en_dict = dict()
zh_dict = dict()


def make_dict(lang_file, lang_dict):
    for line in lang_file.readlines():
        if line != None and line[0] != "#" and line[0] != "{" and "=" in line and "S:"in line:
            line_list = line.split("=", 1)        # 依据等号切分语言文件条目
            lang_dict[line_list[0]] = line_list[1]


make_dict(zh_input, zh_dict)
make_dict(en_input, en_dict)

for k, v in en_dict.items():
    en_output.writelines(k.strip(" ") + "=" + v)
    try:
        if zh_dict[k] != v:
            zh_output.writelines(k.strip(" ") + "=" + zh_dict[k])
    except:
        pass

print("transform.py loaded")
