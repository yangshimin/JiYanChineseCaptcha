# !/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/3/31 13:36
# @Author  : YangShiMin
# @Email   : fausty@synnex.com
# @File    : logging_config.py
# @Software: PyCharm
import os
from config import LOG_PATH

log_path = os.path.join(LOG_PATH, 'logs')
if not os.path.exists(log_path):
    os.makedirs(log_path)

LOGGING_CONFIG = {
    'version': 1,
    'incremental': False,
    'disable_existing_loggers': True,
    'formatters': {
        'verbose': {
            'format': "%(asctime)s %(processName)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s"
        },
        'simple': {
            'format': "%(asctime)s %(processName)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s"
        },
        'raw': {
            'format': "%(asctime)s %(processName)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s"
        },
    },
    'handlers': {
        'console': {
            'level': "DEBUG",
            'class': "logging.StreamHandler",
            'formatter': "raw",
            'stream': 'ext://sys.stdout'
        },
        'debug': {
            'level': "DEBUG",
            'class': "logging.handlers.RotatingFileHandler",
            'filename': os.path.join(log_path, "debug.log"),
            'formatter': "raw",
            'maxBytes': 10 * 1024 * 1024,
            'backupCount': 1,
            'encoding': "utf-8"


        },
        'info': {
            'level': "INFO",
            'class': "logging.handlers.RotatingFileHandler",
            'filename': os.path.join(log_path, "info.log"),
            'formatter': "simple",
            'maxBytes': 10 * 1024 * 1024,
            'backupCount': 3,
            'encoding': "utf-8"
        },
        'warn': {
            'level': "WARNING",
            'class': "logging.handlers.RotatingFileHandler",
            'filename': os.path.join(log_path, "warn.log"),
            'formatter': "verbose",
            'maxBytes': 10 * 1024 * 1024,
            'backupCount': 1,
            'encoding': "utf-8"
        },
        'fatal': {
            'level': "ERROR",
            'class': "logging.FileHandler",
            'filename': os.path.join(log_path, "err.log"),
            'formatter': "verbose",
            'encoding': "utf-8"
        },

    },
    'loggers': {
        'debug': {
            'handlers': ["debug", "console"],
            'level': "DEBUG",
            'propagate': False
        },
        'info': {
            'handlers': ["info", "console"],
            'level': "INFO",
            'propagate': False
        },
        'warn': {
            'handlers': ["warn", "console"],
            'level': "WARNING",
            'propagate': False
        },
        'error': {
            'handlers': ["fatal", "console"],
            'level': "ERROR",
            'propagate': False
        },
    }
}

