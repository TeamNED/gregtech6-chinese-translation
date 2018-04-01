#-*- coding：utf-8 -*-
import yaml

from source.gregtech.gregtech_translator import GregTechTranslator

if __name__ == '__main__':
    print('Start replaceing ...')
    gt_translator = GregTechTranslator(
        None, None, 'config/patterns.yml', 'config/glossary.yml', 'config/exceptions.yml')
    with open('config/replacer_workspace.yml') as workspace_file:
        workspace = yaml.load(workspace_file)
        for item in workspace:
            print('Working on lang/'+item)
            gt_translator.path_to_original = 'lang/'+item+'/en_us.lang'
            gt_translator.path_to_translated = 'lang/'+item+'/zh_cn.lang'
            gt_translator.load_file()
            gt_translator.translate_all()
            gt_translator.dump_translated_to(gt_translator.path_to_translated)

    print('Replacing completed successfully')
