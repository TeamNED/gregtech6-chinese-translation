#-*- coding：utf-8 -*-
import unittest
import yaml
from source.replacer.pattern import Pattern
from source.replacer.translator import Translator
from source.utilities.mclang import mclang_to_dict


class TestGlossary(unittest.TestCase):

    def test_glossary(self):
        pattern_file = open('test/test4_patterns.yml', 'r', encoding='utf-8')
        pattern_content = yaml.load(pattern_file)
        pattern_list = [Pattern(x['key'], x['value'], x['token'],
                                x['repl'], x['priority']) for x in pattern_content]

        lang_file = open('test/test4.lang', 'r', encoding='utf-8')
        lang = mclang_to_dict(lang_file, lambda x: x.strip().startswith('S:'))

        glossary_file = open('test/test4_glossary.yml', 'r', encoding='utf-8')
        glossary = yaml.load(glossary_file)

        translator = Translator(glossary, pattern_list)

        test_result = {k:  str(translator.translate(k, v))
                       for k, v in lang.items()}
        test_ans = {'S:gt.multiitem.bumblebee.dark.name': '黑暗大黄蜂',
                    'S:gt.multiitem.bumblebee.void.name': '虚空大黄蜂', 'S:oredict.ingotVoid': '再构煤晶锭'}

        self.assertDictEqual(test_result, test_ans)


if __name__ == '__main__':
    unittest.main()
