# !/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 01/06/21
# @Author  : YangShiMin
# @Email   : fausty@synnex.com
# @File    : annotation.py
# @Software: PyCharm
import os
import xml.etree.ElementTree as ET
from config import ANNOTATION_DIR
from logger.get_logger import logger
from utils import opencv_read_image, opencv_write_image


"""
    读取LabelIMG生成的xml文件, 并根据读取到的信息生成标注文件
"""


def parse_annotation_xml(file_path):
    """解析xml文件"""
    in_file = open(file_path, encoding="utf-8")
    tree = ET.parse(in_file)
    root = tree.getroot()

    for obj in root.iter('object'):
        cls = obj.find('name').text
        xml_box = obj.find('bndbox')
        point = [int(xml_box.find('xmin').text), int(xml_box.find('ymin').text),
                 int(xml_box.find('xmax').text), int(xml_box.find('ymax').text)]
        yield cls, point


def generate_single_chinese(image_path):
    """
    生成单个汉字的图片
    """
    store_image_dir = os.path.split(p)[0]
    file_name = os.path.basename(os.path.splitext(p)[0])
    # 原图的哈希值
    image_hash_value = file_name.rsplit("_")[-1]
    image = opencv_read_image(image_path)
    annotation_dir = os.path.join(os.getcwd(), ANNOTATION_DIR)
    xml_file = os.path.join(annotation_dir, f"{file_name}.xml")
    point_list = list()
    for single_chinese, points in parse_annotation_xml(xml_file):
        single_point_image = image[points[1]:points[3], points[0]:points[2]]
        # cv2.imshow(single_chinese, single_point_image)
        # cv2.waitKey()
        if single_point_image is []:
            logger.error(f"坐标点异常: {image_path}")
            return

        single_image_path = os.path.join(annotation_dir, 'single_chinese', single_chinese,
                                         f'{single_chinese}_{image_hash_value}.jpg')
        opencv_write_image(single_image_path, single_point_image)
        point_list.append(points)

    # 对原图的坐标点进行更正
    points = [",".join(map(lambda point: str(point), points)) for points in point_list]
    points_str = '_'.join(points)
    image_path = os.path.join(store_image_dir, f"{points_str}_{image_hash_value}.jpg")
    opencv_write_image(image_path, image)


if __name__ == "__main__":
    p = r'E:\个人\JiYanChineseCaptcha\annotation\87,128,155,205_93,238,154,307_00c24510c1a42a404ab6213c094a6545.jpg'
    generate_single_chinese(p)
