# -*- coding:utf-8 -*-


import logging
import os

from logger import logger

def fun():
    pass

try:
    fun(1)
except:
    logger.exception('Error Message')


print(11)