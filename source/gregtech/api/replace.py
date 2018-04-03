#-*- coding：utf-8 -*-
import argparse
import logging
import re
import sys

import yaml

from source.gregtech.gregtech_translator import GregTechTranslator


class PredicateCounter:
    def __init__(self, predicate_args):
        self.predicate_args = predicate_args
        self.count = 0
        self.track_regex = re.compile(
            self.predicate_args.track)

    def predicate(self, key):
        """ Match a key with given limit and regex"""
        if(self.predicate_args.track is None):
            logging.getLogger("replace.py").warning(
                "No regex given for tracking")
            return

        self.count = self.count + 1

        if(self.predicate_args.n is not None and self.count > self.predicate_args.n):
            return

        return self.track_regex.match(key)

    def clear_count(self):
        self.count = 0


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
    if args.track:
        predicate_counter = PredicateCounter(parser.parse_args())

    # initate logging system
    format_string_replace = "%(asctime)-8s %(levelname)-7s %(filename)s:%(lineno)-3d %(message)s"
    date_format_string = "%H:%M:%S"
    formatter_replace = logging.Formatter(
        format_string_replace, date_format_string)

    handler_replace = logging.StreamHandler(sys.stdout)
    handler_replace.setFormatter(formatter_replace)
    handler_replace.setLevel(logging.DEBUG)
    logger_replace = logging.getLogger("replace")
    logger_replace.setLevel(logging.DEBUG)
    logger_replace.addHandler(handler_replace)

    format_string_translator = "%(asctime)-8s %(levelname)-7s %(filename)s:%(lineno)-3d %(event)-12s %(message)s"
    formatter_translator = logging.Formatter(
        format_string_translator, date_format_string)
    handler_translator = logging.StreamHandler(sys.stdout)
    handler_translator.setFormatter(formatter_translator)
    handler_translator.setLevel(logging.DEBUG)
    logger_translator = logging.getLogger("translator")
    logger_translator.setLevel(logging.DEBUG)
    logger_translator.addHandler(handler_translator)

    # replacing
    logger_replace.info('Start replacing ...')
    gt_translator = GregTechTranslator(
        None, None, 'config/patterns.yml', 'config/glossary.yml', 'config/exceptions.yml')
    with open('config/replacer_workspace.yml') as workspace_file:
        workspace = yaml.load(workspace_file)
        for item in workspace:
            if args.workspace and item not in args.workspace:
                continue

            logger_replace.info('Working on lang/'+item)

            gt_translator.path_to_original = 'lang/'+item+'/en_us.lang'
            gt_translator.path_to_translated = 'lang/'+item+'/zh_cn.lang'
            gt_translator.load_file()

            if args.track:
                logging.getLogger("replace").debug("Tracking mode enabled, now tracking: {0}".format(
                    predicate_counter.predicate_args.track))
                gt_translator.translate_all(predicate_counter.predicate)
            else:
                gt_translator.translate_all()

            gt_translator.dump_translated_to(gt_translator.path_to_translated)

    logger_replace.info('Replacing completed successfully')
