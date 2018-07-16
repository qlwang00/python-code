# -*- coding:utf-8 -*-


import logging,os

logger=logging.getLogger()
formatter=logging.Formatter('%(asctime)s %(levelname)-8s: %(message)s')
fh=logging.FileHandler(os.path.join(os.getcwd(),'log.txt'))
fh.setFormatter(formatter)
logger.addHandler(fh)