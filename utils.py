# coding=utf8

import logging

logger = ""


def init_logger():
        global logger
        if not logger:
                logger = logging.getLogger('run_log')
                logger.setLevel(logging.INFO)

                fh = logging.FileHandler('run.log')
                fh.setLevel(logging.INFO)
                sh = logging.StreamHandler()
                sh.setLevel(logging.INFO)

                formatter = logging.Formatter('%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s')
                fh.setFormatter(formatter)
                sh.setFormatter(formatter)

                logger.addHandler(fh)
                logger.addHandler(sh)


def basic_record_log(msg):
        logging.basicConfig(level=logging.INFO,
                            format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                            datefmt='%Y-%m-%d %H:%M:%S',
                            filename='./run.log',
                            filemode='a')
        logging.info(msg)


def record_log(msg):
        init_logger()
        logger.info(msg)
