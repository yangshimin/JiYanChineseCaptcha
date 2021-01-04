# !/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 01/04/21
# @Author  : YangShiMin
# @Email   : fausty@synnex.com
# @File    : make_dateset.py
# @Software: PyCharm
import os
import cv2
import numpy as np
from yolo.mode_one import run_click


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


def save_image_corner(image_path, corner_out_dir, title):
    """
    保存图片上左下角区域的图片，并以识别结果作为图片名
    """
    # 原图的哈希值
    image_hash_value = os.path.basename(os.path.splitext(p)[0])
    image = opencv_read_image(image_path)
    # 读取左下角区域的图片的像素值
    corner = image[344:, :116]
    # cv2.imshow("corner", corner)
    # cv2.waitKey()
    if not os.path.exists(corner_out_dir):
        os.makedirs(corner_out_dir)
    out_path = os.path.join(corner_out_dir, f"{title}_{image_hash_value}.jpg")
    opencv_write_image(out_path, corner)


def save_image_point(image_path, store_point_image_dir, store_single_chinese_dir, point_list):
    """
    用point_point_hash.ext的方式命名图片
    """
    # 原图的哈希值
    image_hash_value = os.path.basename(os.path.splitext(p)[0])
    image = opencv_read_image(image_path)
    # 保存单字符
    save_single_chinese(image, store_single_chinese_dir, point_list)

    points = [",".join(map(lambda point: str(point), list(points.values())[0])) for points in point_list]
    points_str = '_'.join(points)
    image_path = os.path.join(store_point_image_dir, f"{points_str}_{image_hash_value}.jpg")
    opencv_write_image(image_path, image)


def save_single_chinese(image_obj, store_single_dir, points_list):
    """
    根据传入的坐标保存所定位的文字
    """
    for points in points_list:
        single_chinese = list(points.keys())[0]
        point = list(points.values())[0]
        single_point_image = image_obj[point[1]:point[3], point[0]:point[2]]
        # cv2.imshow(single_chinese, single_point_image)
        # cv2.waitKey()

        image_path = os.path.join(store_single_dir, single_chinese, f'{single_chinese}.jpg')
        opencv_write_image(image_path, single_point_image)


def get_image_infos(image_path):
    """通过别人实现的模型来获取文字的定位"""
    title = None
    point_infos = dict()
    infos = run_click(image_path)
    print(infos)
    for info in infos:
        if info.get("classes") == "title":
            title = info.get("content")
        elif info.get("classes") == "target":
            point_infos[info.get("content")] = info.get("crop")
    sort_points = [{single_chinese: point_infos[single_chinese]} for single_chinese in title]
    return {"title": title, "points": sort_points}


if __name__ == "__main__":
    p = r'D:\极验文字点选原始图片\1b70675124dc61dca966680407c5f712.jpg'
    corner_image_dir = 'image_corner'
    point_image_dir = 'image_point'
    single_chinese_image_dir = 'image_single_chinese'

    infos = get_image_infos(p)
    save_image_corner(p, corner_image_dir, infos["title"])
    save_image_point(p, point_image_dir, single_chinese_image_dir, infos["points"])