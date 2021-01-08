# !/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 01/04/21
# @Author  : YangShiMin
# @Email   : fausty@synnex.com
# @File    : config.py
# @Software: PyCharm
import os

# 保存日志的目录
LOG_PATH = os.getcwd()


# 验证码图片的宽和高
CODE_WIDTH, CODE_HEIGHT = 333, 333

# 验证码图片左上角的坐标
CODE_START_POINT = (615, 421)

# 验证码确认按钮左上角的坐标
CONFIRM_START_POINT = (826, 763)

# 存放语序图片的目录
CORNER_IMAGE_DIR = 'sample/image_corner'

# 存放以坐标点命名的图片目录
POINT_IMAGE_DIR = 'sample/image_point'

# 存放汉字类别的单字图片目录
SINGLE_CHINESE_IMAGE_DIR = 'sample/image_single_chinese'

# 存放annotation xml文件的目录
ANNOTATION_DIR = 'annotation'
