#-*- coding：utf-8 -*-
import unittest
import yaml
import logging
import logging.config


class TestLogging(unittest.TestCase):

    def test_logging(self):
        with open('config/logging_test.yml', 'r') as logging_file:
            logging_config = yaml.load(logging_file)
            print(logging_config)
            logging.config.dictConfig(logging_config)
        logger = logging.getLogger()

        logger.debug('DEBUG')
        logger.info('INFO')
        logger.warning('WARNING')


if __name__ == '__main__':
    unittest.main()
