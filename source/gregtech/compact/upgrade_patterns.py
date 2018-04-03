#-*- coding：utf-8 -*-
import json
import yaml

if __name__ == '__main__':
    with open('archive/Replacer-TMR/patterns.json', 'r', encoding='utf-8') as pattern_file:
        patterns = json.loads(pattern_file.read())
        for item in patterns:
            item['key'] = 'S:'+item['name']
            del item['name']
            item['token'] = 'item'
            item['repl'] = item['repl'].replace('{0}', '{material}')
            item['value'] = item['value'].replace('<mw>', '<material>')
        with open('config/upgraded_patterns.yml', 'w', encoding='utf-8') as output_file:
            yaml.dump(patterns, output_file,
                      allow_unicode=True, default_flow_style=False)
