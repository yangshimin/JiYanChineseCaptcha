# !/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 01/05/21
# @Author  : YangShiMin
# @Email   : fausty@synnex.com
# @File    : utils.py
# @Software: PyCharm
import os
import glob
import cv2
import numpy as np


def opencv_read_image(image_path, flags=cv2.IMREAD_COLOR):
    """
    imread不能读取含有中文字符的路径
    flags常用值:
        cv2.IMREAD_COLOR：默认参数，读入一副彩色图片，忽略alpha通道
        cv2.IMREAD_GRAYSCALE：读入灰度图片
        cv2.IMREAD_UNCHANGED：顾名思义，读入完整图片，包括alpha通道
    参考(ImreadModes): https://docs.opencv.org/4.4.0/d4/da8/group__imgcodecs.html#ga61d9b0126a3e57d9277ac48327799c80
    """
    return cv2.imdecode(np.fromfile(image_path, dtype=np.uint8), cv2.IMREAD_COLOR)


def opencv_write_image(path, img_obj):
    """
    如果以imwrite保存图片, 图片名含有中文则会乱码
    """
    dir_path = os.path.split(path)[0]
    if not os.path.exists(dir_path):
        os.makedirs(dir_path)
    _, ext = os.path.splitext(path)
    cv2.imencode(ext, img_obj)[1].tofile(path)


def statistics_chinese_classes_count(dir_path):
    """
    统计文字类别下的数目
    """
    statistics_info = dict()
    for entry in os.scandir(dir_path):
        file_path = entry.path
        chinese_classes = os.path.basename(file_path)
        file_number = len(glob.glob(pathname=".jpg"))
        statistics_info[chinese_classes] = file_number
    return statistics_info

