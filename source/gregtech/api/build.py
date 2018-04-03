#-*- coding：utf-8 -*-

import os
import yaml
from source.utilities.mclang import mclang_to_dict


def build_lang():
    print('Start building ...')
    with open('config/division.yml', 'r', encoding='utf-8') as config_file:
        config = yaml.load(config_file)
        output = {}

        for item in config:
            group_name = item['name']
            with open('lang/'+group_name+'/zh_cn.lang', 'r', encoding='utf-8') as lang_file:
                lang = mclang_to_dict(
                    lang_file, lambda x: x.strip().startswith('S:'))
                output.update(lang)
        with open('GregTech.lang', 'w', encoding='utf-8') as output_file:
            output_file.write(
                "# Configuration file\n\nenablelangfile {\n    B:UseThisFileAsLanguageFile=true\n}\n\n\nlanguagefile {\n")
            for k, v in sorted(output.items(), key=lambda x: x[0]):
                output_file.write('    {0}={1}\n'.format(k, v))
            output_file.write("}\n")

    print('Building completed successfully')


if __name__ == '__main__':
    build_lang()
