#-*- coding：utf-8 -*-
import unittest
import yaml
from source.utilities.mclang import mclang_to_dict
from source.utilities.splitter import dict_split


class TestSplitter(unittest.TestCase):

    def test_splitter(self):

        lang_file = open('test/test3.lang', 'r', encoding='utf-8')
        lang = mclang_to_dict(lang_file, lambda x: x.strip().startswith('S:'))

        config_file = open('config/division.yml', 'r', encoding='utf-8')
        config = yaml.load(config_file)

        test_result = dict_split(lang, config)
        test_ans = {'tooltip': {'S:gt.tooltip.blah': 'blah tooltip', 'S:gt.multiitem.blaah.tooltip': 'blaah tooltip'},
                    'gt_multiitem': {'S:gt.multiitem.blaah.name': 'blaah'}, 'misc': {'S:enchantment.blaaah': 'enchantment blaaah'}}

        self.assertDictEqual(test_result, test_ans)


if __name__ == '__main__':
    unittest.main()
