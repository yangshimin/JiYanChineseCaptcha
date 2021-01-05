# !/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/3/31 14:05
# @Author  : YangShiMin
# @Email   : fausty@synnex.com
# @File    : get_logger.py
# @Software: PyCharm
import logging.config
from .logging_config import LOGGING_CONFIG


class Logger(object):
    logging.config.dictConfig(LOGGING_CONFIG)
    dlogger = logging.getLogger("debug")
    ilogger = logging.getLogger("info")
    wlogger = logging.getLogger("warn")
    elogger = logging.getLogger("error")

    def debug(self, message, *args, **kwargs):
        self.dlogger.debug(message, *args, **kwargs)

    def info(self, message, *args, **kwargs):
        self.ilogger.info(message, *args, **kwargs)

    def warning(self, message, *args, **kwargs):
        self.wlogger.warning(message, *args, **kwargs, exc_info=True)

    def error(self, message, *args, **kwargs):
        self.elogger.error(message, *args, **kwargs, exc_info=True)

    def exception(self, messsage, *args, **kwargs):
        self.elogger.exception(messsage, *args, **kwargs)


logger = Logger()
