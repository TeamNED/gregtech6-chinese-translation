#-*- coding：utf-8 -*-
import argparse
import logging
import logging.config
import re
import sys

import yaml

from source.gregtech.gregtech_translator import GregTechTranslator


class RegexFilter(logging.Filter):
    def __init__(self):
        super().__init__()
        # self.set_track_args(None)

    def set_track_args(self, track, limit=None):
        self.track = track
        self.count = 0
        self.limit = limit
        if(track):
            self.track_regex = re.compile(self.track)

    def filter(self, record):
        """ Match a key with given limit and regex"""
        if record.event == 'TRANSLATING':
            self.count = self.count + 1  # only increase on new items

        if(self.track and self.track_regex.match(record.key)):
            if(self.limit is None or self.count <= self.limit):
                return 1
        return 0

    def clear_count(self):
        self.count = 0


def logging_system_init(track, limit=None):
    """If track is not none, initiate a logging system"""
    # if args.track is None:
    #    return
    with open('config/logging.yml', 'r') as logging_file:
        logging_config = yaml.load(logging_file)
        logging.config.dictConfig(logging_config)

        reg_filter = RegexFilter()
        reg_filter.set_track_args(track, limit)
        logging.getLogger('source.replacer.translator').addFilter(reg_filter)


if __name__ == '__main__':
    # parser
    parser = argparse.ArgumentParser(
        description='A regex-based replacer for GregTech6 Chinese Translasion')
    parser.add_argument('-t', '--track',
                        help='Regex expressions of which subject you want to track')
    parser.add_argument('-n', type=int,
                        help='Maxinum limit of tracking items')
    parser.add_argument('-w', '--workspace', nargs='+',
                        help='working namespace, replacer_workspace.yml will be ignored if enabled')
    args = parser.parse_args()

    # initate logging system
    logging_system_init(args.track, args.n)
    # replacing
    logger = logging.getLogger(__name__)
    logger.info('Start replacing ...')
    gt_translator = GregTechTranslator(
        None, None, 'config/patterns.yml', 'config/glossary.yml', 'config/exceptions.yml')
    with open('config/replacer_workspace.yml') as workspace_file:
        workspace = yaml.load(workspace_file)
        for item in workspace:
            if args.workspace and item not in args.workspace:
                continue

            logger.info('Working on lang/'+item)

            gt_translator.path_to_original = 'lang/'+item+'/en_us.lang'
            gt_translator.path_to_translated = 'lang/'+item+'/zh_cn.lang'
            gt_translator.load_file()

            if args.track:
                logger.debug(
                    "Tracking mode enabled, now tracking: %s", args.track)
            gt_translator.translate_all()

            gt_translator.dump_translated_to(gt_translator.path_to_translated)

    logger.info('Replacing completed successfully')
