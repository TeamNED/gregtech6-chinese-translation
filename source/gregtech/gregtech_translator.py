#-*- coding：utf-8 -*-
import yaml

from source.replacer.pattern import Pattern
from source.replacer.translator import Translator
from source.utilities.mclang import mclang_to_dict


class GregTechTranslator(Translator):
    def __init__(self, path_to_original, path_to_translated, path_to_patterns, path_to_glossary, path_to_exception):
        """ Translator for GregTech 6"""
        self.path_to_original = path_to_original
        self.path_to_translated = path_to_translated
        self.path_to_patterns = path_to_patterns
        self.path_to_glossary = path_to_glossary
        self.path_to_exception = path_to_exception
        self.load_config()
        super().__init__(self.glossary, self.patterns)

    def load_config(self):
        """ load all config-related varibles"""

        # Load patterns
        with open(self.path_to_patterns, 'r', encoding='utf-8') as pattern_file:
            pattern_content = yaml.load(pattern_file)
            self.patterns = [Pattern(x['key'], x['value'], x['token'],
                                     x['repl'], x['priority']) for x in pattern_content]
        # Load glossary
        with open(self.path_to_glossary, 'r', encoding='utf-8') as glossary_file:
            self.glossary = yaml.load(glossary_file)

        # Load excption
        with open(self.path_to_exception, 'r', encoding='utf-8') as excption_file:
            self.excptions = yaml.load(excption_file)

    def load_file(self):
        """ Reload  varibles only related to the original file and translated file"""
        # Load original
        with open(self.path_to_original, 'r', encoding='utf-8') as original_file:
            self.original = mclang_to_dict(
                original_file, lambda x: x.strip().startswith('S:'))

        # Load translated
        with open(self.path_to_translated, 'r', encoding='utf-8') as translated_file:
            self.translated = mclang_to_dict(
                translated_file, lambda x: x.strip().startswith('S:'))

    def load_all(self):
        """ load all path-related varibles"""
        self.load_file()
        self.load_config()

    def translate_all(self):
        for k, v in self.original.items():
            if k in self.excptions.keys():
                translate_result = self.excptions[k]
            else:
                translate_result = self.translate(k, v)
            if(translate_result is not None):
                self.translated[k] = translate_result  # Translate succeeded
            elif k not in self.translated.keys():
                self.translated[k] = v  # New item

    def dump_translated_to(self, path):
        with open(path, 'w', encoding='utf-8') as output:
            for k, v in sorted(self.translated.items(), key=lambda x: x[0]):
                output.write("{0}={1}\n".format(k, v))
