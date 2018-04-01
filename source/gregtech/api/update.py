#-*- coding：utf-8 -*-

import os
import yaml
from source.utilities.mclang import mclang_to_dict
from source.utilities.splitter import dict_split

"""Use this script only after the lang updated !"""


def update_splitted_lang():
    print('Updating splitted langs ...')
    with open('config/division.yml', 'r', encoding='utf-8') as config_file:
        config = yaml.load(config_file)
        _update_splitted_lang_version(
            'lang/source/original/GregTech.lang', config, 'en_us.lang')
        _update_splitted_lang_version(
            'lang/source/translated/GregTech.lang', config, 'zh_cn.lang')
    print('Splitted langs updated successfully')


def _update_splitted_lang_version(lang_path, config, output_name):
    with open(lang_path, 'r', encoding='utf-8') as lang_file:
        lang = mclang_to_dict(lang_file, lambda x: x.strip().startswith('S:'))
        for group_name, dic in dict_split(lang, config).items():
            print('Updating lang/'+group_name+'/'+output_name+' ...')

            if not os.path.exists('lang/'+group_name):
                os.makedirs('lang/'+group_name)
            with open('lang/'+group_name+'/'+output_name, 'w', encoding='utf-8') as output:
                for k, v in sorted(dic.items(), key=lambda x: x[0]):
                    output.write('{0}={1}\n'.format(k, v))


if __name__ == '__main__':
    update_splitted_lang()
