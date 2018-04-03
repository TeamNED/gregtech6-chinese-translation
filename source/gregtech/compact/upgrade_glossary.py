#-*- coding：utf-8 -*-
import json
import yaml

if __name__ == '__main__':
    with open('archive/Replacer-TMR/glossary.json', 'r', encoding='utf-8') as glossary_file:
        glossary = json.loads(glossary_file.read())
        for k, v in glossary.items():
            if type(v) is dict:
                new_value = []
                for k2, v2 in v.items():
                    if k2 != '.*':
                        new_value.append({'value': v2, 'regex': 'S:'+k2})
                new_value.append({'regex': '.*', 'value': v['.*']})
                glossary[k] = new_value
        output_glossary = {'material': glossary}
        with open('config/upgraded_glossary.yml', 'w', encoding='utf-8') as output_file:
            yaml.dump(output_glossary, output_file,
                      allow_unicode=True, default_flow_style=False)
