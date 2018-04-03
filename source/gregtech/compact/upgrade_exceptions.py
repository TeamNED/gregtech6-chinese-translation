#-*- coding：utf-8 -*-
import json
import yaml

if __name__ == '__main__':
    with open('archive/Replacer-TMR/exceptions.json', 'r', encoding='utf-8') as exception_file:
        exceptions = json.loads(exception_file.read())
        for k, v in exceptions.items():
            del exceptions[k]
            exceptions['S:'+k] = v
        with open('config/upgraded_exceptions.yml', 'w', encoding='utf-8') as output_file:
            yaml.dump(exceptions, output_file,
                      allow_unicode=True, default_flow_style=False)
